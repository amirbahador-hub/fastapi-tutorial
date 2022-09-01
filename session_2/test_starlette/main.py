from starlette.applications import Starlette
from starlette.routing import Route
from starlette.requests import Request
from starlette.responses import JSONResponse


async def index(request: Request):
    return JSONResponse(content={"ok": True})


routes=[
        Route("/", endpoint=index)
        ]


app = Starlette(
        debug=True,
        routes=routes
        )


