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

@app.get("/", response_class=HTMLResponse)
async def show_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/signup")
async def signup(request: Request, name: str = Form(None), username: str = Form(None), password: str = Form(None)):
    select_username_command = "SELECT * FROM member WHERE username = %s"
    new_username = (username, )
    cursor.execute(select_username_command, new_username)
    result=cursor.fetchall()
    if not result:
        add_new_member="INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
        new_member=(name, username, password)
        cursor.execute(add_new_member, new_member)
        con.commit() #確認執行
        return RedirectResponse(url='/', status_code=303)
    else:
        message = "該帳號已被註冊，請重新輸入"
        return RedirectResponse(url="/error?message=" + message, status_code=303)
    
@app.post("/signin")
async def signin(request: Request, username: str = Form(None), password: str = Form(None)):
    if not username or not password:
        message = "請輸入帳號或密碼"
        return RedirectResponse(url="/error?message=" + message, status_code=303)
    select_username_command = "SELECT * FROM member WHERE username = %s"
    check_member = (username, )
    cursor.execute(select_username_command, check_member)
    result=cursor.fetchall()
    if username == result[0][2]: 
        if password == result[0][3]:
            request.session["SIGNED-IN"] = True
            request.session["MEMBER_ID"] = result[0][0]
            request.session["NAME"] = result[0][1]
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
    if not request.session.get("SIGNED-IN"):
        return RedirectResponse(url='/', status_code=303)
    username = request.session.get("USERNAME")
    name = request.session.get("NAME")
    cursor.execute("SELECT message.id, message.content, message.time, member.name FROM message JOIN member ON message.member_id = member.id ORDER BY message.time DESC")
    select_from_db = cursor.fetchall()
    messages_list = [{"message_id": row[0], "content": row[1], "time": row[2], "name": row[3]} for row in select_from_db]
    return templates.TemplateResponse(name="member.html", context={"request": request, "name": name, "messages_list": messages_list})

@app.get("/error", response_class=HTMLResponse)
async def error_page(request: Request):
    if not request.session.get("SIGNED-IN"):
        return RedirectResponse(url='/', status_code=303) 
    error = request.query_params.get("message", "")
    return templates.TemplateResponse(name="error.html", context={"request": request, "error": error})

@app.get("/signout", response_class=HTMLResponse)
async def signout(request: Request):
    request.session.clear()
    return RedirectResponse(url='/')

@app.post("/createMessage", response_class=HTMLResponse)
async def createMessage(request: Request, content: str = Form(None)):
    if not request.session.get("SIGNED-IN"):
        return RedirectResponse(url='/', status_code=303)  
    member_id = request.session.get("MEMBER_ID")
    cursor = con.cursor()
    add_new_message="INSERT INTO message (member_id, content) VALUES (%s, %s)"
    new_message=(member_id, content)
    cursor.execute(add_new_message,new_message)
    con.commit() #確認執行
    return RedirectResponse(url='/member', status_code=303)
