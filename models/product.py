from models.category import Category

class Product:
	def __init__(
		self,
		id: str,
		name: str,
		category: Category,
	):
		self._id = id
		self._name = name
		self._category = category

	@property
	def id(self):
		return self._id

	@property
	def name(self):
		return self._name

	@property
	def category(self):
		return self._category

	def __repr__(self) -> str:
		return f"{self._name} {self._category}"

	@staticmethod
	def from_json(json_product: dict):
		if json_product is None:
			return None
		json_product['category'] = Category.from_json(json_product.get('category'))
		return Product(**json_product)