from typing import Any, Dict
from models import Product

class ParserAgent:
    def run(self, raw_data: Dict[str, Any]) -> Product:
        product = Product.from_dict(raw_data)
        return product
