import random

dice = [1, 2, 3, 4, 5, 6]

def normalmode():
    while True:
        rolled = random.choice(dice)
        print(f"\nYou rolled: {rolled}")
        
        choice = input("Want to roll again (1) or exit to main menu (2)? ")
        if choice == "1":
            continue
        elif choice == "2":
            break
        else:
            print("Invalid input. Please enter 1 or 2.")

def cheatmode():
   
   try:
    choice = int(input("Enter a number between 1 and 6 which you want to repeat the most: "))
    if choice not in dice:
        print("Invalid choice.")
   except ValueError:
      print("Please enter a valid number.")
   biased_list=dice.copy()
   biased_list+=[choice]*10
   while True:
      rolled = random.choice(biased_list)
      print(f"\nYou rolled: {rolled}")
      options = input("\nWant to roll again (1) or exit to main menu (2)? ")
      if options == "1":
        continue
      elif options == "2":
        break         
      else:    
        print("Invalid input. Please enter 1 or 2.")

def main():
   while True:
      print("\nWelcome To The DICE simulator!!!")
      print("1.Normal Mode")
      print("2.Cheat Mode")
      print("3.Exit")
      choice=input("\nEnter your choice(1,2,3):")
      if choice=='1':
         normalmode()
      elif choice=='2':
         cheatmode()
      else:
         break
main()

   




  


    

    


