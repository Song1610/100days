from prettytable import PrettyTable

# todo 1: Create a PrettyTable object and save it to a variable called table
table = PrettyTable()

# todo 2: 표 만들기

table.add_column("Pokemon Name", ["피카츄", "꼬부기", "파이리"])
table.add_column("Type", ["전기", "물", "불"])

# todo 3: 중앙정렬에서 좌측정렬로 변경
# table.align["Pokemon Name"] = "l"
# table.align["Type"] = "l"
# table.add_column("Pokemon Name", ["피카츄", "꼬부기", "파이리"], "l")
# table.add_column("Type", ["전기", "물", "불"], "l")
table.align = "l"
# 위의 4개의 줄 = table.aling = "l" 

print(table.align)
print(table)