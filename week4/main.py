from fastapi import FastAPI, Request, Form, Path
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import HTMLResponse
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from urllib.parse import urlencode

app = FastAPI()

# Configure middleware
middleware = [
    Middleware(SessionMiddleware, secret_key="your_secret_key")
]

# Attach middleware to the application
app.add_middleware(SessionMiddleware, secret_key="your_secret_key")

app.mount("/static", StaticFiles(directory="static"))
templates = Jinja2Templates(directory="templates")

members = {
    "test": "test"
}

# Route to handle GET requests (rendering the form)
@app.get("/", response_class=HTMLResponse)
async def show_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Route to handle GET requests for the member page
@app.get("/member", response_class=HTMLResponse)
async def show_member_page(request: Request):
    # Check if the user is signed in
    if "SIGNED-IN" not in request.session or not request.session["SIGNED-IN"]:
        # If not signed in, redirect to the home page
        return RedirectResponse(url='/', status_code=303)
    return templates.TemplateResponse("member.html", {"request": request})

@app.get("/logout", response_class=HTMLResponse)
async def logout(request: Request):
    request.session["SIGNED-IN"] = False
    return RedirectResponse(url='/', status_code=303)

@app.get("/error", response_class=HTMLResponse)
async def show_error_page(request: Request, error: str):
    return templates.TemplateResponse("error.html", {"request": request, "error": error})

@app.post("/signin", response_class=HTMLResponse)
async def signins(request: Request, account: str = Form(None), password: str = Form(None)):
    if account in members and members[account] == password:
        request.session["SIGNED-IN"] = True
        return RedirectResponse(url='/member', status_code=303)
    elif not account or not password:
        error_message = "請輸入帳號或密碼"
    else:
        error_message = "帳號、密碼輸入錯誤"

    query_params = {"error": error_message}
    query_string = urlencode(query_params)
    redirect_url = f'/error?{query_string}'
    return RedirectResponse(url=redirect_url, status_code=303)

@app.post("/square/", response_class=HTMLResponse)
async def calculate_square(request: Request):
    form_data = await request.form()
    number = int(form_data["number"])
    square_result = number ** 2
    return templates.TemplateResponse("square.html", {"request": request, "number": number, "square_result": square_result})

# @app.post("/square/{number}", response_class=HTMLResponse)
# async def calculate_square(request: Request, number: int = Path(...)):
#     square_result = number ** 2
#     return templates.TemplateResponse("square.html", {"request": request, "number": number, "square_result": square_result})    