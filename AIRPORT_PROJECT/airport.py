import json
import os
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import urlopen

API_URL = (
    "https://apis.data.go.kr/B551177/statusOfDepartureCongestion/"
    "getDepartureCongestion"
)


def fetch_t1_queues():
    key = os.getenv("AIRPORT_API_KEY", "").strip()
    if not key:
        raise ValueError("AIRPORT_API_KEY 환경변수에 공공데이터포털 인증키를 설정하세요.")

    query = urlencode({
        "serviceKey": key,
        "terminalId": "P01",
        "pageNo": 1,
        "numOfRows": 50,
        "type": "json",
    })
    try:
        with urlopen(f"{API_URL}?{query}", timeout=8) as response:
            payload = json.load(response)
    except HTTPError as error:
        raise ValueError(
            f"공공데이터포털 응답 오류 (HTTP {error.code}). 요청 주소와 활용 승인을 확인하세요."
        ) from None
    except (URLError, TimeoutError):
        raise ValueError("공공데이터포털에 연결하지 못했습니다.") from None
    except (ValueError, UnicodeError):
        raise ValueError("JSON 응답을 받지 못했습니다. 인증키와 활용 승인을 확인하세요.") from None

    try:
        result = payload["response"]
        code = str(result["header"]["resultCode"])
        if code not in ("0", "00"):
            raise ValueError("공공데이터포털이 오류를 반환했습니다. 인증키와 활용 승인을 확인하세요.")
        items = result["body"].get("items") or []
        if isinstance(items, dict):
            items = items.get("item") or []
        if isinstance(items, dict):
            items = [items]

        rows = []
        for item in items:
            gate = item.get("gateId")
            count = str(item.get("waitLength", "")).strip()
            if gate and count.isdecimal():
                rows.append((str(gate), int(count)))
    except (KeyError, TypeError, AttributeError):
        raise ValueError("혼잡도 응답 형식이 예상과 다릅니다.") from None

    if not rows:
        raise ValueError("표시할 T1 대기 인원이 없습니다. API 응답 항목을 확인하세요.")
    return rows
