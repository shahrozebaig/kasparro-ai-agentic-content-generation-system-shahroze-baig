from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from models.product_model import Product
from models.question_model import Question

class PipelineState(BaseModel):
    product: Optional[Product] = None
    product_b: Optional[Product] = None

    questions: List[Question] = Field(default_factory=list)
    faqs: List[Dict[str, str]] = Field(default_factory=list)

    product_page: Optional[Dict[str, Any]] = None
    comparison_page: Optional[Dict[str, Any]] = None

    logs: List[str] = Field(default_factory=list)
