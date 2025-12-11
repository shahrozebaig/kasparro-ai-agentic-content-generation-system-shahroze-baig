from typing import List
<<<<<<< HEAD
from models.product_model import Product
=======
from models import Product
>>>>>>> a45da5129a34f31c80f2a5e0334180f00f6b8dcd

def generate_benefits_copy(product: Product) -> List[str]:
    lines = []
    for benefit in product.benefits:
<<<<<<< HEAD
        skin = ", ".join(product.skin_type) if product.skin_type else "all"
        line = f"{benefit} for {skin} skin types"
=======
        line = f"{benefit} for {', '.join(product.skin_type)} skin types"
>>>>>>> a45da5129a34f31c80f2a5e0334180f00f6b8dcd
        lines.append(line)
    return lines
