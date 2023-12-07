from sqlalchemy import create_engine, Column, Integer, String, Date 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from config import DATABASE
DATABASE_URL = DATABASE['database_manegment'] + '://' + DATABASE['user'] + ':' + DATABASE['password'] + '@'+ DATABASE['host']+'/'+ DATABASE['database']
print(DATABASE_URL)
engine = create_engine(DATABASE_URL)
Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Item(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key = True, autoincrement= True) 
    title = Column(String) 
    author = Column(String) 
    genre = Column(String) 
    created_at = Column(Date)

Base.metadata.create_all(bind = engine)

ItemPydentic = sqlalchemy_to_pydantic(Item, exclude=['id'])

def create_item(data):
    with Sessionlocal() as db:
        data = ItemPydentic(**data)
        data = Item(**data.dict())
        db.add(data)
        db.commit()
        db.refresh(data)
    return data

def get_item():
    data = []
    with Sessionlocal() as db:
        items = db.query(Item).all()
        for item in items:
            data.append({
                'title': item.title,
                'author': item.author,
                'genre': item.genre,
                'created_at': str(item.created_at)
            })
    return data

def retrieve(item_id):
    with Sessionlocal() as db:
        data = db.get(Item, item_id)
        if data:
            return {'title': data.title,
                'author': data.author,
                'genre': data.genre,
                'created_at': str(data.created_at)
                }


def update_item(item_id, changes):
    with Sessionlocal() as db:
        changes = ItemPydentic(**changes)
        data = db.get(Item, item_id)
        if data:
            for field, value in changes.dict().items():
                setattr(data, field, value)
            db.commit()
            db.refresh(data)
            return 'Успешно изменено'
        
        return 'Неверный ID'

def delete_item(item_id):
    with Sessionlocal() as db:
        drop = db.get(Item, item_id)
        db.delete(drop)
        db.commit()

# create_item({"title":"Evgeniy Onegin", "author": "Turgenev", "genre": "drama"})
# update_item(1, {"created_at": "1800-04-10"})
# print(get_item())