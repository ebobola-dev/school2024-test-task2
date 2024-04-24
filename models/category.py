class Category:
	def __init__(
		self,
		id: str,
		name: str
	):
		self._id = id
		self._name = name

	@property
	def id(self):
		return self._id

	@property
	def name(self):
		return self._name

	def __repr__(self) -> str:
		return f"[{self._name}]"

	@staticmethod
	def from_json(json_category: dict):
		if json_category is None:
			return None
		return Category(**json_category)