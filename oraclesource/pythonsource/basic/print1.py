# print() 알아보기 - 화면 출력
# 옵션
#  1) sep : ,로 들어오는 출력문자들의 구분을 어떻게 할 것인가?
#  2) end : 줄바꿈을 하지 않고 다음 줄과 연결해서 출력

# java랑 다른 점 - 세미콜론(;) 사용 X

print("Hello Python!!") # 문자열 - 쌍따옴표, 홑따옴표 허용
print('Hello Python!!') # script랑 같은 개념
print(100)      # int (정수)
print("100")    # str (문자열)
print("25.3")
print(25)
print()
# type() : 변수 타입 확인
print(type(100))    # <class 'int'>
print(type("100"))  # <class 'str'>
print(type(25.5))   # <class 'float'>
print(type(True))   # <class 'bool'>
print()
print('T','E','S','T')  # T E S T
# 콤마(,)를 사용하면 기본적으로 한 칸을 띄우고 출력해준다.
print('T','E','S','T', sep='')  # TEST
# space bar 한 번이 default 인데 sep=''를 사용하면 붙여쓴다는 의미(?)
print('2022','05','19',sep='-') # 2022-05-19
# sep='-' 를 사용해서 문자열을 연결할 수 있다.
print("niceman","naver.com",sep='@')    # niceman@naver.com
print()
print("파이썬은 ",end=' ')
print("쉬운 언어입니다.")



