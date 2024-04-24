from datetime import datetime

from models.product import Product

class Order:
	def __init__(
		self,
		ordered_at: datetime,
		items: tuple[Product],
	):
		self._ordered_at = ordered_at
		self._items = items

	@property
	def ordered_at(self):
		return self._ordered_at

	@property
	def items(self):
		return self._items

	def __repr__(self) -> str:
		return f"Заказ от {self.ordered_at.strftime('%d.%m.%Y %H:%M')}"

	@staticmethod
	def from_json(json_order: dict):
		if json_order is None:
			return None
		if not isinstance(json_order.get('items'), list):
			json_order['items'] = []
		else:
			json_order['items'] = tuple(Product.from_json(json_product) for json_product in json_order.get('items'))
		json_order['ordered_at'] = datetime.fromisoformat(json_order.get('ordered_at'))
		return Order(**json_order)