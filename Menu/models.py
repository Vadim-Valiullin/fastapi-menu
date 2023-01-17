from sqlalchemy import Column, INTEGER, String, TEXT, ForeignKey
from core.db import Base
from sqlalchemy.orm import relationship


class Menu(Base):
    __tablename__ = "Меню"

    id = Column(INTEGER, primary_key=True, index=True, unique=True)
    title = Column(String, unique=True)


class Submenu(Base):
    __tablename__ = "Подменю"

    id = Column(INTEGER, primary_key=True, index=True, unique=True)
    title = Column(String, unique=True)
    menu = Column(INTEGER, ForeignKey(Menu.id))
    menu_id = relationship("Menu")


class Dish(Base):
    __tablename__ = "БЛЮДА"

    id = Column(INTEGER, primary_key=True, index=True, unique=True)
    title = Column(String, unique=True)
    description = Column(TEXT)
    cooking_time = Column(INTEGER)
    price = Column(INTEGER)
    submenu = Column(INTEGER, ForeignKey(Submenu.id))
    submenu_id = relationship("Submenu")
