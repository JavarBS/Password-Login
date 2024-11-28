print("Welcome, Please sign in.")
print()

username = input("Username: ")
password = input("password: ")
print ()

if username == "Jack" and password == "J@ck":
  playGame = input("Welcome Jack! Do you want to play a game? (Y/N) ")
  if(playGame == "Y"):
      print("Okay, lets play!")
  else:
    print("Okay, maybe next time.")

elif username == "Jill" and password == "J@ll":
  print("Welcome Jill!")
  print("Hope you have a great day!")

elif username == "Jane" and password == "J@ne":
  print("Welcome Jane!")
  answer = input("How are you today, feeling great? ")
  if(answer == "Yes"):
    print("Amazing!")
  else:
    print("I hope your day gets better!")

else:
  print("Incorrect username or password.")