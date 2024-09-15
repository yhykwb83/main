def OnlineStore():
  print("------------------------")
  item_a = 200.0
  item_b = 400.0
  item_c = 600.0
  print("Online Store")
  print("------------------------")
  print("Product(S)" + " "*15 + "Price")
  print("Item1" + " "*20, item_a)
  print("Item2" + " "*20, item_b)
  print("Item3" + " "*20, item_c)
  print("Combo 1(Item 1 + 2)" + " "*6, (item_a + item_b)*0.9)
  print("Combo 2(Item 2 + 3)" + " "*6, (item_b + item_c)*0.9)
  print("Combo 3(Item 1 + 3)" + " "*6, (item_a + item_c)*0.9)
  print("Combo 4(Item 1 + 2 + 3)" + " "*2, (item_a + item_b +  item_c)*0.75)
  print("------------------------")
  print("For Delivery Contact:98764678899")

OnlineStore()

def greet(name):
  print( "Hello," + name + "!") 

greet("Tom")

def print_twice(name):
  greet(name)
  friend = "Mike"
  greet(friend)
  greet(name +" and " +friend)

print_twice("Jim")

def show_parameter(para):
  print("parameter is", para)

show_parameter(10)

y = 20

def shadowing_example():
    y = 10  # Local variable with the same name as the global variable
    print("Inside the function:", y)

shadowing_example()
print("Outside the function:", y)