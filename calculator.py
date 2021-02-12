from math import *

array = []

def inp(n):
	n = int(input("How many numbers do you wish to operate on? : \n"))
	
def nums(array,n):
	
	for i in range(n):
		print("Enter item ",i+1)
		item=int(input())
		array.append(item)
	if len(array)==1:
		print("number is  : ", array)
	elif len(array)>=2:
		print("numbers are : ",array)
	else:
		print("Error...\n")
		
def add(array,n):
	sum = 0
	if n>1:
		for i in range(n):
			sum+=array[i]
		return sum
	elif n == 1:
		return array[0]
	else:
		return "Error\n"
	
def subtract(array,n):
	diff = array[0]
	if n>1:
		for i in range(1,n):
			diff-=array[i]
		return diff
	elif n == 1:
		return array[0]
	else:
		return "Error\n"
	
def multiply(array):
	mult = 1
	if n>1:
		for i in range(n):
			mult*=array[i]
		return mult
	elif n == 1:
		return array[0]
	else:
		return "Error\n"

def divide(array,n):
	
	div = 1
	if n>1:
		for i in range(n):
			div/=array[i]
		return div
	elif n == 1:
		return array
	else:
		return "Error\n"

	
		
	
	
def mean(array,size):
	sum=0
	for i in range(size):
		sum=sum+array[i]
		i+=1
	av=(sum)/size
	print("Mean is : ", av,  "\n")
	

def minimum(array,n):
		min=array[0]
		for i in range(1,n):
			if array[i]<min:
				min=array[i]
		print("Minimum element is : \n",min, "\n")
		
def maximum(array,n):
		max=array[0]
		for i in range(1,n):
			if array[i]>max:
				max=array[i]
		print("Maximum element is : \n",max,"\n")


def bubblesort(array,n):
		for i in range(n):
			for j in range(n-i-1):
				if array[j]>array[j+1] :
					temp = array[j]
					array[j] = array[j+1]
					array[j+1] = temp
		print("Sorted list is : ",array,"\n")

def median(array,n):
		bubblesort(array,n)
		middle = n/2
		if middle%2!=0:
			index = int(middle)
			print("Median is : ",array[index],"\n")
		else :
			half=int(middle)
			med=(array[half]+array[half-1])/2
			print("Median is : ",med,"\n")
			
			
def mode(input):
    counter = 2
    num = []

    for i in input:
        currentCounter = input.count(i);
        if(currentCounter >= counter):
            counter = currentCounter
            num.append(i)
    
    if(num == input):
        return "no mod found"

    num = list(set(num))

    if(len(num) < 1):
        return "no mod found"
    
    if(len(num)==1):
        	print("Mode is : ",num,"\n")
    
    if(len(num)>1):
    		print("Modes are : ",num,"\n")
			
			
			
while True:
	GC=int(input("""Choose a General  operation : 
	1. Basic
	2. Triginometric
	3. Hyperbolic
   	4. Conversions
	5. Exit\n"""))
	
	if GC == 1:
		while True:
			BC = str(input("""Choose a Basic Operation : 
		i)   Addition
		ii)  Subtraction
		iii) Multiplication
		iv) Division
		v)  Power
		vi) logarithm
		vii)Mean
		viii)Median
		ix) Mode
		x)  Minimum
		xi) Maximum 
		xii)Exit\n"""))
			
			if BC == "i": #addition
				n = int(input("How many numbers do you wish to operate on? : \n"))
				nums(array,n)
				print("Sum is : ",add(array,n))
				
			
			if BC == "ii": #subtraction
				n = int(input("How many numbers do you wish to operate on? : \n"))
				nums(array,n)
				print("Difference is : ",subtract(array,n))
				
			if BC == "iii":#Multiplication
				n = int(input("How many numbers do you wish to operate on? : \n"))
				nums(array,n)
				print("Product is : ",multiply(array,n))
			
			if BC == "iv":#Division
				n = int(input("How many numbers do you wish to operate on? : \n"))
				nums(array,n)
				print("Quotient is : ",divide(array,n))
				
				
			if BC == "v":#power
				a = float(input("Enter radix : "))
				b = float(input("Enter power : "))
				print("Answer is : ",pow(a,b))
			
			
			if BC == "vi":#log
				a = int(input("Input base : "))
				b = int(input("Input operand : "))
				print("Answer is : ",log(a,b))
				
			if BC == "vii":#mean
				n = int(input("Input list size : "))
				nums(array,n)
				mean(array,n)
				
			if BC == "viii":#median
				n = int(input("Input list size : "))
				nums(array,n)
				median(array,n)
				
			if BC == "ix":#mode
				n=int(input("Input list size : "))
				nums(array,n)
				mode(array)
				
			if BC == "x":#minimum
				n=int(input("Input list size : "))
				nums(array,n)
				minimum(array)
				
			if BC == "xi":#maximum
				n=int(input("Input list size : "))
				nums(array,n)
				maximum(array)
				
			if BC == "xii":#exit
				print("Exiting Basic Operations...\n")
				break
				
	
	if GC == 2:
			MC = str(input("""Choose a mode :
		a) Degrees
		b) Radian\n"""))
					
	while True:
			BC = str(input("""Choose a Trigonometric Operation : 
		i)   Trigonometric functions
		ii)  Inverse trigonometric functions
		iii) Exit\n"""))
		
			if BC == "i":
				while True:
			 		TF = str(input("""Choose a Trigonometric function : 
		i)  sin
		ii) cos
		iii)tan
		iv)cosec
		v) sec
		vi)cot
		vii)exit\n"""))
		
	if TF == "i":
								angle = int(input("Input angle : "))
								if MC == "a":
									angle = radians(angle)
								elif MC == "b":
									angle = degrees(angle)
								ans=sin(angle)
								print(f"cos({angle} = {ans}")
					
	
		
		
