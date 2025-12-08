from typing import Dict, Any
from models import Product

def generate_comparison(product_a: Product, product_b: Product) -> Dict[str, Any]:
    comparison = {
        "price": {
            product_a.product_name: {
                "value": product_a.price,
                "currency": product_a.currency,
            },
            product_b.product_name: {
                "value": product_b.price,
                "currency": product_b.currency,
            },
        },
        "concentration": {
            product_a.product_name: product_a.concentration,
            product_b.product_name: product_b.concentration,
        },
        "skin_type": {
            product_a.product_name: product_a.skin_type,
            product_b.product_name: product_b.skin_type,
        },
        "key_ingredients": {
            product_a.product_name: product_a.key_ingredients,
            product_b.product_name: product_b.key_ingredients,
        },
        "benefits": {
            product_a.product_name: product_a.benefits,
            product_b.product_name: product_b.benefits,
        },
    }
    return comparison
