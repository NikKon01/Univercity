import random
nch = 0
ch = 0
for i in range(100000):
    a = [0, 0, 1]
    choice = random.randint(0, 2)
    a.pop(choice)
    a.remove(0)
    if a[0] == 1:
        nch += 1
    else:
        ch += 1
print(f'Вероятность если поменять выбор: {nch/1000} %\nВероятность если не менять выбор: {ch/1000} %')