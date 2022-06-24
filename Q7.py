given_list=[{'first':'1'},{'second':'2'},{'third':'1'},{'four':'5'},{'five':'5'},{'six':'9'},{'seven':'7'}]


i=0
req_list=[]
while i<len(given_list):
    for item in given_list[i]:
        value=given_list[i][item]
    if value not in req_list:
        req_list.append(value)
    
    i+=1
print(req_list)

# how to improve this code?
# improved :)
# I did it...