#Think Python 2 - Chapter10
#---------------------------
# name = ["John", "Mary"]
# print(name[1])
# cheeses = ['Cheddar', 'Edam', 'Gouda']
#---------------------------
# def cheese_list(i):
#     for i in cheeses:
#         print(i)
# cheese_list(cheeses)
#---------------------------
# test = [1,2,3,4,5,6]
# def add_all(t):
#     total = 0
#     for x in t:
#         total += x
#     print(total)
# add_all(test)
#---------------------------
# t=[1,2,3]
# print(sum(t))
#---------------------------
# classmate = ["ann", "cindy","tim"]
# def capitalize_all(t):
#     res = []
#     for s in t:
#         res.append(s.capitalize())
#     return res
# print(capitalize_all(classmate))
#---------------------------
# classmate = ["aNn", "Cindy","TOM"]
# def only_upper(t):
#     res = []
#     for s in t:
#         if s.isupper():
#             res.append(s)
#     return res
# print(only_upper(classmate))
#---------------------------
# s = 'spam'
# t = list(s)
# print(t)
#---------------------------
# s = 'pining for the fjords'
# t = s.split()
# print(t)
#---------------------------
# s = 'spam-spam-spam'
# delimiter = '-'
# t = s.split(delimiter)
# print(t)
#---------------------------
# t = ['pining', 'for', 'the', 'fjords']
# delimiter = ' '
# s = delimiter.join(t)
# print(s) 
#---------------------------
# t1 = [1, 2]
# t2 = t1.append(3)
# print(t1)
# print(t2)
#---------------------------
# t1 = [1, 2]
# t2 = t1.append(3)
# t3 = t1 + [4]
# print(t1)
# print(t3)
#---------------------------
# t= [1,5,3,4,6,2,]
# t.sort()
# print(t)
#---------------------------
# employees = ["Alice Ash", "Bob Bite", "Cathy Cole", "Dave Drake", "Elvis Echo", "Fred Ford", "George Grey", "Harry Higgs", "Ivan Iron", "Joe Jason"]
# subList1 = employees[:5]
# subList2 = employees[5:]
# subList2.append("Kriti Brown")
# del subList1[1]
# merged_list = subList1 + subList2
# salaryList = [20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000]

# def salaryUp(salaries):
#     for i in range(len(salaries)):
#         salaries[i] =int (salaries[i] * 1.04)
#     return salaries
# salaryList = salaryUp(salaryList)

# top_salaries = sorted(salaryList, reverse=True)[:3]
# print(top_salaries)

sentence = input("Please enter a sentence: ")
word_list = sentence.split()
word_list.reverse()
print(word_list)