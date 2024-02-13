#!/bin/bash
email=${ACUNETIX_EMAIL}
password=${ACUNETIX_PASSWORD}

# if [ -z "$email" ] || [ -z "$password" ]; then
#   echo "Email or password environment variables are not set."
#   exit 1
# fi


# HELLO from entypoint...
/bin/sh /awvs_start.sh &

# Just testing
sleep 15



# assuming that script will retrive token
token=$(/bin/bash /home/acunetix/.acunetix/change_credentials.sh ${email} ${password} | grep "GREP_ME" | cut -c 8- )

# check if token found
if [ -n "$token" ]; then
  echo "API Token: $token"
  
  # do smothing with token
  # TODO: Add to database...
  echo "$token" > /api_token.txt
  
  # something else if ness.
else
  # on fail
  echo "Failed to obtain API token."
fi

# not sure about that
# tail -f /dev/null
