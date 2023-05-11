def fizz_buzz(max_num, fizz_value, buzz_value):
  fizz_buzz_list = []  
  for num in range(1, max_num + 1):
        if num % fizz_value == 0 and num % buzz_value == 0:
            fizz_buzz_list.append('FizzBuzz')
        elif num % fizz_value == 0:
            fizz_buzz_list.append('Fizz')
        elif num % buzz_value == 0:
            fizz_buzz_list.append('Buzz')
        else:
            fizz_buzz_list.append(num)
  print(fizz_buzz_list)
def intCheck(inputVar):
  isInt = False
  while not isInt:
    if inputVar.isdigit():
      return int(inputVar)
    else:
      inputVar = input("That was not a positive integer! Please enter the positive integer you intended: ")
      
def inputPrompt(funcVariable):
  match funcVariable:
    case "max_num":
      funcVariable = input("Enter the maximum number of the range you'd like to analyze:  ")
      return intCheck(funcVariable)
    case "fizz_value":
      funcVariable = input("Enter the factor you want replaced with 'Fizz': ")
      return intCheck(funcVariable)    
    case "buzz_value": 
      funcVariable = input("Enter the factor you want replaced with 'Buzz': ")
      return intCheck(funcVariable)

def continuePrompt():
    while True:
        response = input("Would you like to try it again? Type 'y' for yes and 'n' for no: ")
        if response == "y":
            return True
        elif response == "n":
            return False
        else:
            print("That was not a valid answer.")

willContinue = True
while willContinue:
  print("This is a function that analyzes a range for two different factors. You will enter a maximum number for a range that starts at 0, and the two factors you'd like to tag. The first factor will be replaced with the word 'Fizz' and the second factor will be replaced with the word 'Buzz'. If the number in the range has both factors, it will be replaced with 'FizzBuzz'. Enjoy!")
  fizz_buzz(
    inputPrompt("max_num"),
    inputPrompt("fizz_value"),
    inputPrompt("buzz_value")
  )
  willContinue = continuePrompt()
  
print("Thank you for trying my code!")
