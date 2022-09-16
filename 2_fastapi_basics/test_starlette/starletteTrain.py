from starlette.requests import Request
from starlette.responses import JSONResponse, PlainTextResponse, Response
from starlette.routing import Route, Mount, WebSocketRoute
from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles


async def home(request: Request):
    return PlainTextResponse("hello world")


async def user(request: Request):
    return JSONResponse({"fname": "ali", "lname": "qasemi"})


async def getName(request: Request):
    return JSONResponse({"name": request.path_params})


async def webSockerEndPoint(websocket):
    await websocket.accept()
    await websocket.send_text('Hello, websocket!')
    await websocket.close()


async def apps(scope, receive, send):
    assert scope['type'] == 'http'
    request = Request(scope, receive)
    content = '%s %s' % (request.method, request.url.path)
    response = Response(content, media_type='text/plain')
    await response(scope, receive, send)


routes = [
    Route("/", home),
    Route("/user/info", user),
    Route("/user/get", getName),
    WebSocketRoute("/ws", webSockerEndPoint),
    Mount("/static", StaticFiles(directory="static"))
]

app = Starlette(debug=True, routes=routes)
