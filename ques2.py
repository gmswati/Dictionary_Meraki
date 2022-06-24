# a=2
# def my(b):
#     print(a+b)
# print('megha')
# my(10)
# dict={'swati':22,'pragati':17}
# print(dict[0])

a=[[1,2,3],4,[5,6,7],8,[9,10,11],12]
# method 1:
# i=0
# while i<len(a):
#     if type(a[i])!=list:
#         a[i-1].append(a[i])
#         a.remove(a[i])
#     else:
#         pass
#     i+=1
# print(a)

# How to improve it?
# method 2:
i=0
lists=[]
list_item=[]
while i<len(a):
    if type(a[i])==list:
        lists.append(a[i])
    else:
        list_item.append(a[i])
    i+=1
print(lists)
i=0
while i<len(lists):
    lists[i].append(list_item[i])
    i+=1
print(lists)