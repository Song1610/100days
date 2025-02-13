def format_name(f_name, l_name):
    # name에 아무것도 입력하지 않았을 때 코드를 빠르게 끝내는 법
    if f_name == "" or l_name == "":
        return "아무것도 입력되지 않았습니다."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"result : {formated_f_name} {formated_l_name}"       # 문장의 끝
    print("got the printed test!")  # return을 사용했기 때문에 출력되지 않음

print(format_name(input("first name : "), input("last name: ")))
