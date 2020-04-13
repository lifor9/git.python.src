# coding=utf-8
import requests
from bs4 import BeautifulSoup

resp = requests.get('https://www.naver.com/')
soup = BeautifulSoup(resp.text, 'html.parser')
titles = soup.select('.ah_roll .ah_k')  # 타이틀(제목)을 가지고 있는 클래스 명

for title in titles:
    print(title.get_text())

# for i, title in enumerate(titles, 1):
#     print(f'{i}위 {title.get_text()}')

# hotkeywords = soup.select('.ah_list .ah_item') # 제목과 순위 그리고 링크 주소 까지 가져오기
#
# for hotkey in hotkeywords:
#     print(f'{hotkey.select_one(".ah_r").get_text()}위 '
#           f'{hotkey.select_one(".ah_k").get_text()} '
#           f'{hotkey.select_one(".ah_a").get("href")}')

