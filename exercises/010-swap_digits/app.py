#Complete the fuction to return the swapped digits of a given two-digit-interger.
def swap_digits(num):
  # Your code here
  num1 = num // 10
  num2 = num % 10
  concatenated = str(num2) + str(num1)
  return concatenated
   
#Invoke the function with any two digit interger as its argument
print(swap_digits(30))
