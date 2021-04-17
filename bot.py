import requests
import sqlite3
import telebot
import warnings
import time


warnings.filterwarnings('ignore', message='Unverified HTTPS request')


tg_bot_token = "" # Example: "496545159:AAGjUrqG3f6HGChpOYkLYbblitb_TRbdbSY"
chat_id =   # Example: -1001351824461

api_key = "" # Example: "1986ad8e936ca9bf5a50fev0reebfb1tt4b3rtb22a2c8b793c1c0946b"
host = "" # Example: "https://localhost:3443"
recheck_sec = 600


# init bot token
bot = telebot.TeleBot(tg_bot_token)

# init db
conn = sqlite3.connect('acu.db', check_same_thread=False)
c = conn.cursor()

def firstinit():
    #crete count table if not exixsts
    sql19 = 'create table if not exists count (tbl VARCHAR(10), vt_id VARCHAR(64), vt_name VARCHAR(200))'
    c.execute(sql19)
    c.execute("INSERT INTO count VALUES('vuln1', '8d36f5ef-3e32-748c-13aa-c217bae63383', '[🔡] Configuration code disclosure')")
    c.execute("INSERT INTO count VALUES('vuln2', 'd4b48cfc-be42-03bf-fcdf-822909b4ab3e', '[😼] Git repository found')")
    c.execute("INSERT INTO count VALUES('vuln3', '2f8c854b-047c-73ad-cc4e-1a6a77b7fff0', '[📦] Possible database backup')")
    c.execute("INSERT INTO count VALUES('vuln4', '555af421-ba31-1924-5f7c-14c347d5fda1', '[🗜️] Remote file inclusion')")
    c.execute("INSERT INTO count VALUES('vuln5', 'f78536f5-0b3c-ca29-dd6b-dd35b85d0312', '[📂] Directory traversal')")
    c.execute("INSERT INTO count VALUES('vuln6', 'db04b846-7dec-fb62-f12d-1a152945cdae', '[💉] SQL Injection')")
    c.execute("INSERT INTO count VALUES('vuln7', '5b3895f4-9656-d13f-8a83-5d9dabcdadf5', '[📤] File upload')")
    c.execute("INSERT INTO count VALUES('vuln8', 'be51ec83-1af0-9961-fbf3-5db05859eecb', '[🔓] Weak password')")
    c.execute("INSERT INTO count VALUES('vuln9', '7777c336-316c-a967-2acd-45b7ee798413', '[📦] Backup files')")
    c.execute("INSERT INTO count VALUES('vuln10', 'b53afc6c-83c3-7ea8-ce7b-d5f5fb01b7d7', '[📃] Directory listings')")
    c.execute("INSERT INTO count VALUES('vuln11', '6c3a3195-107f-7bc2-c254-f3fac0f93e46', '[🗃️] Folder backup')")
    c.execute("INSERT INTO count VALUES('vuln12', '57e1a6a4-f21e-8d9c-e678-c32be439ee63', '[🛸] Adminer 4.6.2')")
    conn.commit()

    #crete stats table if not exists
    sql = 'create table if not exists ' + 'stats' + ' (high INT, med INT, low INT, total INT)'
    c.execute(sql)
    conn.commit()
firstinit()


sql2 = """SELECT * FROM count"""
yo = c.execute(sql2)
out2 = c.fetchall()


def main():
    sql2 = """SELECT * FROM count"""
    yo = c.execute(sql2)
    out2 = c.fetchall()

    

    for x in range(12):
        sql4 = """SELECT * FROM vuln{}""".format(str(x+1))
        go3 = c.execute(sql4)
        webwite_name = c.fetchall()
        sqlcount = """SELECT count() FROM vuln{}""".format(str(x+1))
        go4 = c.execute(sqlcount)
        rowcount = c.fetchall()
        
        resp = requests.get(host + '/api/v1/vulnerability_groups', headers={'x-auth': api_key,}, params=(('q', 'vt_id:' + out2[x][1] + ';status:open'),), verify=False)
        out = resp.json()["items"]
        
        for lox in range(len(out)):

        
            try:
            #DB variables for compairing:
            
                #currnet website name - webwite_name[lox][1]
                #currnet vulns count of this website - webwite_name[lox][2]
                #current websit id - webwite_name[lox][0]
            
                #print("From db: "  + webwite_name[lox][1] + " " + str(webwite_name[lox][2]))
        
            #ACU variables for compairing:
        
                #currnet website name - out[lox]["name"]
                #currnet vulns count of this website - out[lox]["count"]
                #current websit id -  out[lox]["id"]
            
                sql5 = """select count from vuln{} where website = '{}'""".format(str(x+1), out[lox]["name"])
                tmp1 = c.execute(sql5)
                webcount = c.fetchone()
                #print(str(webcount))
                if str(webcount) == 'None':
                    bot.send_message(chat_id, "Первая уязвимость _{}_ на `{}` !".format(out2[x][2], out[lox]["name"]), parse_mode= 'Markdown')
                    sql10 = """insert into vuln{} (id, website, count) VALUES ('{}','{}',{})""".format(str(x+1), out[lox]["id"], out[lox]["name"], out[lox]["count"])
                    c.execute(sql10)
                    conn.commit()
                
                elif str(webcount[0]) != str(out[lox]["count"]):
     
                    bot.send_message(chat_id, "Ещё одна уязвимость!\n\n_{}_ на `{}` .\n".format(out2[x][2], out[lox]["name"]), parse_mode= 'Markdown')
                    sql11 = """Update vuln{} set count = {} where website = '{}'""".format(str(x+1), out[lox]["count"], out[lox]["name"])
                    c.execute(sql11)
                    conn.commit()
               
            
                #print("From ACU: " + out[lox]["name"] + " " + str(out[lox]["count"]) + " ({})".format(out2[x][2]))
            
            except KeyError:
                print("LOL")
            
            #time.sleep(0.5)

    #current tv_id for website - out2[x][1]
    #current vlun name for website - out2[x][2]




def initdb():
    bot.send_message(chat_id, """Создаём струкруту БД...""")
    #sql2 = """SELECT * FROM count"""
    #yo = c.execute(sql2)
    #out2 = c.fetchall()

    for t in range(12):
        respo = requests.get(host + '/api/v1/vulnerability_groups', headers={'x-auth': api_key,}, params=(('q', 'vt_id:' + out2[t][1] + ';status:open'),), verify=False)
        out = respo.json()["items"]
    
    
        sql3 = """DROP TABLE IF EXISTS 'vuln{}'""".format(str(t+1))
        go = c.execute(sql3)
        conn.commit()
        
        sql8 = 'create table if not exists vuln' + str(t+1) + ' (id VARCHAR(64), website VARCHAR(255), count INT)'
        c.execute(sql8)
        conn.commit()
    
        for x in range(len(out)):

            sql = """insert into vuln{} (id, website, count) VALUES ('{}','{}',{})""".format(str(t+1), out[x]["id"], out[x]["name"], out[x]["count"])
            go = c.execute(sql)
            conn.commit()
    bot.send_message(chat_id, """Готово. Перезайдите в программу и выберите 'Y'.""")
    
    
    
x = input("Вы уже работали с этой программой? (Y/n) ")

looop = 0
if x == "Y" or x == "y":
    while True:
        main()
        print("loop + " + str(looop + 1)) 
        looop += 1
        time.sleep(recheck_sec)
elif x == "N" or x == "n":
    initdb()
    while True:
    
        main()
    
    
if __name__ == '__main__':
	bot.polling()