from fastapi import FastAPI, Request, Form
from starlette.middleware.sessions import SessionMiddleware
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import mysql.connector

# 連線資料庫
con=mysql.connector.connect(
    user="root",
    password="root",
    host="localhost",
    database="website"
)
cursor=con.cursor()
test="lion"
username="lion"
password="123qwe"
# 建立Cursor物件，用來對資料庫下指令

# cursor.execute("INSERT INTO member (name, username, password) VALUES ('test', 'test', 'test');") #執行SQL指令
# new_member=("kkkk", "jmnh", "oooo")
# cursor.execute(add_new_member, new_member)

# command = "SELECT * FROM member WHERE username = %s"
# new_username = (username, )
# cursor.execute(command, new_username)
# result=cursor.fetchall()
# con.commit() #確認執行

# print(result[0][1]) #name
# print(result[0][2]) #username
# print(result[0][3]) #password

cursor.execute("SELECT message.id, message.content, message.time, member.name FROM message JOIN member ON message.member_id = member.id ORDER BY message.time DESC")
select_from_db = cursor.fetchall()
con.commit()
messages_list = [{"message_id": row[0], "content": row[1], "time": row[2], "name": row[3]} for row in select_from_db]
print(messages_list)
# if not result:
#     print("yes")
# else:
#     print("no")
# add_new_member=("INSERT INTO member (name, username, password) VALUES (%s, %s, %s)")
# new_member=("newwww", test, "new123")
# if test not in username:
#     cursor.execute(add_new_member, new_member)
#     con.commit() #確認執行
    # print("unique")
# else:
#     message = "該帳號已被註冊，請重新輸入"
    # return RedirectResponse(url="/error?message=" + message, status_code=303)
    

con.close()

# productName="美式"
# productId="5"
# cursor.execute("UPDATE product SET name=%s WHERE id=%s", (productName, productId)) #只有一項 tuple的, 也不能省略