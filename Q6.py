dic={"ball":"red","bat":4,"wickets":8,'ball':"green","bat":3}
my_dic={}
for key in dic:
    if key not in my_dic:
        my_dic[key]=dic[key]
    else:
        pass
    # if key in my_dic:
    #     pass
    # else:
    #     my_dic[key]=dic[key]
print(my_dic)

# how to improve this code?