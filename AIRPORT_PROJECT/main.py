# AI 종류: ChatGPT
# AI 사용 목적: 프로그램 실행 및 모듈 연결 코드 작성 도움
# 프롬프트: "공항 안내 프로그램을 4명 역할별로 나눠 코드를 작성해줘."
# 담당: 장태현
# AI 활용자: 실제 활용한 사람 이름 기입
# 날짜: 2026-11-17

import os
import tkinter as tk
from tkinter import messagebox

from storage import load_flights
from gui import FlightApp


def main():
    """데이터를 불러오고 프로그램 화면을 실행한다."""

    # main.py가 있는 폴더
    project_folder = os.path.dirname(
        os.path.abspath(__file__)
    )

    # 항공편 데이터 파일 위치
    flight_path = os.path.join(
        project_folder, "data", "flights.json"
    )

    # 조회 기록 파일 위치
    history_path = os.path.join(
        project_folder, "data", "history.json"
    )

    root = tk.Tk()
    root.withdraw()

    try:
        flights = load_flights(flight_path)

    except Exception as error:
        messagebox.showerror(
            "파일 오류",
            f"항공편 정보를 불러오지 못했습니다.\n{error}",
            parent=root
        )
        root.destroy()
        return

    app = FlightApp(root, flights, history_path)

    root.deiconify()
    root.mainloop()


if __name__ == "__main__":
    main()