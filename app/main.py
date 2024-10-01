# import dependencies
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime



# create app instance
app = FastAPI()

# set location for templates
templates = Jinja2Templates(directory="app/view_templates")

# handle http get requests for the site root /
# return the index.html page
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
        return templates.TemplateResponse(request=request, name="index.html")

@app.get("/advice.html", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="advice.html")

@app.get("/params.html", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="params.html")

@app.get(".partials/dependencies.html", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="dependencies.html")

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static",
)

serverTime: datetime = datetime.now().strftime("%d/%m/%y %H:%M:%S")



