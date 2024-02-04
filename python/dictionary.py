# dic = {
#     "Sojib" : 3,
#     "Sagor" : 10,
#     "Hasnat" : 5,
#     "Sowrav" : 6
# }
# # print(dic["Sojib2"])  <- throws an error if not found
# print(dic.get('Sojib2'))
# print(dic.keys())
# print(dic.values())
# for key, value in dic.items():
#     print(key, end=" ")
#     print(value)

dic1 = {
    1 : "Hridoy",
    2 : "Adnan",
    3 : "Sojib"
}
dic2 = {
    4 : "Rashfi",
    5 : "Hasnat",
    6 : "Sowrav"
}
dic1.update(dic2)
print(dic1)
dic1.pop(4)
print(dic1)
dic1.popitem()
del dic2
print(dic1)

