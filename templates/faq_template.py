from typing import List, Dict, Any
from models.product_model import Product

def build_faq_page(product: Product, faqs: List[Dict[str, str]]) -> Dict[str, Any]:
    page = {
        "page_type": "faq",
        "product_name": product.product_name,
        "faqs": faqs,
    }
    return page
