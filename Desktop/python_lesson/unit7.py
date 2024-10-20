#-----------------------#
# eng2sp = {"one": 'uno', "two": 'dos', "three": 'tres'}
# eng2sp["four"] = "quatro"
# print(eng2sp)
# print(eng2sp["two"])
# print(len(eng2sp))
# print("one" in eng2sp)
# vals = eng2sp.values()
# print("dos" in vals)
#-----------------------#
# def histogram(s):
#     d = dict()
#     for c in s:
#         if c not in d:
#             d[c] = 1
#         else:
#             d[c] += 1
#     return d
# h = histogram('brontosaurus')
# print(h)
# print(h.get("a",0))
#-----------------------#
# def histogram(s):
#     d = dict()
#     for c in s:
#         d[c] = d.get(c, 0) + 1
#     return d

# def reverse_lookup(d, v):
#     for k in d:
#         if d[k] == v:
#             return k
#     raise LookupError()

# def invert_dict(d):
#     inverse = dict()
#     for key in d:
#         val = d[key]
#         if val not in inverse:
#             inverse[val] = [key]
#         else:
#             inverse[val].append(key)
#     return inverse

# h = histogram('parrot')
# key = reverse_lookup(h, 2)
# print(h)
# print(key)
# inverse = invert_dict(h)
# print(inverse)

#-----------------------#
# count = 0
# def example3(a):
#     global count
#     count2 = count + a
#     return count2
# print(example3(1))
#-----------------------#
# def create_dict_from_file(filename):
#     word_dict = {}
#     with open(filename, 'r') as file:
#         for line in file:
#             word = line.strip()
#             word_dict[word] = None
#     if 'apple' in word_dict:
#        print('Apple is in the dictionary!')
#        return word_dict
#
# word_dict = create_dict_from_file('words.txt')
# print(word_dict)
#-----------------------Tuple practice1#
# t1 = 'a',
# print(type(t1))
# t2 = tuple()
# print(t2)
# t3 = tuple('lupins')
# print(t3)
# t4 = ('a', 'b', 'c', 'd', 'e')
# t5 = ('A',) + t4[1:]
# print(t5)
#-----------------------Tuple practice2#
# t6 = (0,1,2)
# t7 = (0,3,4)
# def compare(a,b):
#     if a < b:
#         return True
#     else:
#         return False
# print(compare(t6,t7))
#-----------------------Tuple practice3#
# addr = 'monty@python.org'
# uname, domain = addr.split('@')
# print(uname)
# print(domain)
# t = divmod(7, 3)
# print(t) #quotient and remainder
# quot, rem = divmod(8, 3)
# print(quot) #quotient
# print(rem) #remainder
#-----------------------Tuple practice4#
# def printall(*args):
#     print(args)
# printall(1,2.0,"3")
# t = (7, 3)
# print(divmod(*t))
# print(max(1,2,3))
# print(min(1,2,3))
# def sum_all(*args):
#     return sum(args)
# print(sum_all(1,2,3))
#-----------------------Tuple practice5#
# s = 'abc'
# t = [0, 1, 2]

# def hello():
#     for pair in zip(s, t):
#         print(pair)
# print(hello()) #print each pair

# list(zip(s,t)) #make pairs as a list
# t2 = list(zip(s,t))
# def hello2():
#     for letter,number in t2:
#         print(number,letter)
# hello2()

# for index, element in enumerate('abc'):
#     print(index, element)
#-----------------------Tuple practice6#
# d = {'a':0, 'b':1, 'c':2}
# t = d.items()
# print(t)

# def hello3():
#     for key, value in d.items():
#         print(key, value)
# hello3()

# d = (dict(t))
# print(d)

# e = dict(zip('abc', range(3)))
# print(e)

#-----------------------Tuple practice7#
# Original dictionary with students and their courses
student_courses = {
    'Stud1': ['CS1101', 'CS2402', 'CS2001'],
    'Stud2': ['CS2402', 'CS2001', 'CS1102']
}

# Print the original dictionary
print("Original Dictionary:", student_courses)

# Function to invert the dictionary
def invert_dictionary(student_courses):
    # Create an empty dictionary for the inverted result
    inverted_dict = {}
    
    # Loop through each student and their courses in the original dictionary
    for student, courses in student_courses.items():
        # Loop through each course for the student
        for course in courses:
            # If the course is not already a key in the inverted dictionary, add it
            if course not in inverted_dict:
                inverted_dict[course] = []
            # Append the student to the list of students for that course
            inverted_dict[course].append(student)
    
    return inverted_dict

# Call the function to invert the dictionary and store the result
inverted_dict = invert_dictionary(student_courses)

# Print the inverted dictionary
print("Inverted Dictionary:", inverted_dict)

#-----------------------Tuple practice8#