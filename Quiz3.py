"""Quiz 사이트 별로 비번 만들어주는 프로그램

ex) http://naver.com
1: http:// 부분은 제외 => naver.com
2: 처음 만나는 점(.) 이후 부분은 제외 => naver
3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 +"!" 로 구성
                (nav)               (5)         (1)     (!)
ex) 생성된 비밀번호 : nav51!
"""

url = "http://idkhowtopython.com"
my_str = url.replace("http://", "")  # 1
print(my_str)
my_str = my_str[:my_str.index(".")]  # 2
print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다.".format(url, password))
