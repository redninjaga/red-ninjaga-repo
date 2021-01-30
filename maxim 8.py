# print(9 % 4)
#  print(2**5)
#  print(2//5)
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# c = []
# for x in a:
#     for y in b:
#         if x == y:
#             c.append(x)
# print(c)
d ={1: 12, 3: 4, 4: 3, 2: 1, 0: 0}
result = sorted(d, key=d.get,reverse = False)
# result_revers = sorted(d, key=d.get, reverse = True)
print(result)
# print(result_revers)