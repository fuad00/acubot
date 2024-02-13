#!/bin/bash

linux_user=acunetix
product_name=acunetix

base_folder="/home/$linux_user/.$product_name"

get_settings_from_ini()
{
    db_user=$(awk -F "=" '/databases.connections.master.connection.user/ {print $2}' $base_folder/wvs.ini)
    if [ -z "$db_user" ]; then
        echo "Acunetix installation found at $base_folder, but has invalid wvs.ini file. Aborting installation."
        echo
        exit -1
    fi

    db_host=$(awk -F "=" '/databases.connections.master.connection.host/ {print $2}' $base_folder/wvs.ini)
    if [ -z "$db_host" ]; then
        echo "Acunetix installation found at $base_folder, but has invalid wvs.ini file. Aborting installation."
        echo
        exit -1
    fi

    db_port=$(awk -F "=" '/databases.connections.master.connection.port/ {print $2}' $base_folder/wvs.ini)
    if [ -z "$db_port" ]; then
        echo "Acunetix installation found at $base_folder, but has invalid wvs.ini file. Aborting installation."
        echo
        exit -1
    fi

    db_name=$(awk -F "=" '/databases.connections.master.connection.db/ {print $2}' $base_folder/wvs.ini)
    if [ -z "$db_name" ]; then
        echo "Acunetix installation found at $base_folder, but has invalid wvs.ini file. Aborting installation."
        echo
        exit -1
    fi

    db_password=$(awk -F "=" '/databases.connections.master.connection.password/ {print $2}' $base_folder/wvs.ini)
    if [ -z "$db_password" ]; then
        echo "Acunetix installation found at $base_folder, but has invalid wvs.ini file. Aborting installation."
        echo
        exit -1
    fi

    gr="(?<=wvs\.app_dir\=~\/\.$product_name\/v_)[0-9]+(?=\/scanner)"
    version_numeric=$(cat $base_folder/wvs.ini | grep -o -P $gr)
    version="v_$version_numeric"
}

get_settings_from_ini
db_pgdir="$base_folder/$version/database"


run_db_sql(){

    sudo -u $linux_user PGPASSWORD=$db_password $db_pgdir/bin/psql -q -d $db_name -t -c "$1" -b -h $db_host -p $db_port -U $db_user -v ON_ERROR_STOP=1
    if [ "$?" -ne 0 ]; then
        echo "Error running SQL command. Exiting."
        exit -1
    fi
}


default_command() {
  qr=$(run_db_sql "SELECT email FROM users WHERE user_id='986ad8c0a5b3df4d7028d5f3c06e936c'")
  master_user=$(echo "$qr" | awk '{$1=$1};1')

  echo "Master user found: $master_user"

  master_user=$1
  master_password=$2

  master_user=${master_user,,}

  echo "Using master user $master_user"

  if [ ${#master_password} -lt 8 ]; then
      echo "Password requirements not met."
      exit 1
  fi

  run_db_sql "UPDATE users SET email='$master_user', password=encode(digest('$master_password', 'sha256'), 'hex'), pwd_expires = null, otp=null, otp_required=false WHERE user_id='986ad8c0a5b3df4d7028d5f3c06e936c'"
  run_db_sql "update users set pwd_expires = NOW() + interval '1 day' * pwd_max_age where pwd_max_age is not null and pwd_max_age != 0 and user_id='986ad8c0a5b3df4d7028d5f3c06e936c'"
  run_db_sql "DELETE FROM ui_sessions"

  reset_api_key $master_user
}

reset_api_key() {
  qr=$(run_db_sql "SELECT replace(user_id::text, '-', '') FROM users WHERE email='$1'")
  user_id=$(echo "$qr" | awk '{$1=$1};1')

  if [ -z "$user_id" ]; then
    echo "User $1 not found"
    exit 1
  fi

  db_api_key=$(tr -dc a-f0-9 </dev/urandom | head -c 32 ; echo '')

  run_db_sql "UPDATE users SET api_key='$db_api_key' WHERE user_id='$user_id'"

  echo "GREP_ME1$user_id$db_api_key"
}

if [ "$#" -eq 2 ]; then
  default_command "$1" "$2"
else
  echo "Usage: $0 <new_email> <new_password>"
  exit 1
fi