# def sum_many(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i
#     return sum
# print(sum_many(1,2,3))

def average(*args):   
     result = 0
     for i in args:
         result += i
     return result / len(args)

print(average(22,55,8,885))