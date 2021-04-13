from math import *
from sympy import *

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
	
def multiply(array,n):
	mult = 1
	if n>1:
		for i in range(n):
			mult*=array[i]
		return mult
	elif n == 1:
		return array[0]
	else:
		return "Error\n"

def rad(ans):
	return (ans*180)/pi

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
				minimum(array,n)
				
			if BC == "xi":#maximum
				n=int(input("Input list size : "))
				nums(array,n)
				maximum(array,n)
				
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
						input_angle = int(input("Input angle : "))
						if MC == "a":
							angle = radians(input_angle)
						elif MC == "b":
							angle = degrees(input_angle)
						ans=sin(angle)
						approx=round(ans,2)
						print(f"sin({input_angle}) = {approx}")

					if TF == "ii":
						input_angle = int(input("Input angle : "))
						if MC == "a":
							angle = radians(input_angle)
						elif MC == "b":
							angle = degrees(input_angle)
						ans=cos(angle)
						approx=round(ans,2)
						print(f"cos({input_angle}) = {approx}")

					if TF == "iii":
						input_angle = int(input("Input angle : "))
						if MC == "a":
							angle = radians(input_angle)
						elif MC == "b":
							angle = degrees(input_angle)
						ans=tan(angle)
						approx=round(ans,2)
						print(f"tan({input_angle}) = {approx}")

					if TF == "iv":
						input_angle = int(input("Input angle : "))
						if MC == "a":
							angle = radians(input_angle)
						elif MC == "b":
							angle = degrees(input_angle)
						ans=cosec(angle)
						approx=round(ans,2)
						print(f"cosec({input_angle}) = {approx}")

					if TF == "v":
						input_angle = int(input("Input angle : "))
						if MC == "a":
							angle = radians(input_angle)
						elif MC == "b":
							angle = degrees(input_angle)
						ans=sec(angle)
						approx=round(ans,2)
						print(f"sec({input_angle}) = {approx}")

					if TF == "vi":
						input_angle = int(input("Input angle : "))
						if MC == "a":
							angle = radians(input_angle)
						elif MC == "b":
							angle = degrees(input_angle)
						ans=cot(angle)
						approx=round(ans,2)
						print(f"cot({input_angle}) = {approx}")

					if TF == "vii":
						break
				

			if BC == "ii":
				while True:
					TF = str(input("""Choose a Trigonometric function : 
					i)  arcsin
					ii) arccos
					iii)arctan
					iv)arccosec
					v) arcsec
					vi)arccot
					vii)exit\n"""))

					if TF == "i":
						input_number = float(input("Input number : "))
						
						ans=asin(input_number)
						approx=round(ans,2)

						if MC=="a":
							final = rad(approx)

							if input_number == 1 or isclose(90,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
								print(f"arcsin({input_number}) = 90")
								break

							if input_number == 0.866 or isclose(60,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
								print(f"arcsin({input_number}) = 60")
								break

							if input_number == 0.7071 or isclose(45,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
								print(f"arcsin({input_number}) = 45")
								break

							if input_number == 0.5 or isclose(30,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
								print(f"arcsin({input_number}) = 30")
								break

							if input_number == 0 or isclose(0,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
								print(f"arcsin({input_number}) = 0")
								break

							else:
								print(f"arcsin({input_number}) = {final}")
								break

						elif MC == "b":
							print(f"arcsin({input_number}) = {approx}")

						else:
							sys.exit(1)
							

					if TF == "ii":
						input_number = float(input("Input number : "))
						
						ans=acos(input_number)
						approx=round(ans,2)

						if MC=="a":
							final = rad(approx)

							if input_number == 0 or isclose(90,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
								print(f"arccos({input_number}) = 90")
								break

							if input_number == 0.5 or isclose(60,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
								print(f"arccos({input_number}) = 60")
								break

							if input_number == 0.7071 or isclose(45,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
								print(f"arccos({input_number}) = 45")
								break

							if input_number == 0.866 or isclose(30,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
								print(f"arccos({input_number}) = 30")
								break

							if input_number == 1 or isclose(0,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
								print(f"arccos({input_number}) = 0")
								break

							else:
								print(f"arccos({input_number}) = {final}")
								break

						elif MC == "b":
							print(f"arccos({input_number}) = {approx}")

						else:
							sys.exit(1)

					if TF == "iii":
						input_number = float(input("Input number : "))
						
						ans=atan(input_number)
						approx=round(ans,2)

						if MC=="a":
							final = rad(approx)

							if input_number == inf or isclose(90,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
								print(f"arctan({input_number}) = 90")
								break

							if input_number == 1.732 or isclose(60,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
								print(f"arctan({input_number}) = 60")
								break

							if input_number == 1 or isclose(45,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
								print(f"arctan({input_number}) = 45")
								break

							if input_number == 0.577 or isclose(30,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
								print(f"arctan({input_number}) = 30")
								break

							if input_number == 0 or isclose(0,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
								print(f"arctan({input_number}) = 0")
								break

							else:
								print(f"arctan({input_number}) = {final}")
								break

						elif MC == "b":
							print(f"arctan({input_number}) = {approx}")

						else:
							sys.exit(1)

					if TF == "iv":
						input_number = float(input("Input number : "))
						
						ans=acosec(input_number)
						approx=round(ans,2)

						if MC=="a":
							final = rad(approx)

							if input_number == 1 or isclose(90,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
								print(f"arccosec({input_number}) = 90")
								break

							if input_number == 1.155 or isclose(60,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
								print(f"arccosec({input_number}) = 60")
								break

							if input_number == 1.414 or isclose(45,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
								print(f"arccosec({input_number}) = 45")
								break

							if input_number == 2 or isclose(30,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
								print(f"arccosec({input_number}) = 30")
								break

							if input_number == inf or isclose(0,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
								print(f"arccosec({input_number}) = 0")
								break

							else:
								print(f"arccosec({input_number}) = {final}")
								break

						elif MC == "b":
							print(f"arccosec({input_number}) = {approx}")

						else:
							sys.exit(1)

					if TF == "v":
						input_number = float(input("Input number : "))
						
						ans=asec(input_number)
						approx=round(ans,2)

						if MC=="a":
							final = rad(approx)

							if input_number == inf or isclose(90,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
								print(f"arcsec({input_number}) = 90")
								break

							if input_number == 2 or isclose(60,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
								print(f"arcsec({input_number}) = 60")
								break

							if input_number == 1.414 or isclose(45,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
								print(f"arcsec({input_number}) = 45")
								break

							if input_number == 1.155 or isclose(30,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
								print(f"arcsec({input_number}) = 30")
								break

							if input_number == 1 or isclose(0,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
								print(f"arcsec({input_number}) = 0")
								break

							else:
								print(f"arcsec({input_number}) = {final}")
								break

						elif MC == "b":
							print(f"arcsec({input_number}) = {approx}")

						else:
							sys.exit(1)

					if TF == "vi":
						input_number = float(input("Input number : "))
						
						ans=atan(input_number)
						approx=round(ans,2)

						if MC=="a":
							final = rad(approx)

							if input_number == 0 or isclose(90,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
								print(f"arctan({input_number}) = 90")
								break

							if input_number == 0.577 or isclose(60,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
								print(f"arctan({input_number}) = 60")
								break

							if input_number == 1 or isclose(45,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
								print(f"arctan({input_number}) = 45")
								break

							if input_number == 1.732 or isclose(30,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
								print(f"arctan({input_number}) = 30")
								break

							if input_number == inf or isclose(0,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
								print(f"arctan({input_number}) = 0")
								break

							else:
								print(f"arctan({input_number}) = {final}")
								break

						elif MC == "b":
							print(f"arctan({input_number}) = {approx}")

						else:
							sys.exit(1)
					if TF == "vii":
						break
					
			if BC == "iii":
				break

	if GC == 3:
			
		while True:
			HC = str(input("""Choose a Trigonometric Operation : 
				i)   Hyperbolic functions
				ii)  Inverse hyperbolic functions
				iii) Exit\n"""))
	
			if HC == "i":
				while True:
					HF = str(input("""Choose a Hyperbolic function : 
					i)  sinh
					ii) cosh
					iii)tanh
					iv)cosech
					v) sech
					vi)coth
					vii)exit\n"""))

					input_number = float(input("Enter a number : \n"))

					if  HF == "i":
						ans=sinh(input_number)
						approx=round(ans,2)
						print(f"sinh({input_number}) = {approx} \n")

					if  HF == "ii":
						ans=cosh(input_number)
						approx=round(ans,2)
						print(f"cosh({input_number}) = {approx} \n")

					if  HF == "iii":
						ans=tanh(input_number)
						approx=round(ans,2)
						print(f"tanh({input_number}) = {approx} \n")

					if  HF == "iv":
						ans=cosech(input_number)
						approx=round(ans,2)
						print(f"cosech({input_number}) = {approx} \n")

					if  HF == "v":
						ans=sech(input_number)
						approx=round(ans,2)
						print(f"sech({input_number}) = {approx} \n")

					if  HF == "vi":
						ans=coth(input_number)
						approx=round(ans,2)
						print(f"coth({input_number}) = {approx} \n")

					if HF == "vii":
						break

			if HC == "ii":
				while True:
					HF = str(input("""Choose an Inverse hyperbolic function : 
					i)  arsinh
					ii) arcosh
					iii)artanh
					iv)arcosech
					v) arsech
					vi)arcoth
					vii)exit\n"""))

					input_number = float(input("Enter a number : \n"))

					if  HF == "i":
						ans=asinh(input_number)
						approx=round(ans,2)
						print(f"arsinh({input_number}) = {approx} \n")

					if  HF == "ii":
						ans=acosh(input_number)
						approx=round(ans,2)
						print(f"arcosh({input_number}) = {approx} \n")

					if  HF == "iii":
						ans=atanh(input_number)
						approx=round(ans,2)
						print(f"artanh({input_number}) = {approx} \n")

					if  HF == "iv":
						ans=acosech(input_number)
						approx=round(ans,2)
						print(f"arcosech({input_number}) = {approx} \n")

					if  HF == "v":
						ans=asech(input_number)
						approx=round(ans,2)
						print(f"arsech({input_number}) = {approx} \n")

					if  HF == "vi":
						ans=acoth(input_number)
						approx=round(ans,2)
						print(f"arcoth({input_number}) = {approx} \n")

					if HF == "vii":
						break

	if GC == "iv":

		while True:
			CC = str(input("""Choose a Conversion Operation : 
				i)   Number systems
				ii)  Temperature
				iii) Angles
				iv)  Exit\n"""))
	
			if CF == "i":
				while True:
					HF = str(input("""Choose a conversion function : 
					i)  binary to decimal
					ii) binary to octal
					iii)binary to hexadecimal
					iv)decimal to binary
					v) decimal to octal
					vi)decimal to hexadecimal
					vii)decimal to other 
					viii) octal to hexadecimal \n"""))
					






				

					

		
		
                                                            
					
	
		
		
