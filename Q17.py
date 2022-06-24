fruit = {}

def addone(index):
    if index in fruit:
        fruit[index] += 1
    else:
        fruit[index] = 1

addone('Apple')
# print(fruit)
addone('Banana')
# print(fruit)
addone('apple')
# print(fruit)
addone('Apple')

print(len(fruit))
print(fruit)