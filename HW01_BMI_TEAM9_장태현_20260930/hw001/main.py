"""health.txt를 읽고 BMI 결과를 Turtle 표로 표시합니다."""
from pathlib import Path
import sys


def opinion(bmi):
    # 과제 예시의 수치/소견은 서로 맞지 않아 아래 기준을 명시하여 사용한다.
    if bmi < 18.5:
        return "저체중"
    if bmi < 23:
        return "정상"
    if bmi < 25:
        return "과체중"
    return "비만"


def read_health(path):
    people = []
    with path.open(encoding="utf-8-sig") as file:
        for number, line in enumerate(file, 1):
            parts = line.split()
            if not parts or parts[0] == "전화번호":
                continue
            if len(parts) != 4:
                raise ValueError(f"{number}번째 줄: 전화번호 이름 키 몸무게 순서로 입력하세요.")
            phone, name, height, weight = parts
            height, weight = float(height), float(weight)
            if height <= 0 or weight <= 0:
                raise ValueError(f"{number}번째 줄: 키와 몸무게는 양수여야 합니다.")
            bmi = weight / (height / 100) ** 2
            people.append([phone, name, f"{height:g}", f"{weight:g}",
                           f"{bmi:.2f}", opinion(bmi)])
    if not people:
        raise ValueError("health.txt에 팀원 정보를 입력하세요.")
    return people


def draw_table(people):
    import turtle
    screen = turtle.Screen()
    screen.title("TEAM9 BMI 프로그램")
    row_height = 55
    widths = [220, 130, 120, 140, 120, 130]
    total_width = sum(widths)
    total_height = row_height * (len(people) + 1)
    screen.setup(total_width + 80, total_height + 170)
    screen.tracer(0)
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    left, top = -total_width / 2, total_height / 2
    font = "AppleGothic" if sys.platform == "darwin" else "Malgun Gothic"

    def line(x1, y1, x2, y2):
        pen.penup()
        pen.goto(x1, y1)
        pen.pendown()
        pen.goto(x2, y2)
        pen.penup()

    pen.penup()
    pen.goto(0, top + 30)
    pen.write("TEAM9 팀원 BMI 결과", align="center", font=(font, 20, "bold"))
    x = left
    line(x, top, x, top - total_height)
    for width in widths:
        x += width
        line(x, top, x, top - total_height)
    for i in range(len(people) + 2):
        y = top - i * row_height
        line(left, y, left + total_width, y)
    rows = [["전화번호", "이름", "키(cm)", "몸무게(kg)", "BMI", "소견"]] + people
    for i, row in enumerate(rows):
        x = left
        for width, value in zip(widths, row):
            pen.goto(x + width / 2, top - i * row_height - 36)
            pen.write(value, align="center", font=(font, 13, "bold" if i == 0 else "normal"))
            x += width
    pen.goto(0, top - total_height - 35)
    pen.write("BMI = 몸무게(kg) ÷ 키(m)²", align="center", font=(font, 12, "normal"))
    screen.update()
    turtle.done()


def main():
    people = read_health(Path(__file__).with_name("health.txt"))
    for person in people:
        print(" | ".join(person))
    if "--check" not in sys.argv:
        draw_table(people)


if __name__ == "__main__":
    main()
