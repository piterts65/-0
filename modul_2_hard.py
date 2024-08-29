import random
list_ = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
n=random.choice(list_)
print(n)

def result():
    string = ''
    for i in range(1, n):
        for j in range(i+1, n):
            if n % (i+j) == 0:
                string += str(i)+str(j)
    return string
print(result())

















