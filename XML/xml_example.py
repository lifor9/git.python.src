# coding=utf-8
#import xml.etree.ElementTree as etree
from lxml import etree

# Empty array
members = []
albums = []

# # 방법 1
# # Load XML
tree = etree.parse('sample01.xml')
root = tree.getroot()

# Get data
kids = root.getchildren()

for child in kids:
    if child.tag == "name":
        gname = child.text
    elif child.tag == "members":
        for x_member in child:
            members.append(x_member.text)
    elif child.tag == "albums":
        for x_album in child:
            albums.append([x_album.get("order"), x_album.text])

# Print
print("걸그룹 %s에 대한 정보는 다음과 같습니다:" % gname, end="\n\n")

print(" 멤버: ", end="")
for index, member in enumerate(members):
    if index > 0: print(", ", end="")
    print(member, end="")

print("\n\n [앨범 목록]")
for album in albums:
    print("  * %s: %s" % (album[0], album[1]))

# 방법 2
tree = etree.parse('sample02.xml')

#첫번째 user를 검색한 후 마침
user = tree.find('./user')

print(user.tag)  # tag name -> user
print(user.attrib)  # {'grade' : 'gold'}
print(user.get('grade'))  # attr value -> gold

userName = user.find('name')  # <name></name> tag
print(userName.text)  # Kim Cheol Soo

# 특정 attribute를 가진 태그 가져오는 방법
tree.find('./user[@grade]') #grade attrib을 가진 첫 번째 user
tree.find('./user[@grade][2]') #grade attrib을 가진 두 번째 user

# 특정 attrib의 특정 값을 가진 태그 가져오는 방법
tree.find('./user[@grade="diamond"]') #diamond 등급인 Kim Yoo Mee 태그

# 노드 XPath 표기법
# ./* #현재 노드의 하위 모든 태그
# ../ #부모 노드


# 태그 여러 개 한꺼번에 가져오기
for user in tree.findall('./user'):
    print(user.tag)

