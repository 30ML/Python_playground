import itertools

문자열 = "0123456789"

# for i in 문자열:
#     for j in 문자열:
#         for k in 문자열:
#             print(i, j, k)

for 패스워드_길이 in range(1, 5):
    input()
    for password in itertools.product(문자열, repeat=패스워드_길이):
        print(password)
        print("".join(password))
