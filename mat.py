# esty Friedman
# adi Buchris
# malky Rotshild
#from math import round
from datetime import datetime

def dominanty(M):
    n = len(M)
    count = n

    for i in range(n):
        sum_row = 0
        for j in range(n):
            sum_row = sum_row + abs(M[i][j])
        x =(sum_row - abs(M[i][i]))
        y =abs(M[i][i])
        if (y > x):
            count -=1
    if (count !=0):
        print("None Dominant Diagonal\n")
        return 0
    else:
        print("Dominant Diagonal\n")
        return 1

def final_answer(x):
    now = datetime.now()
    the_date = now.day * 10000 + now.hour * 100 + now.minute
    # print(the_date)
    x = float(x)
    x = str(round(x, 6)) + "00000" + str(the_date)
    return x


# Defining our function as seidel which takes 3 arguments
# as A matrix, Solution and B matrix
def jacoby(a, x, b):
    # Finding length of a(3)
    n = len(a)
    # for loop for 3 times as to calculate x, y , z
    y=[0 for a in x]
    for j in range(0, n):
        # temp variable d to store b[j]
        d = b[j]

        # to calculate respective xi, yi, zi
        for i in range(0, n):
            if (j != i):
                d -= a[j][i] * x[i]

                # updating the value of our solution
        y[j] = d / a[j][j]
        # returning our updated solution
    return y

def seidel(a, x, b):
    # Finding length of a(3)
    n = len(a)
    # for loop for 3 times as to calculate x, y , z
    for j in range(0, n):
        # temp variable d to store b[j]
        d = b[j]

        # to calculate respective xi, yi, zi
        for i in range(0, n):
            if (j != i):
                d -= a[j][i] * x[i]
                # updating the value of our solution
        x[j] = d / a[j][j]
        # returning our updated solution
    return x


def calsEps(x,y,eps):
    for i in range(len(x)):
        if abs(x[i]-y[i])>eps:
            return True
    return False


def mainSeidel(a,x,b,eps):
    first=[eps+1 for a in x]
    iter=0
    while(calsEps(x,first,eps)):
        iter=iter+1
        first = [a for a in x]
        x = seidel(a, x, b)
        print(x)
        #print each time the updated solution

    print("\nThe solution in the Seidel method:")
    for i in range (len (x)):
        x[i] =final_answer(x[i])

    print(x)
    print("number of itertion="+ str(iter))
    print("\n\n")


def mainJacoby(a,x,b,eps):
    first=[eps+1 for a in x]
    iter=0
    while(calsEps(x,first,eps)):
        iter=iter+1
        first = [a for a in x]
        x = jacoby(a, x, b)
        print(x)

        #print each time the updated solution
    print("\nThe solution in the Jacoby method:")
    for i in range (len (x)):
        x[i] =final_answer(x[i])

    print(x)
    print("number of itertion="+ str(iter))

# int(input())input as number of variable to be solved
n = 3
a = []
b = []
# initial solution depending on n(here n=3)
x =  [0, 0, 0]
x2 = [0, 0, 0]
a = [[10, 8, 1], [4, 10, -5], [5, 1, 10]]
b = [-7, 2, 1.5]
if dominanty(a):
    print("The initial posting is:")
    print(x)
    eps=0.0001
    mainSeidel(a, x, b, eps)
    mainJacoby(a, x2, b, eps)
else:
    pass