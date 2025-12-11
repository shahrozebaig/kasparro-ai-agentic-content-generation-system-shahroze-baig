from typing import List
from models.product_model import Product

def generate_benefits_copy(product: Product) -> List[str]:
    lines = []
    for benefit in product.benefits:
        skin = ", ".join(product.skin_type) if product.skin_type else "all"
        line = f"{benefit} for {skin} skin types"
        lines.append(line)
    return lines
