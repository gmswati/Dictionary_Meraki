dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
dic4={}
for keys1 in dic1:
    for keys2 in dic2:
        if keys1==keys2:
            dic4[keys1]=dic1[keys1]+dic2[keys2]
            for keys3 in dic3:
                if keys1==keys3:
                    dic4[keys1]=dic4[keys1]+dic3[keys3]
        else:
            # if dic1[keys1]
            dic4[keys1]=dic1[keys1]
            dic4[keys2]=dic2[keys2]
    for keys3 in dic3:
        if keys1==keys3:
            dic4[keys3]=dic1[keys1]+dic3[keys3]
        else:
            dic4[keys3]=dic3[keys3]
# for key2 in dic2:
#     for key3 in dic3:
#         if key2==key3:
#             dic4=dic2[key2]+dic3[key3]
#         else:
#             dic4[key2]=dic2[key2]
            # dic4[key3]=dic3[key3]
print(dic4)

# try to understand it's flow?
# How to improve this code,make this code univarsal?

