# functions
# 함수를 이용해 중복코드를 줄이는 법
# 함수에 입력값, 출력을 제공하는 법
# 1. def
''' 
def my_function():
  # do this
  # then do this
  # finally do this

반복적으로 실행할 지침이 있을 때 작성해야 코드 양을 줄일 수 있음
'''

# 2. functions with inputs
'''
def my_function(something):
  # do this something
  # then do this
  # finally do this
'''

# functions with outputs (입력값을 볼 수 있게 해주는 함수)
'''
def my_function():
  result = 3 * 2
  return result

output = result
my_function() 호출 시 result 값 6이 출력
'''


# 1차
def format_name():
    f_name = input("성 : ")
    l_name = input("이름 : ")
    return f_name
    return l_name

format_name()


# 2차
def format_name(f_name, l_name):
    f_name = str(input("성: ")).title()
    l_name = str(input("이름: ")).title()
    return f_name
    return l_name

format_name()


# 3차
def format_name(f_name, l_name):
    print(f_name.title())
    print(l_name.title())


format_name("kim", "mingyu")


def format_name(f_name, l_name):
    format_f_name = f_name.title()
    format_l_name = l_name.title()
    return f"{format_f_name}.{format_l_name}"


format_string = format_name("kim", "MINGYU")
print(format_string)

# 함수 하나가 리턴문을 가졌을 때
'''
def 어쩌구():
  블라블라
  return ___ # return : 이 함수의 끝
'''


def format_name(f_name, l_name):
  """
  take a first and last name and format it to return the title case version of the name.
  """
    if f_name == "" or l_name == "":
        return "잘못입력하셨습니다."
    format_f_name = f_name.title()
    format_l_name = l_name.title()
    return f"result : {format_f_name}.{format_l_name}"


print(format_name(input("성 : "), input("이름 : ")))


# docstring
''' 
함수나 다른 코드블록에서 코딩할 때 문서 만드는 방법
그냥 쓰는 이거 ''' ''' 아니면 """ """를 쓰면 됨
'''

def svt(hp, vc, pp):
   ''' svt is hiphop, vocal, performance.'''
   # 이렇게 한 뒤 svt 하면 docsting이 뜸
