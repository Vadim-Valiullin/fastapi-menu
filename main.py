from fastapi import FastAPI, Query, Path, Body
from schemas import *


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post('/dish', response_model=Dish)
def create_dish(item: Dish, submenu: Submenu, menu: Menu):
    return {'item': item, 'submenu': submenu, 'menu': menu}


@app.post('/submenu')
def create_submenu(submenu: Submenu = Body(..., embed=True)):
    return {'submenu': submenu}


@app.get('/dish')
def get_dishes(q: list[str] = Query(..., description='Выбор блюда')):
    return q


@app.get('/dish/{pk}')
def get_dish(pk: int = Path(..., gt=1), price: int = Query(None, gt=50, le=1500)):
    return {'dish': pk, 'price': price}
