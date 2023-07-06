import orjson
from neomodel import config
from sanic import Sanic
from os import getenv
from dotenv import load_dotenv

from services.posts_service import posts_service
from services.users_service import users_service
from services.customers_service import customers_service
from services.stores_service import stores_service
from services.comments_service import comments_service
from services.chat_service import chat_service
from services.categories_service import categories_service
from services.locations_service import locations_service
from services.sales_service import sales_service
from services.delivery_service import delivery_service

load_dotenv()

config.DATABASE_URL = getenv("DATABASE_URL")

app = Sanic("App", dumps=orjson.dumps)

app.blueprint(posts_service)
app.blueprint(users_service)
app.blueprint(customers_service)
app.blueprint(stores_service)
app.blueprint(comments_service)
app.blueprint(chat_service)
app.blueprint(categories_service)
app.blueprint(locations_service)
app.blueprint(sales_service)
app.blueprint(delivery_service)
