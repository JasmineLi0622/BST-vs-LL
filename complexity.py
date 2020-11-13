# activity 2 part2
import sys
sys.path.append(r"C:\Users\17550\Desktop\Python\CW1\activity2 K20056947")

from binarysearchtree import BinarySearchTree as bst
import random

def random_tree(n):
    if type(n)==int:
        if n>=0:
            rand_num=[]
            while len(rand_num)!=n:
                new_num=random.randint(1, 1000)
                if new_num not in rand_num:
                    rand_num.append(new_num)
            BST=bst()
            while rand_num!=[]:
                BST.insert(rand_num.pop(0))
            return(BST)
        else:
            print('the n must be a nonnegative int')
    else:
        print('the n must be a nonnegative int')


X=list(range(5,105,5))
Y=[]
size=1000
import time

for x in X:
    capture_time=0
    for i in range(size):
        cur_tree=random_tree(x)
        start_time=time.time()
        for j in range(500):
            #since my computer run the search really fast, and the duration time is 0.0
            #so here i have to repeat this method many times, so that i can see the trend
            cur_tree.search(42)
        end_time=time.time()
        capture_time+=end_time-start_time
    Y.append(capture_time/size)
    
'''the supposed code without rep:
for x in X:
    capture_time=0
    for i in range(size):
        cur_tree=random_tree(x)
        start_time=time.time()
        cur_tree.search(42)
        end_time=time.time()
        capture_time+=end_time-start_time
    Y.append(capture_time/size)
'''

import matplotlib.pyplot as plt
plt.plot(X, Y)
plt.xlabel('Size of trees')
plt.ylabel('Search time')
plt.ticklabel_format(axis='both', style='sci', scilimits=(0,0))
plt.show()

'''Complexity analysis X vs Y
Though there are some fluctuations in the plot which may caused by other running programs, in general, 
the plot shows an increasing trend. Also, as the size grows, the increase in running time slightly
slows down, which implies the complexity might be logarithmic. But the increase rate seems to be
faster than that of a logarithmic complexity.

'''
#the fluctuation caused by other systems might make Y[1] less than Y[0],
#making the linear and logarithmic complexity seem ackward, please try to avoid this situation
c_l=(Y[1]-Y[0])/5
b_l=Y[0]-5*c_l
Y2=[c_l*x+b_l for x in X]

import math
c_log=(Y[1]-Y[0])/(math.log(10,2)-math.log(5,2))
b_log=Y[0]-math.log(5,2)*c_log
Y3=[c_log*math.log(x,2)+b_log for x in X]

plt.plot(X, Y)
plt.plot(X, Y2)
plt.plot(X, Y3)
plt.legend(['BST','Linear','Logarithmic'])
plt.xlabel('Size of trees')
plt.ylabel('Search time')
plt.ticklabel_format(axis='both', style='sci', scilimits=(0,0))
plt.show()

'''Complexity analysis X vs Y, Y2 and Y3
Generally, the line falls between the ideal linear complexity line and the logarithmic complexity line，
The line grows faster than logarithmic complexity line, but slower than linear complexity line. 

The reason behind this might be: the randomly created Binary Search Tree is not restricted to be 
balanced.
For a Binary Search Tree,the maximum times of comparison while searching is the height of the tree.
If a Binary Search Tree of size n is balanced, then the searching complexity has the same orders of 
magnitude with log2(n). On the contrary, the worst situation is that a list of monotone increasing 
or decreasing numbers are generated to create a Binary Search Tree, consequently, this Binary Search 
Tree is similar to a linked list, and the searching complexity is O(n).
Since our code generates the Binary Search Tree randomly and takes the average searching time, so
the line does not follow exactly the same as Y2 or Y3.

To fix this, we should try to keep the generate tree balanced. For example, we can test if the tree
will become unbalanced when a number is inserted, if true, then we can either cancel this insert progress, 
generate another number and try insert again, or try to rotate the tree to keep it balanced. 
'''




from linkedlist import LinkedList as ll
def random_list(n):
    if type(n)==int:
        if n>=0:
            rand_num=[]
            while len(rand_num)!=n:
                new_num=random.randint(1, 1000)
                rand_num.append(new_num)
            LL=ll()
            while rand_num!=[]:
                LL.insert(rand_num.pop(0))
            return(LL)
        else:
            print('the n must be a nonnegative int')
    else:
        print('the n must be a nonnegative int')


Y4=[]
for x in X:
    capture_time=0
    for i in range(size):
        cur_list=random_list(x)
        start_time=time.time()
        for j in range(500):
            #since i repeat the bst search method 400 times, 
            #to be comparable, i also repeat the ll search method 500 times
            cur_list.search(42)
        end_time=time.time()
        capture_time+=end_time-start_time
    Y4.append(capture_time/size)
        
plt.plot(X, Y)
plt.plot(X, Y2)
plt.plot(X, Y3)
plt.plot(X, Y4)
plt.legend(['BST','Linear','Logarithmic','LL'])
plt.xlabel('Size of trees')
plt.ylabel('Search time')
plt.ticklabel_format(axis='both', style='sci', scilimits=(0,0))
plt.show()

''' Complexity analysis X vs Y, Y2, Y3 and Y4
The shape of Y4 appears to be linear, and it always falls above Y2, Y, Y3 which means the searching 
efficiency of linked list is lower than that of binary search tree at any size. Also, as the n 
increases, the searching efficiency gap between linked list and binary search tree becomes much larger.
In conclusion, the bianry search tree is much more efficient when searching than linked list, and thus
it is more suitable for searching than linked list. 

'''


