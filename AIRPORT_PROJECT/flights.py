# AI 종류: ChatGPT
# AI 사용 목적: 9팀 항공편 맞춤 공항 안내 프로그램의 설계 및 구현
# 사용한 AI 프롬프트: 이거 팀프로젝트 발표인데 8페이지에 나와있는 12주차 13주차 완성해야하는데 팀원을 역할 분담해서 각자 맡을 코드(파이썬으로만)를 주고 구현 까지 할 수 있는 코드를 짜주고 팀원(전재균,김기범,최민호,장태현)에게 각각 코드를 줘 그리고 우리 팀 깃허브의 커밋해서 통합하는 방법까지 알려줘
# AI 요청자: 장태현
# AI 사용 날짜: 2026-11-23

"""최민호 담당 — 항공편 데이터와 검색."""


class FlightInfo:
    def __init__(self, number, airline, destination, terminal, checkpoint,
                 wait_time, facilities):
        self.number = number
        self.airline = airline
        self.destination = destination
        self.terminal = terminal
        self.checkpoint = checkpoint
        self.wait_time = wait_time
        self.facilities = facilities


def load_sample_flights():
    """발표와 시연을 위한 샘플 데이터 목록을 만든다."""
    return [
        FlightInfo("KE123", "대한항공", "도쿄", "제2여객터미널",
                   "동편 보안검색대", 18,
                   ["한국전통문화센터", "면세구역 카페", "푸드코트"]),
        FlightInfo("OZ101", "아시아나항공", "오사카", "제1여객터미널",
                   "서편 보안검색대", 12, ["카페", "푸드코트"]),
        FlightInfo("7C201", "제주항공", "후쿠오카", "제1여객터미널",
                   "동편 보안검색대", 7, ["카페", "편의점"]),
        FlightInfo("LJ301", "진에어", "타이베이", "제2여객터미널",
                   "서편 보안검색대", 15, ["카페", "식당"]),
    ]


def find_flight(flights, number):
    """입력 양쪽의 공백을 없애고 대문자로 바꾼 뒤 목록에서 검색한다."""
    number = number.strip().upper()
    for flight in flights:
        if flight.number == number:
            return flight
    return None
