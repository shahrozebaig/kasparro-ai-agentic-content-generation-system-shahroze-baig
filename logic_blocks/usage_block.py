<<<<<<< HEAD
from models.product_model import Product

def generate_usage_copy(product: Product) -> str:
    return product.how_to_use or ""
=======
from models import Product

def generate_usage_copy(product: Product) -> str:
    return product.how_to_use
>>>>>>> a45da5129a34f31c80f2a5e0334180f00f6b8dcd
