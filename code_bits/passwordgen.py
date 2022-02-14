import random

# def genPassword(l=0):
#     if l < 8 or l > 15 or l == 0:
#         l = random.randint(8, 15)
#         print("Password must be from 8 to 15 characters!")
#     chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&*?"
#     for idx in range(l):
#         if idx == 0:
#             password = chars[random.randint(0, 25)]
#         elif idx == (len(list(range(l))) - 1):
#             password = password + chars[random.randint(62, 69)]
#         elif idx > (len(list(range(l))) - 3):
#             password = password + chars[random.randint(52, 61)]
#         else:
#             password = password + chars[random.randint(0, 61)]
#     return password

# print(genPassword())

# one line
# def gen(l):
#     chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&*?"
#     print([(chars[random.randint(0, 25)] if idx == 0 else chars[random.randint(62, 69)] if idx == (len(list(range(l))) - 1) else chars[random.randint(52, 61)] if idx > (len(list(range(l))) - 3) else chars[random.randint(0, 61)]) for idx in range(l)])
# gen(9)



import random


gen = lambda l, c="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&*?": print([(c[random.randint(0, 25)] if idx == 0 else c[random.randint(62, 69)] if idx == (len(list(range(l))) - 1) else c[random.randint(52, 61)] if idx > (len(list(range(l))) - 3) else c[random.randint(0, 61)]) for idx in range(l)])

gen(9)













