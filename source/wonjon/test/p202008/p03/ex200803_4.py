import random

# 자동차 1명 당첨자
car = 0
# 자동차 1명 당첨자 추출
car = random.randrange(1,101)
# 냉장고 5명 당첨자 보관 리스트
winner = []

while True:
    temp = random.randrange(1, 101)

    # 냉장고 당첨자 총 5명 나오면 종료
    if len(winner) == 5:
        break

    # 신규 냉장고 당첨자가 기존 자동차 당첨자와 중복 나오면 다시 돌리기
    if car == temp:
        continue

    # 신규 냉장고 당첨자가 기존 냉장고 당첨자와 중복 나오면 다시 돌리기
    for i in winner:
        if i == temp:
            continue

    # 중복 안되는 신규 냉장고 당첨자 명단 추가
    winner.append(temp)
# 냉장고 당첨자 순서 정렬
winner.sort()

# 자동차 당첨자 출력
print(car)
# 냉장고 당첨자 출력
print(winner)

# pass와 continue를 혼동하여 사용.
# continue로 바꿔서 중복 당첨자 목록 제외

