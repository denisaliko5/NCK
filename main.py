num = int(input("Enter a number of elements: "))
num1 = int(input("Enter a number of possible arrangements: "))
def factorial(f_num):
  f_num1 = f_num
  times = 1
  while times < f_num1:
    f_num *= times
    times += 1
  return f_num
def nCk():
  print(factorial(num)/(factorial(num1)*(factorial(num-num1))))
if num1 < num:
  nCk()
elif num1 == num:
  print(factorial(num))