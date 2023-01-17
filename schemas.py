from pydantic import BaseModel, validator


class Menu(BaseModel):
    title: str


class Submenu(BaseModel):
    title: str
    menu: Menu


class Dish(BaseModel):
    title: str
    price: float
    cooking_time: int
    submenu: Submenu


    @validator('price')
    def price(cls, value):
        if 1500 < value < 55:
            raise ValueError('Цена должна быть в пределах от 55 до 1500 рублей')
        return value
