from fastapi import FastAPI, Request, Form
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import HTMLResponse
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key="qwert54321")
app.mount("/static", StaticFiles(directory="static"))
templates = Jinja2Templates(directory="templates")

members = {
    "test": "test"
}

# Route to handle GET requests (rendering the form)
@app.get("/", response_class=HTMLResponse)
async def show_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/signin")
async def signin(request: Request, account: str = Form(None), password: str = Form(None)):
    if account in members and members[account] == password:
        request.session["SIGNED-IN"] = True
        return RedirectResponse(url='/member', status_code=303)
    elif not account or not password:
        message = "請輸入帳號密碼"
        return RedirectResponse(url="/error?message=" + message, status_code=303)
    else:
        message = "帳號、或密碼輸入有誤"
        return RedirectResponse(url="/error?message=" + message, status_code=303)
    
@app.get("/member", response_class=HTMLResponse)
async def member_page(request: Request):
    # Check if the user is signed in
    if "SIGNED-IN" not in request.session or not request.session["SIGNED-IN"]:
        # If not signed in, redirect to the home page
        return RedirectResponse(url='/', status_code=303)
    return templates.TemplateResponse(name="member.html", context={"request": request})

@app.get("/error", response_class=HTMLResponse)
async def error_page(request: Request):
    error = request.query_params.get("message", "")
    return templates.TemplateResponse(name="error.html", context={"request": request, "error": error})

@app.get("/signout", response_class=HTMLResponse)
async def signout(request: Request):
    request.session["SIGNED-IN"] = False
    return RedirectResponse(url='/')


@app.post("/square/", response_class=HTMLResponse)
async def calculate_square(request: Request):
    form_data = await request.form()
    number = int(form_data["number"])
    square_result = number ** 2
    return RedirectResponse(url=f"/square/{number}", status_code=303)
    
@app.get("/square/{number}", response_class=HTMLResponse)
async def show_square_result(request: Request, number: int):
    square_result = number ** 2
    return templates.TemplateResponse("square.html", {"request": request, "number": number, "square_result": square_result})
