dict1={'name':"raju","marks":56}
keys=input('enter required key:')
# for key in dict1:
key_list=dict1.keys()
print(key_list)
if keys in key_list:
    print('exist')
else:
    print('not exist')