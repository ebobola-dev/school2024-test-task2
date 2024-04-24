
from config import *
from utils.json_util import JsonUtils
from models.order import Order
from functions import *

try:
	source_orders_json = JsonUtils.read(SOURCE_DATA_FILEPATH)
except:
	print('Не удалось прочитать исходный файл с заказами')
	quit()

orders = tuple(Order.from_json(json_order) for json_order in source_orders_json)

print()