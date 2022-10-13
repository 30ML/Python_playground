import datetime

input_text = input("입력: ")

if input_text == "안녕":
    print("안녕하세요.")
elif input_text == "지금 몇 시야?" or input_text == "지금 몇 시에요?":
    now_hour = datetime.datetime.now().hour
    print("지금은 {}시입니다.".format(now_hour))
else:
    print(input_text)
