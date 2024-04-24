from models.order import Order

def get_new_year_eve_orders(orders: tuple[Order]) -> tuple[Order]:
	return tuple(filter(lambda order: order.ordered_at.month == 12, orders))

def get_category_statistics(orders: tuple[Order]) -> dict:
	categories = {}
	for order in orders:
		for product in order.items:
			if product.category.name in categories:
				categories[product.category.name] += 1
			else:
				categories[product.category.name] = 1
	return categories

def get_most_popular_categories(category_statistics: dict) -> tuple[str]:
	max_category_usage = max(category_statistics.values())

	most_popular_categories = tuple(sorted(category[0] for category in filter(lambda category_statistic: category_statistic[1] == max_category_usage, category_statistics.items())))
	"""
				↑↑↑
	most_popular_categories = []
	for key, value in category_statistics.items():
		if value == max_category_usage:
			most_popular_categories.append(key)

	most_popular_categories = sorted(most_popular_categories)
	most_popular_categories = tuple(most_popular_categories)
	"""

	return most_popular_categories
