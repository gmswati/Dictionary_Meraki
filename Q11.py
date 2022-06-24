# from multiprocessing import Value
# from re import M


my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
all_values=list(my_dict.values())
max=0
s_max=0
T_max=0
i=0
req_list=[]
while i<len(all_values):
    if max<all_values[i]:
        max=all_values[i]
    i+=1
print(max)
req_list.append(max)
all_values.remove(max)   
j=0
while j<len(all_values):
    if s_max<all_values[j]:
        s_max=all_values[j]
    j+=1
print(s_max)
req_list.append(s_max)
all_values.remove(s_max)   
j=0
while j<len(all_values):
    if T_max<all_values[j]:
        T_max=all_values[j]
    j+=1
print(T_max)
req_list.append(T_max)
print(req_list)
# req_list.reverse()
# print(req_list)










# for value in all_values:
#     if max<value:
#         max=value
#     if S_max<value and max!=value:
#         S_max=value
#     if T_max< value and max!=value and S_max!=value:
#         T_max=value
# print(max)
# print(S_max)
# print(T_max)



















































# max=0
# S_max=0
# T_max=0
# for key in my_dict:
#     if max<my_dict[key]:
#         max=my_dict[key]
#     elif S_max<my_dict[key] and S_max!=max:
#         S_max=my_dict[key]
#     elif T_max<my_dict[key] and T_max!=max and S_max!=max:
#         T_max=my_dict[key]
# print(max)
# print(S_max)
# print(T_max)

# How to improve this code?