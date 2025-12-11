from typing import List, Dict, Any
<<<<<<< HEAD
from models.product_model import Product
=======
from models import Product
>>>>>>> a45da5129a34f31c80f2a5e0334180f00f6b8dcd

def build_faq_page(product: Product, faqs: List[Dict[str, str]]) -> Dict[str, Any]:
    page = {
        "page_type": "faq",
        "product_name": product.product_name,
        "faqs": faqs,
    }
    return page
