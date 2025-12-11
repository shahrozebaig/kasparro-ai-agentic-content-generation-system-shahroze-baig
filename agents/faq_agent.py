import json
from models.state_model import PipelineState
from utils.llm_client import llm_generate
from config import settings

PROMPT = """
You are an expert skincare assistant. Given a product JSON and a user question, provide a concise, accurate answer.
Return plain text or JSON. Product: {product}
Question: {question}
"""

class FAQAgent:
    def run(self, state: PipelineState) -> PipelineState:
        if not state.product:
            raise RuntimeError("No product in state")
        faqs = []
        limit = settings.faq_limit
        for q in state.questions:
            if len(faqs) >= limit:
                break
            prompt = PROMPT.format(product=state.product.json(), question=q.text)
            try:
                ans = llm_generate(prompt, max_tokens=250)
                try:
                    parsed = json.loads(ans)
                    answer = parsed.get("answer") or parsed.get("response") or ans
                except Exception:
                    answer = ans
            except Exception:
                answer = "Sorry, unable to generate answer at this time."
            faqs.append({"question": q.text, "answer": answer})
        state.faqs = faqs
        state.logs.append(f"FAQAgent: generated {len(faqs)} faqs")
        return state
