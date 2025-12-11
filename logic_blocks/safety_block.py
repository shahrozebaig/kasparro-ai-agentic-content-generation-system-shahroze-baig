from models.product_model import Product

def generate_safety_copy(product: Product) -> str:
    parts = []
    if product.side_effects:
        parts.append(product.side_effects)
    parts.append("Perform a patch test before full use, especially if you have sensitive skin.")
    return " ".join(parts).strip()
