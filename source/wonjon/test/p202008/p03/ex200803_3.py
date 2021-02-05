# 평균 구하기

dong = {'국어':80,'영어':75,'수학':55}

add = 0

for i in dong.values():
    add = add + i

avg = add/3
print(avg)

# 자연수 13이 홀수인지 짝수인지 판별
number = 13
flag = ""

if number % 2 == 0 : flag = "짝수"
else : flag = "홀수"

print(flag)

# 주민번호를 나눠서 출력
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:-1]
print(yyyymmdd)
print(num)


# 성별 나타내는 부분 출력
gender = pin[7:8]
print(gender)

# a:b:c:d -> a#b#c#d
a = "a:b:c:d"
b = a.replace(":","#")
print(b)

# [1,3,5,4,2] -> [5,4,3,2,1]
a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)

# ['Life', 'is', 'too', 'short'] -> 문자열
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)

# (1,2,3) 튜플 -> (1,2,3,4) 튜플
a = (1,2,3)
a = a + (4,)
print(a)

# 딕셔너리 a 오류의 경우와 그 이유 설명
# 3번 딕셔너리 키값에 변경될 수 있는 리스트는 들어갈 수 없다.
# 1 str, 2 튜플, 4 숫자

# B값 추출
a = {'A':90, 'B':80, 'C':70}
result = a['B']
print(a)
print(result)

# a리스트에서 중복 숫자 제거
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
b = list(aSet)
print(b)

# b[1]의 값도 4로 변한다
# 리스트형의 주소를 변수 a와 b가 동일하게 저장하기때문에, a[1]의 값을 바꿔도 b[1]도 바뀐다
a = b = [1,2,3]
a[1] = 4
print(b)