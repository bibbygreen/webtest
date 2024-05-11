import mysql.connector
# 連線資料庫
con=mysql.connector.connect(
    user="root",
    password="root",
    host="localhost",
    database="test"
)
test="new"
usernameInDB=[]
passwordInDB=[]
# 建立Cursor物件，用來對資料庫下指令

# cursor.execute("INSERT INTO member (name, username, password) VALUES ('test', 'test', 'test');") #執行SQL指令
# new_member=("kkkk", "jmnh", "oooo")
# cursor.execute(add_new_member, new_member)
cursor=con.cursor()
cursor.execute("SELECT * FROM member;")
data=cursor.fetchall()
con.commit() #確認執行
for row in data:
    usernameInDB.append(row[2])
    passwordInDB.append(row[3])

print(usernameInDB)
print(passwordInDB)

# add_new_member=("INSERT INTO member (name, username, password) VALUES (%s, %s, %s)")
# new_member=("newwww", test, "new123")
# if test not in username:
#     cursor.execute(add_new_member, new_member)
#     con.commit() #確認執行
#     # print("unique")
# else:
#     message = "該帳號已被註冊，請重新輸入"
#     # return RedirectResponse(url="/error?message=" + message, status_code=303)
    

con.close()

# productName="美式"
# productId="5"
# cursor.execute("UPDATE product SET name=%s WHERE id=%s", (productName, productId)) #只有一項 tuple的, 也不能省略