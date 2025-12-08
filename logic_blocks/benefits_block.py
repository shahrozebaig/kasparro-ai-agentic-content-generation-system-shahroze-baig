from typing import List
from models import Product

def generate_benefits_copy(product: Product) -> List[str]:
    lines = []
    for benefit in product.benefits:
        line = f"{benefit} for {', '.join(product.skin_type)} skin types"
        lines.append(line)
    return lines
