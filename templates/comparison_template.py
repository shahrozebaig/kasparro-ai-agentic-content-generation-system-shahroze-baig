from typing import Dict, Any
<<<<<<< HEAD
from models.product_model import Product
=======
from models import Product
>>>>>>> a45da5129a34f31c80f2a5e0334180f00f6b8dcd

def build_comparison_page(
    product_a: Product,
    product_b: Product,
    comparison_data: Dict[str, Any],
) -> Dict[str, Any]:
    page = {
        "page_type": "comparison",
        "product_a": {
            "product_name": product_a.product_name,
            "concentration": product_a.concentration,
            "skin_type": product_a.skin_type,
            "key_ingredients": product_a.key_ingredients,
            "benefits": product_a.benefits,
            "price": {
                "value": product_a.price,
                "currency": product_a.currency,
            },
        },
        "product_b": {
<<<<<<< HEAD
            "product_name": product_b.get("product_name") if isinstance(product_b, dict) else product_b.product_name,
            "concentration": product_b.get("concentration") if isinstance(product_b, dict) else product_b.concentration,
            "skin_type": product_b.get("skin_type") if isinstance(product_b, dict) else product_b.skin_type,
            "key_ingredients": product_b.get("key_ingredients") if isinstance(product_b, dict) else product_b.key_ingredients,
            "benefits": product_b.get("benefits") if isinstance(product_b, dict) else product_b.benefits,
            "price": {
                "value": product_b.get("price") if isinstance(product_b, dict) else product_b.price,
                "currency": product_b.get("currency") if isinstance(product_b, dict) else product_b.currency,
=======
            "product_name": product_b.product_name,
            "concentration": product_b.concentration,
            "skin_type": product_b.skin_type,
            "key_ingredients": product_b.key_ingredients,
            "benefits": product_b.benefits,
            "price": {
                "value": product_b.price,
                "currency": product_b.currency,
>>>>>>> a45da5129a34f31c80f2a5e0334180f00f6b8dcd
            },
        },
        "comparison": comparison_data,
    }
    return page
