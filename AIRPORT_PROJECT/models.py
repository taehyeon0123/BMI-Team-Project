# AI 종류: ChatGPT
# AI 사용 목적: 항공편 데이터 클래스 작성 도움
# 프롬프트: "공항 안내 프로그램을 4명 역할별로 나눠 코드를 작성해줘."
# 담당: 최민호
# AI 활용자: 실제 활용한 사람 이름 기입
# 날짜: 2026-11-17


class FlightInfo:
    """항공편 한 개의 정보를 저장한다."""

    def __init__(self, number, airline, destination,
                 terminal, checkpoint, wait_time, facilities):

        # 문자 항목 검사
        text_values = [
            number, airline, destination,
            terminal, checkpoint
        ]

        for value in text_values:
            if not isinstance(value, str):
                raise ValueError("항공편의 문자 항목을 확인하세요.")

            if value.strip() == "":
                raise ValueError("항공편 정보에 빈 항목이 있습니다.")

        # 대기시간 검사
        if type(wait_time) is not int or wait_time < 0:
            raise ValueError("대기시간은 0 이상의 정수여야 합니다.")

        # 시설 목록 검사
        if not isinstance(facilities, list):
            raise ValueError("시설 정보는 리스트여야 합니다.")

        for facility in facilities:
            if not isinstance(facility, str):
                raise ValueError("시설 이름은 문자열이어야 합니다.")

            if facility.strip() == "":
                raise ValueError("시설 이름이 비어 있습니다.")

        self.number = number.strip().upper()
        self.airline = airline.strip()
        self.destination = destination.strip()
        self.terminal = terminal.strip()
        self.checkpoint = checkpoint.strip()
        self.wait_time = wait_time
        self.facilities = facilities

    def to_dict(self):
        """항공편 정보를 딕셔너리로 변환한다."""

        return {
            "number": self.number,
            "airline": self.airline,
            "destination": self.destination,
            "terminal": self.terminal,
            "checkpoint": self.checkpoint,
            "wait_time": self.wait_time,
            "facilities": self.facilities
        }