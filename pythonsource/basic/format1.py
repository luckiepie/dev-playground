# format()
# ~~.printf("%d", 3) 와 같은 개념
# %c - 문자 하나, %f = 실수, %d - 정수, %s - 문자(만능)

print('%d' % 100)   # 있는 그대로 출력
print('%5d' % 100)  # 5자리에 맞춰서 출력 (숫자라서 오른쪽 정렬에 맞춰서 출력)
print('%05d' % 100) # 비어있는 자리에 0으로 채워서 출력
print()
print("%s" % "hi")  # 좌측 정렬 출력
print("%5s" % "hi") # 우측 정렬 출력
print()
print("%8.2f" % 12.21)  # .2f 의 의미 : 소숫점 2번째 자리 까지만 출력
print("%-8.2f" % 12.21) # 그냥 주면 오른쪽 정렬. -f를 주면 왼쪽 정렬
print("%-8.2f" % 12.213456434254)
# 중간에 %로 들어와야 한다.
print()
print("I eat %d apples" % 3)    # 공간만 잡아놓고 끼워넣는 방식이 더 편하다(?)
print("I eat %s apples" % 3)    # %s 는 정수, 실수 다 받는다(?)
number = 4
print("I eat %s apples" % number)
print("I eat", number, "apples")
print()
print("%d : %s" % (1, "홍길동"))
print("%d : %s - %f" % (2, "신짱구", 93.2))
print("Test1 : %5d Price : %4.2f" %(776, 5634.123))
# 2개 이상부터는 괄호()를 사용해서 묶어줘야 한다.
print()
# %s의 만능
print("I eat %rs apples" % 3)
print("I eat %rs apples" % 3.126)
print("I eat %rs apples" % "3")
print()
print("Error is %d%%" % 98)
# %라는 문자를 출력하고 싶을 때에는 %를 2번 쓴다. 한 번만 사용하면 에러 발생.


