from fastapi import FastAPI, Request, Form
from starlette.middleware.sessions import SessionMiddleware
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import mysql.connector

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="qwert54321")
app.mount("/static", StaticFiles(directory="static"))
templates = Jinja2Templates(directory="templates")

# 連線資料庫

con=mysql.connector.connect(
    user="root",
    password="root",
    host="localhost",
    database="website"
)
cursor=con.cursor()

usernameInDB=[]
passwordInDB=[]
memberidInDB=[]
nameInDB=[]
cursor.execute("SELECT * FROM member;")
data=cursor.fetchall()
con.commit() #確認執行
for row in data:
    memberidInDB.append(row[0])
    nameInDB.append(row[1])
    usernameInDB.append(row[2])
    passwordInDB.append(row[3])


@app.get("/", response_class=HTMLResponse)
async def show_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/signup")
async def signup(request: Request, name: str = Form(None), username: str = Form(None), password: str = Form(None)):
    if username not in usernameInDB:
        add_new_member="INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
        new_member=(name, username, password)
        cursor.execute(add_new_member, new_member)
        con.commit() #確認執行
        # Update lists with new member information
        cursor.execute("SELECT * FROM member WHERE username = %s", (username,))
        new_member_data = cursor.fetchone()
        memberidInDB.append(new_member_data[0])
        nameInDB.append(new_member_data[1])
        usernameInDB.append(new_member_data[2])
        passwordInDB.append(new_member_data[3])
        return RedirectResponse(url='/', status_code=303)
    else:
        message = "該帳號已被註冊，請重新輸入"
        return RedirectResponse(url="/error?message=" + message, status_code=303)
    
@app.post("/signin")
async def signin(request: Request, username: str = Form(None), password: str = Form(None)):
    if not username or not password:
        message = "請輸入帳號或密碼"
        return RedirectResponse(url="/error?message=" + message, status_code=303)
    if username in usernameInDB:
        index = usernameInDB.index(username)
        if password == passwordInDB[index]:
            member_id = memberidInDB[index]
            request.session["SIGNED-IN"] = True
            request.session["MEMBER_ID"] = member_id
            request.session["USERNAME"] = username
            return RedirectResponse(url='/member', status_code=303)
        else:
            message = "密碼輸入有誤"
            return RedirectResponse(url="/error?message=" + message, status_code=303)
    else:
        message = "帳號不存在，請重新註冊"
        return RedirectResponse(url="/error?message=" + message, status_code=303)
       
@app.get("/member", response_class=HTMLResponse)
async def member_page(request: Request):
    # Check if the user is signed in
    if "SIGNED-IN" not in request.session or not request.session["SIGNED-IN"]:
        return RedirectResponse(url='/', status_code=303)

    username = request.session.get("USERNAME")
    index = usernameInDB.index(username)
    name = nameInDB[index]
    cursor.execute("SELECT message.id, message.content, message.time, member.name FROM message JOIN member ON message.member_id = member.id ORDER BY message.time DESC")
    select_from_db = cursor.fetchall()
    con.commit()
    messages_list = [{"message_id": row[0], "content": row[1], "time": row[2], "name": row[3]} for row in select_from_db]
    return templates.TemplateResponse(name="member.html", context={"request": request, "name": name, "messages_list": messages_list})

@app.get("/error", response_class=HTMLResponse)
async def error_page(request: Request):
    error = request.query_params.get("message", "")
    return templates.TemplateResponse(name="error.html", context={"request": request, "error": error})

@app.get("/signout", response_class=HTMLResponse)
async def signout(request: Request):
    request.session["SIGNED-IN"] = False
    return RedirectResponse(url='/')

@app.post("/createMessage", response_class=HTMLResponse)
async def createMessage(request: Request, content: str = Form(None)):
    if "MEMBER_ID" not in request.session:
        return RedirectResponse(url='/', status_code=303)
    
    member_id = request.session["MEMBER_ID"]

    cursor = con.cursor()
    add_new_message="INSERT INTO message (member_id, content) VALUES (%s, %s)"
    new_message=(member_id, content)
    cursor.execute(add_new_message,new_message)
    con.commit() #確認執行

    return RedirectResponse(url='/member', status_code=303)

