from typing import List
from models import Product

def generate_ingredients_copy(product: Product) -> List[str]:
    return product.key_ingredients
