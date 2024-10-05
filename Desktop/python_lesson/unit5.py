# def print_n(n):
#     while n != 0:
#         print(n)
#         n = n - 1
#     else:
#         print("Blast off!")
# print_n(3)
# ------------------------
# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)
# print('Done!')
# ------------------------
# def reverse_print(string):
#     index = len(string) - 1  # 最初のインデックスを文字列の最後の文字に設定
#     while index >= 0:  # インデックスが0以上の間ループ
#         print(string[index])  # 現在のインデックスの文字を表示
#         index = index - 1  # インデックスを1つ減らす

# # 関数の使用例
# fruit = 'banana'
# reverse_print(fruit)
# ------------------------
# fruit = 'banana'  
# print(fruit[:])
# ------------------------
# def find(word, letter):  
#     index = 0  
#     while index < len(word):  
#         if word[index] == letter:  
#             return index  
#         index = index + 1  
#     return -1
# print(find("hello", "o"))
# ------------------------

# def count(word, letter):
#     find = 0
#     for char in word:  
#       if char == letter:
#         find = find + 1
#     return(find)
    
# print(count("banana","a"))
# ------------------------

# word = 'banana'
# new_word = word.upper()
# print(new_word)
# ------------------------

# word = "banana"
# index = word.find("na")
# print(index)
# ------------------------

#Exercise8.2
#word = 'banana'
#print(word.count('a'))
# ------------------------

#Exercise8.3
# def is_palindrome(word):
#     return word == word[::-1]
# print(is_palindrome("racear"))
# ------------------------

# # Exercise8.4
# def any_lowercase1(s):
#     for c in s:
#         if c.islower():
#             return True
#         else:
#             return False
# print(any_lowercase1("Hello"))


# def any_lowercase2(s):
#     for c in s:
#         if 'c'.islower():
#             return 'True'
#         else:
#             return 'False'
        
# print(any_lowercase2("HELLO"))
# # ------------------------

# def any_lowercase3(s):
#     for c in s:
#         flag = c.islower()
#     return flag
# print(any_lowercase3("Hello"))
# # ------------------------

# def any_lowercase4(s):
#     flag = False
#     for c in s:
#         flag = flag or c.islower()
#     return flag
# print(any_lowercase4("Hello"))
# ------------------------

# def any_lowercase5(s):
#     for c in s:
#         if not c.islower():
#             return False
#     return True
# print(any_lowercase5("Hello"))

# #Assignment
# #Step1:input user's name
# name = input("Type your name: ")

# #Step2:input number of letters from the left
# n = int(input("Type how many characters to display from the left:"))

# #Step3:Display the first n characters from the name
# print("First", n, "characters: ", name[:n])

# #Step4:check the number of vowels
# vowels = 'aeiouAEIOU'
# vowel_count = sum(1 for char in name if char in vowels)
# print("Number of vowels in the name: ", vowel_count)

# #Step5:Reverse user's name
# reversed_name = name[::-1]
# print("Reversed name: ", reversed_name)

n = 10000
count = 0
while n:
    count = count + 1
    n = n // 10
print (count)