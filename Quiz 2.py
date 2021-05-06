# Quiz 당신은 최근에 코딩 스터디 모임을 새로 만들엇.
# 월 4회 스터디, 3 번 온랑니, 1번 오프라인
# 오프라인 모임 날짜 정해주는 프로그램 작성

# 1: 랜덤 날짜
# 2: 월별 날짜는 다름을 감안하여 최소 일수인 28일 이내로 정함
# 3: 매우러 1~3일은 스터디 준비를 해야하므로 제외

# 출력문 예제
# 오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다.

# Answer )
from random import *

date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다.")