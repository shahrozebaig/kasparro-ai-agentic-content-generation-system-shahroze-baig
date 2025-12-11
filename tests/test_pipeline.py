from orchestrator import Orchestrator
import os

def test_run_creates_outputs(tmp_path):
    o = Orchestrator()
    o.outputs = str(tmp_path)
    o.run()
    assert os.path.exists(os.path.join(o.outputs, "faq.json"))
    assert os.path.exists(os.path.join(o.outputs, "product_page.json"))
    assert os.path.exists(os.path.join(o.outputs, "comparison_page.json"))
    assert os.path.exists(os.path.join(o.outputs, "run_logs.json"))
