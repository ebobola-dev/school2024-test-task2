
from config import *
from utils.json_util import JsonUtils
from models.order import Order
from functions import *

print()
try:
	source_orders_json = JsonUtils.read(SOURCE_DATA_FILEPATH)
except:
	print('Не удалось прочитать исходный файл с заказами')
	quit()

orders = tuple(Order.from_json(json_order) for json_order in source_orders_json)
print(f'Файл "{SOURCE_DATA_FILEPATH}" успешно прочитан, получено заказов: {len(orders)}')

new_year_eve_orders = get_new_year_eve_orders(orders)
if len(new_year_eve_orders) == 0:
	print('\nВ канун нового года ничего не заказывали..(')
	quit()
print(f'\nЗаказов в канун нового года: {len(new_year_eve_orders)}')

category_statistics = get_category_statistics(new_year_eve_orders)
print('\nСтатистика по категориям заказов:')
for key, value in category_statistics.items():
	print(f'\t{key} - {value} зз')

most_popular_categories = get_most_popular_categories(category_statistics)
print(f'\nНаиболее популярные категории: {', '.join(most_popular_categories)}')

JsonUtils.write('result.json', {'categories': most_popular_categories})
