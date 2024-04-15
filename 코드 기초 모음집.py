"""
기본적인 계산 연산자
+: 더하기
-: 빼기
*: 곱하기
/: 나누기(몫)
%: 나누기(나머지)
**:거듭제곱 ex) print(2 ** 3) = 8
"""

"""
변수명 = 변수값

변수명은 변수에 맞는 이름이나 자기가 지어주고 싶은 변수명 사용하면 됩니다.
변수값은 필요한 값을 넣어주거나 입력을 받게 할 수도 있다.

예시) 
n = 3

설명) "n"이라는 변수명을 가진 변수에 숫자 3을 넣음
여기서 변수값은 3이 된다.
"""

# a에 10을 넣어주는 코드
a = 10
# b에 3을 넣어주는 코드
b = 3

#a에 들어가 있는 값을 출력
print(a)

#b에 들어가 있는 값을 출력
print(b)

#현재 a에는 10 b에는 3이 들어가 있는 상태

#a 와 b를 더한 값을 출력하는 코드 a + b = ?
print(a + b)

#a에서 b를 뺀 값을 출력하는 코드 a - b = ?
print(a - b)

#a 와 b를 곱한 값을 출력하는 코드 a * b = ?
print(a * b)

#a 와 b를 나눈 몫을 출력하는 코드 a / b = ?
print(a / b)
print(a // b) # //두개를 쓰면 소수점을 버리고 정수만 (ex: 4.2가남으면 4만 결과값에 나옴)
#a 와 b를 나눈 후 나온 나머지을 출력하는 코드 a % b = ?
print(a % b)

"""
int : 정수.
str : 문자.
float : 실수.      문자앞에쓸떄 float()바꿀수있다
chr : 정수값 -> 문자.
ord : 문자 -> 정수값.
split : 나누다 구분하다. 
for : 반복문.
range : 범위. ex) for i in range()
while : 1을 붙이면 계속 반복.
break(if 으로 조건을 만들어 줘야함) 
if : 만약에.
elif : ~도 아니면.
else : 그 외. 
format : (수,".2f")원하는 자리(f) 까지 반올림. ex)format(변수이름:.2f)
map : 여러가지 데이터를 받아서 각각의 요소에 함수를 적용한 결과를 반환하는 내장함수.     map(int,input().split())
max : 정수 중 가장 큰수.할떄 안에들어갈꺼 정의필요
min : 정수 중 가장 작은수.
import : 다른 모듈(외부 라이브러리)의 기능을 현재 모듈에서 사용하기 위해 필요. 
rstrip : 문자열에서 오른쪽에 있는 연속된 모든 공백을 삭제한다.
f {}: {} 안에 변수나 표현식을 쉽게 삽일할 수 있도록 해준다.
list : 목록 작성에 쓰임
count : 몇개인지 갯수를 셀 때 사용
round :결과의값을 반올림할떄 사용 round(변수,반올림할값)".2f -> 해당값을 소수점 이하 둘쨰까지 표시하기위해 
len : 리스트의 길이를 구할 때 사용
del : 리스트 요소 삭제. x 번째 값을 삭제
append : 리스트 요소 추가. ,append(변수)
sort : 리스트 요소 순서대로 정렬. ex) a = [1, 4, 2, 3]. a.sort() => a = [1, 2, 3, 4] 
reverse : 현재 리스트를 역순으로 뒤집는다.
index : 리스트에 x 값이 있으면 위치 값을 돌려준다. ex) a = [1, 2, 3]. a.index(3) = 2 와 같이 index에 들어간 값이 몇번째에 있는지 나타냄
insert : 리스트에 요소 삽입. ex) a = [1, 2, 3]. a.insert(0, 4). a = [4, 1, 2, 3] 0의 자리에 4를 삽입하라는 뜻이다.
remove : 리스트에 나오는 첫 번째 x 값을 제거. 중복 값이 더 있으면 다시 remove를 입력해 삭제한다.
def : 함수를 하나 정의 해놓고 정의 된 함수를 호출해 쓴다. 자주 사용하는 코드를 함수로 묶어 사용(간결하게 됨, 수정 유지보수 편의) 
return : 지정된 변수값을 다시 가져온다.(retrun(넘겨줄 값))= 현재 함수의 실행을 종료하고 Return 우항 값을 함수 호출 쪽으로 반환한다.
output을 전달함. return을 만나면 계산 했다면 계산 값을 가지고 호출 됐던 항으로 돌아가 그대로 실행한다.
함수를 호출할때 집어 넣어주는 값 = 인자값
매개변수 : 입력받는 값을 저장하기 위함
isdigit : 문자열 반복하며 각문자가 숫자인지 확인
isupper : 문자열 반복하며 각문자가 대문자인지 확인
try: 예외가 발생하는 코드
except: try가 예외 발생했을떄의 실행코드
"""