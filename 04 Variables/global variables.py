a = "awesome"

def myfunc():
  a = "fantastic"
  print("Python is " + a)

myfunc()
print("Python is " + a)



x = "awesome"
def myfunc():
  global x
  x = "fantastic"
  print("Python is " + x)   # use global keyword

myfunc()

print("Python is " + x)