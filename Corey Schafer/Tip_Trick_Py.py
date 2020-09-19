"1 Dùng if theo cách khác"
# condition = True
# if condition:
#     x = 1
# else:
#     x = 0
# print (x)
# 'or'
# x = 1 if condition else 0
# print (x)

"2. Đọc số khó đọc"
num1 = 10_000_000_000
num2 = 10_000_000
total = num1 + num2
print(f"{total:,}")

"3. dùng with open để khỏi quên f.close()"
with open(r"G:\KENSHIN\2020\TMA Solution\workspace2\git_home\data.txt", "r") as f:
    file_contents = f.read()
words = file_contents.split(" ")
word_count = len(words)
print(word_count)

"4. gắn index (id) cho items trong 1 collection"
names = ["Thành", "Thư", "Quý", "Nhãn"]

index = 0
for name in names:
    print(index, name)
    index += 1
"cách khác ngắn hơn"
for index, name in enumerate(names, start=1):
    print(index, name)

"5 ghép 2 collection bằng loop"
names = ["Thành", "Thư", "Quý", "Nhãn"]
roles = ["husband", "wife", "daddy", "mommy"]
chars = ["happy", "angry", "happy", "angry"]

for index, name in enumerate(names):
    role = roles[index]
    print(f"{name} is actually {role}")

"hoặc dùng zip trực tiếp, và zip nó ghép đc nhiều collection"
for name, role, char in zip(names, roles, chars):
    print(f"{name} is actuallay {role} and was {char}")

"zip có thể dùng để unpacking items của từng collection vào 1 tuple"
for value in zip(names, roles, chars):
    print(value)
print(type(value))

"""6. Unpacking mà ko muốn lấy hết item trong collection
dùng dấu _ underscore"""

a, _ = (1, 2)
print(a)
# print (b)
"ví dụ unpack nhiều values cho ít variable"
a, b, *c, d = (1, 2, 3, 4, 5)  # in c = [3,4,5]
# a, b, *_ = (1,2,3,4,5)
print(a)
print(b)
print(c)
print(d)
"_ có thể print đc nhiều giá trị, hoặc lấy giá trị cuối"

"7. khai báo attribute và get attribute"


class Person:
    pass


person = Person()

first_key = "first"
first_val = "Thanh"

setattr(person, first_key, first_val)
first = getattr(person, first_key)

print(first)
" dùng 1 dictionary để khai báo attribute cho instance"

person_info = {"first": "Thanh", "last": "Nguyen"}
for key, value in person_info.items():
    setattr(person, key, value)

# print (person.first)
# print (person.last)

for key in person_info.keys():
    print(getattr(person, key))

"8. input private information như password"

from getpass import getpass
username = input("Username: ")
password = getpass("Password: ")

print("Logging In...")

'9. '