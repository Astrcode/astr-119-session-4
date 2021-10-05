#python exceptions let you deal with unexpected results

try:
	print(a)	#this'll throw an exception since a isn't defined
except:
	print("a is not defined!")

#there are specific error to help with cases
try:
	print(a)	#this'll throw an exception since a isn't defined
except NameError:
	print("a is still not defined!")
except:
	print("Something else went wrong.")

#this will break our program since a isn't defined
print(a)

'''
This code will deal with problems as they occur
'''