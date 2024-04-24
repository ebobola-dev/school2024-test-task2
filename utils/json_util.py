import json

class JsonUtils:
	@staticmethod
	def read(filepath: str):
		with open(filepath, "r", encoding='utf-8') as json_file:
			return json.load(json_file)

	@staticmethod
	def write(filepath: str, data: dict):
		with open(filepath, "w", encoding='utf-8') as json_file:
			return json.dump(data, json_file, indent=4, ensure_ascii=False)

