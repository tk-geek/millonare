print (" hello who wants to be a millonaire?")
print()

def play():
  money = 0
  q1 = input ( " What is the Capital in California? ") 
  if (q1== "Sacramento" or   q1 == "sacramento"  ):
    money = money + 100
    print (" you have" , money ,  " dollars")
  else:
    print (" that is incorrect")
  q2 = input ("what is 20+2? ")
  if (q2=="22") :
    money = money + 100
    print("you have", money , " dollars ")
  else:
    print("that is incorrect ")
  q3 = input ("how many ears do you have? ")
  if (q3== "2"):
   money=money+100
   print("you have",money,"dollars") 
  else:
    print ("that is wrong")
  q4=input ("how many wheels does a car have? ")
  if(q4 == "4") :
    money = money + 100
    print("you have",money, "dollars ")
  else:
    print("that is wrong ")
  q5=input ("how many chips  do i have in my mouth😁? ")
  if(q5==6):
    money=money+100
    print("you have",money,"dollars")
  else:
    print("thats wrong")
play()