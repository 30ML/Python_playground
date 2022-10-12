PI = 3.141592

radius = float(input("구의 반지름을 입력해주세요: "))

# 부피: 4/3 * PI * r^3
# 겉넓이: 4 * PI * r^2
print("구의 부피는 {}입니다.".format(4 / 3 * PI * radius ** 3))
print("구의 겉넓이는 {}입니다.".format(4 * PI * radius ** 2))