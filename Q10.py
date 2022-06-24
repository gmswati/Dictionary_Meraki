dict1 =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']
   }
count=0
for key in dict1:
    if type (dict1[key])==list:
        for item in dict1[key]:
            count+=1
    else:
        count+=1
print('Total Count:',count)