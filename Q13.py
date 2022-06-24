my_dict = {
    'a':50, 
    'b':58,
    'c': 56,
    'd':40,
    'e':100, 
    'f':20
    }

highest=max(my_dict,key=my_dict.get)
print(highest)
s_max=max(my_dict,key=my_dict.get)
print(s_max )





# max=0
# S_max=0
# T_max=0
# for key in my_dict:
#     if max<my_dict[key]:
#         max=my_dict[key]
#         m_key=key
# # for key in my_dict:
#     if S_max<my_dict[key] and S_max!=max:
#         S_max=my_dict[key]
#         s_key=key
# # for key in my_dict:
#     if T_max<my_dict[key] and T_max<max and T_max<S_max:
#         T_max=my_dict[key]
#         t_key=key
# print(max)
# print(S_max)
# print(T_max)
# print(m_key)
# print(s_key)
# print(t_key)


