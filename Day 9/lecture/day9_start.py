# {"key": value}
programming_dictionary = {
    "Bug":
    "An error in a program that prevents the program from running as expected.",
    "Function":
    "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again."
}

'''
list[0] & dictionary 차이점
사전은 키가 식별하는 요소가 있음
'''

# retrieving items from dictionary.
print(programming_dictionary["Bug"])

문제 : 올바른 function을 사용하지 않음
ㄴ 데이터 형식에서 키를 제공하도록 해야함
Loop: "The action of doing something over and over again."
ㄴ KeyError: 'Loop'
9 : "seveteen members 9th."
print(programming_dictionary[9])  → 출력됨

# adding new items to dictionary.
programming_dictionary["svt"] = "seventeen is k-pop idol."

# create an empty dictionary
empty_dictionary = {}
empty_dictionary = []  # add function

# wipe an existion dictionary
programming_dictionary = {}
print(programming_dictionary)

# edit an iten in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."

# loop through a dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])

# Grading Program
student_grades = {}

for student in student_scores:
  score = student_scores[student]
  if score > 90:
      student_grades[student] = "Outstanding"
  elif score > 80:
      student_grades[student] = "Exceeds Expectations"
  elif score > 70:
      student_grades[student] = "Acceptable"
  elif score < 70:
      student_grades[student] = "Fail"

# Nesting Lists
# Nesting : 디렉토리 안에 디렉토리
'''
{
  key  : [list],
  key2 : {Dict},
}
'''

capitals = {
    "france": "paris",
    "germany": "berlin",
}

#nesting a list in a dictionary / 프랑스 항목을 변경해서 또 다른 사전을 넣을 수 있게 할 것
travel_log = {
    "france": {
        "cities_visited": ["paris", "lille", "dijon"],
        "total_visits": 12
    },
    "germany": {
        "cities_visited": ["berlin", "hamburg", "stuttgart"],
        "total_visits": 22
    }
}

# nesting, nesting, nesting
'''
[
  {
    key: [list],
    key2 : {dict},
  },
  {
    key: value,
    key2: value,
  }
]
'''

# Nesting Dectionaty in a List
travle_log = [
  {
    "country" : "france",
    "cities_visited" : ["paris", "lille", "dijon"],
    "total_visites" : 12
  },
  {
    "country" : "germany",
    "cities_visited" : ["berlin", "hamburg", "stuttgart"],
    "total_visits" : 22
  }
]