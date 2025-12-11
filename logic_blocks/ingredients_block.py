from typing import List
<<<<<<< HEAD
from models.product_model import Product

def generate_ingredients_copy(product: Product) -> List[str]:
    return product.key_ingredients or []
=======
from models import Product

def generate_ingredients_copy(product: Product) -> List[str]:
    return product.key_ingredients
>>>>>>> a45da5129a34f31c80f2a5e0334180f00f6b8dcd
