def my_function():
    print ("Hello from a function")

def my_function():
    print ("Hello from a function")
my_function()

print ""

def my_function(fname):
    print (fname+"Refsnes")
my_function("Email",)
my_function("Tobias",)
my_function("Linus",)

print ""

def my_function(country = "Norway"):
    print ("I am from" + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

print ""

def my_function(food):
    for x in food:
        print (x)
friuts = ["apple","banana","cherry"]
my_function(friuts)

print ""
def my_function(x):
    return 5 * x
print (my_function(3))
print (my_function(5))
print (my_function(9))

def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)