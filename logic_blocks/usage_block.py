from models import Product

def generate_usage_copy(product: Product) -> str:
    return product.how_to_use
