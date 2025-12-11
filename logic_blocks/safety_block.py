<<<<<<< HEAD
from models.product_model import Product

def generate_safety_copy(product: Product) -> str:
    parts = []
    if product.side_effects:
        parts.append(product.side_effects)
    parts.append("Perform a patch test before full use, especially if you have sensitive skin.")
    return " ".join(parts).strip()
=======
from models import Product

def generate_safety_copy(product: Product) -> str:
    if product.side_effects:
        return (
            f"{product.side_effects}. Patch test before first use if your skin is sensitive."
        )
    return ""
>>>>>>> a45da5129a34f31c80f2a5e0334180f00f6b8dcd
