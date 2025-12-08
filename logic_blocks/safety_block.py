from models import Product

def generate_safety_copy(product: Product) -> str:
    if product.side_effects:
        return (
            f"{product.side_effects}. Patch test before first use if your skin is sensitive."
        )
    return ""
