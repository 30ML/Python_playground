data = ['또리', 1, 'M', '서울특별시 영등포구', 'Y']

f_str = f"""\
이름: {data[0]}
나이: {data[1]}
성별: {data[2]}
지역: {data[3]}
중성화 여부: {data[4]}\
"""
print(f_str)

print()

str_format = """\
이름: {}
나이: {}
성별: {}
지역: {}
중성화 여부: {}\
""".format(*data)
print(str_format)