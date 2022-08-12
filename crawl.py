import requests
from bs4 import BeautifulSoup as bs

try:
    homepage = input("크롤링하고 싶은 홈페이지 주소 입력: ")
    req = requests.get(homepage)
    soup = bs(req.text)
    print("전체 출력========================")
    print(soup)
    print("텍스트만 출력=====================")
    print(soup.get_text())
    print("=================================")
    value = input("추출할 html 태그 입력: ")
    print("HTML 태그나 클래스로 특정 영역 출력=========")
    print(soup.find_all(value))
    print("===================")
except Exception as e:
    print("Error Message: ", e)
