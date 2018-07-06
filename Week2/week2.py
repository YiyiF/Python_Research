# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 22:56:52 2018

@author: eleve
"""

def update(n,x):
    n = 2
    x.append(4)
    print('update:',n,x)
    
def main():
    n = 1
    x = [0,1,2,3]
    print('main:',n,x)
    update(n,x)
    print('main:',n,x)
    
main()

#Q1
def increment(n): 
   n += 1 
   print(n) 

n = 1 
increment(n) 
print(n)

#Q2
def increment(n):
   n += 1
   return n

n = 1
while n < 10:
   n = increment(n)
print(n)




class MyList(list):
    def remove_min(self):
        self.remove(min(self))
    def remove_max(self):
        self.remove(max(self))
        
        
x = [10, 3, 5, 1, 2, 7, 6,4,8]

y = MyList(x)
dir(x)
dir(y)
y.remove_min()
y.remove_max()


#Q1.2
class NewList(list): 
   def remove_max(self): 
     self.remove(max(self)) 
   def append_sum(self): 
     self.append(sum(self)) 

x = NewList([1,2,3]) 
while max(x) < 10: 
   x.remove_max() 
   x.append_sum() 
print(x) 


import numpy as np

zero_vector= np.zeros(5)

zero_matrix= np.zeros((5,3))

zero_vector
zero_matrix

#Q2.1-2
np.zeros(5)

#Q2.1-3
x = np.array([[3,6],[5,7]]) 
y = x.transpose() 
print(y) 


#2.2.2
import numpy as np
x = np.array([1,2,3])
y = np.array([2,4,6])
X = np.array([[1,2,3],[4,5,6]])
Y = np.array([[2,4,6],[8,10,12]])

z = x + y
X[:,1] + Y[:,1]
X[1,:] + Y[1,:]

#list & array
[2,4] + [6,8]

np.array([2,4]) + np.array([6,8])

#Q2.2-1
x = np.array([1,2,5]) 
x[1:2]


#2.2.3
z1 = np.array([1,3,5,7,9])
z2 = z1 + 1

ind = [0,2,3]

z1[ind]

ind = np.array([0,2,3])

z1[ind]

z1 > 6
z1[z1 > 6]
z2[z1 > 6]

ind = z1 > 6
z1[ind]
z2[ind]

#Q2.3-1
a = np.array([1,2]) 
b = np.array([3,4,5]) 
b[a]

c = b[1:] 
b[a] is c 


#2.2.4
np.linspace(0,100,10)

np.logspace(1, 2, 10) # (1,2,3) 1:log10=1,2:log100=2

np.logspace(np.log10(250),np.log10(500),10)



X = np.array([[1, 2, 3],[4, 5, 6]])
X.shape
X.size


x=20 
not np.any([x%i == 0 for i in range(2, x)])



#2.3
import matplotlib.pyplot as plt
plt.plot([0,1,4,9,16])


 x = np.linspace(0,10,20)

y1 = x**2.0

y2 = x**1.5

plt.plot(x, y1, "bo-")

plt.plot(x, y1, "bo-", linewidth=2, marksize=4)

plt.plot(x, y2, "gs-", linewidth=2, markersize=12 )




x = np.linspace(0,10,20)
y1 = x**2.0
y2 = x**1.5
plt.plot(x, y1, "bo-", linewidth=2, markersize=12 ,label="First")
plt.plot(x, y2, "gs-", linewidth=2, markersize=12 ,lable="Second")

plt.xlabel("$X$")
plt.ylabel("$Y$")
#different formular
plt.xlabel("X")
plt.ylabel("Y")

#adjusted axis
plt.axis([-0.5, 10.5, -5, 105])

#legend
x = np.linspace(0,10,20)
y1 = x**2.0
y2 = x**1.5

plt.plot(x, y1, "bo-", linewidth=2, markersize=12, label="First")
plt.plot(x, y2, "gs-", linewidth=2, markersize=12, lable="Second")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis([-0.5, 10.5, -5, 105])
plt.legend(loc="upper left")

plt.savefig(""myplot.pdf)


#2.3.3

#semilogx():x -> log(x) y -> y
#semilogy():x -> x y -> log(y)
#loglog():x -> log(x) y -> log(y)


x = np.linspace(0,10,20)
x = np.logspace(-1, 1, 40)
y1 = x**2.0
y2 = x**1.5

plt.loglog(x, y1, "bo-", linewidth=2, markersize=12, label="First")
plt.loglog(x, y2, "gs-", linewidth=2, markersize=12, lable="Second")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis([-0.5, 10.5, -5, 105])


#2.3.4
x = np.random.gamma(2, 3, 100000)
plt.figure()
plt.subplot(221)
plt.hist(x, bins = 30)
plt.subplot(222)
plt.hist(x, bins = 30, normed=True)
plt.subplot(223)
plt.hist(x, bins = 30, cumulative = 30)
plt.subplot(224)
plt.hist(x, bins = 30, normed = True, cumulative=True, histtype = "step")

plt.savefig("hist_4.pdf")


np.linspace(-5,5,21)


#2.4.1
import random
random.choice(["H", "T"])

random.choice([0, 1])

random.choice([1, 2, 3, 4, 5, 6])

random.choice(range(1,7))

#random.choice expect sequence:list
random.choice([range(1,7)])


random.choice([range(1,7), range(1,9), range(1,11)])

#outer:random choose from range(*,*)
random.choice(random.choice([range(1,7), range(1,9), range(1,11)]))

#Q2.4.1
sum(random.sample(range(10),10))
sum(random.choice(range(10),10)) for i in range(10)

#!!random.sample returns unique random elements


#2.4.1
import random

rolls = []
for k in range(1000000):
    rolls.append(random.choice([1,2,3,4,5,6]))
plt.hist(rolls, bins = np.linspace(0.5, 6.5, 7));

# y = x1 + x2 + x3 + ... + x10
# 10 < y < 60

ys = []
for rep in range(10000): 
    y = 0
    for k in range(10):
        x = random.choice([1,2,3,4,5,6])
        y = y + x
    ys.append(y)
plt.hist(ys);       


#2.4.3
import numpy as np

np.random.random()
#tuple
np.random.random((5,3))

#standard normal dis
np.random.normal(0,1)
#1D
np.random.normal(0,1,5)
#2D
np.random.normal(0,1,(2,5))

#random integer
np.random.randint(1, 7)


X = np.random.randint(1,7,(10,3))
X.shape
np.sum(X)
#dimension 0 ->sums over rows
np.sum(X, axis=0)
#dimension 1 ->sums over colums 
np.sum(X, axis=1)
#error  np.sum(X, axis=2)


Y = np.sum(X, axis=1)

X = np.random.randint(1,7,(1000000,10))
Y = np.sum(X, axis=1)
plt.hist(Y);


#5*2*3 
numpy.random.random((5,2,3))

numpy.random.normal(1,2,3)


#2.4.4
import time

start_time = time.clock()

end_time = time.clock()

end_time - start_time


import random
strat_time = time.clock()
ys = []
for rep in range(1000000):
    y = 0
    for k in range(10):
        x =random.choice([1,2,3,4,5,6])
        y = y + x
    ys.append(y)
end_time = time.clock()
print(end_time - start_time)

strat_time = time.clock()
X = np.random.randint(1,7,(1000000,10))
Y = np.sum(X, axis=1)
end_time = time.clock()
print(end_time - start_time)



delta_X = np.random.normal(0,1,(2,5))
import matplotlib.pyplot as plt
plt.plot(delta_X[0], delta_X[1], "go")

#cumulative sum
delta_X
X = np.cumsum(delta_X, axis = 1)

X_0 = np.array([[0],[0]])
np.random.normal(0,1,(2,5))
X = np.cumsum(delta_X,axis = 1)
plt.plot(X[0],X[1],"ro-")
plt.savefig("rw.pdf")


X_0 = np.array([[0],[0]])
delta_X = np.random.normal(0,1,(2,5))
X = np.concatenate((X_0,np.cumsum(delta_X,axis = 1)), axis = 1)
plt.plot(X[0],X[1],"ro-")
plt.savefig("rw2.pdf")

X_0 = np.array([[0],[0]])
delta_X = np.random.normal(0,1,(2,100))
X = np.concatenate((X_0,np.cumsum(delta_X,axis = 1)), axis = 1)
plt.plot(X[0],X[1],"ro-")
plt.savefig("rw3.pdf")



#homework

import numpy as np

def create_board():
    return np.zeros ((3,3))

board = create_board()

def place(board, player, position):
    if board[position] == 0:
        board[position] = player

def possibilities(board):
    not_occupied = np.where(board == 0)
    return list(zip(not_occupied[0], not_occupied[1]))

print(possibilities(board))









