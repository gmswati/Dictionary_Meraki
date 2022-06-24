word='MISSISSIPPI'
i=0
dict={}
list=[]
while i<len(word):
    if word[i] in word:
        list.append(word[i])
    i+=1
print(list)
for item in list:
    c=0
    for letter in word:
        if item==letter:
            c+=1
    dict[item]=c
print(dict)

# Method 2

# word='MISSISSIPPI'
# i=0
# dict={}
# list=[]
# while i<len(word):
#     if word[i] not in list:
#         list.append(word[i])
#     i+=1
# print(list)
# for item in list:
#     c=0
#     for letter in word:
#         if item==letter:
#             c+=1
#     dict[item]=c
# print(dict)