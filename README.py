# geitplTest1
'''1.Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.'''

for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i,end=',')
        
      
'''2.Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320'''

fact = 1
num = int(input("Enter the number: "))

if(num < 0 or num==0):
   print("Sorry")
 else:
     for i in range(1,num+1):
         fact = fact*i

 print(fact)

'''3.With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included).
and then the program should print the dictionary.Suppose the following input is supplied to the program: 8Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}'''

 dic = {}
 a = int(input("Enter the number: "))


for i in range(1,a+1):
     dic[i] = i*i
 print(dic)



'''4.Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')'''

 li = input("Enter").split(",")
 tup = tuple(li)
 print(li)
 print(tup)

take_input = input('Type the nubers in list with comma:  ')
li = list(take_input.split(','))
tup = tuple(take_input.split(','))
print(li)
print(tup)



'''5.Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.'''

class stringcontest: 
  def __init__(self,x):
         self.x = x
      
  def getstring(self):
      print(self.x)
      
  def printString(self):
      print(self.x.upper())




'''6.Write a program that calculates and prints the value according to the given formula:

Q = Square root of [(2 _ C _ D)/H]

Following are the fixed values of C and H:

C is 50. H is 30.

D is the variable whose values should be input to your program in a comma-separated sequence.For example Let us assume the following comma separated input sequence is given to the program:

100,150,180
The output of the program should be:

18,22,24'''



'''7.Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i _ j.*

Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5

Then, the output of the program should be:

[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]'''





'''8.Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

Suppose the following input is supplied to the program:

without,hello,bag,world
Then, the output should be:

bag,hello,without,world'''



'''9.Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

Suppose the following input is supplied to the program:

Hello world
Practice makes perfect
Then, the output should be:

HELLO WORLD
PRACTICE MAKES PERFECT'''


'''10. sort list Li=[5, 10, 20, 4, 8, 7, 9, 20, 30] without using sort method.'''

Li=[5, 10, 20, 4, 8, 7, 9, 20, 30]
new_list=[]

while Li:
  minimum = Li[0]
  for x in Li:
    if x < minimum:
      minimum = x
  new_list.append(minimum)
  Li.remove(minimum)

print (new_list)
