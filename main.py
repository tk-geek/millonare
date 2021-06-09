print (" hello who wants to be a millonaire?")
print()

def play():
  money = 0
  q1 = input ( " What is the Capital in California ") 
  if (q1== "Sacramento " or   q1 == "sacramento"  ):
    money = money + 100
    print (" you have" , money ,  " dollars")
  else:
    print (" that is incorrect")
play()