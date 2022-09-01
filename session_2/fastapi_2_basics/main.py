from fastapi import FastAPI, Request, Response, status, HTTPException
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from pydantic import BaseModel



app = FastAPI()
templates = Jinja2Templates("templates")
favicon_path = 'favicon.ico'


class Post(BaseModel):
    title: str
    content: str
    published: bool = True


while True:
    try:
        db_info = {
            "host":"localhost",
            "database":"fastapi_test_db",
            "user":"fastapi_test_user",
            "password":"fastapi_test_password",
            "cursor_factory":RealDictCursor
            }
        conn = psycopg2.connect(**db_info)
        cursor = conn.cursor()
        print("Database Connected")
        break
    except Exception as error:
        print("Conneting to database faild")
        print("Error :", error)
        time.sleep(2)

@app.get("/hello")
async def greeting(request:Request, name:str):
    return templates.TemplateResponse("index.html", 
            {"request": request, "name": name})

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute(""" INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING
            * """,
                (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()

    return {"data": new_post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_posts(id: int):
    cursor.execute(""" DELETE FROM posts WHERE id = %s RETURNING
            * """,
                (str(id),))
    deleted_post = cursor.fetchone()
    conn.commit()

    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail=f"post with id: {id} was not found"
                )


    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    return posts

@app.get("/posts/{id}")
def get_post(id: int):
    cursor.execute("""SELECT * from posts WHERE id = %s """,(str(id)))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail=f"post with id: {id} was not found"
                )
    return {"post_detail": post}
