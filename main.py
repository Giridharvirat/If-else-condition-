print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120 :
 print("you can ride")
 age = int(input("what is your age?"))
 if age <=12 :
   bill = 5
   print("child ticket $5.")
 elif age <= 18 :
   bill = 7
   print(" youth ticket $7.")
 else :
   bill = 8
   print("adult ticket $8.")   
 
 wants_photo = input( " do you wnat a pic? Y 0r N")
 if wants_photo == "Y" :
   bill += 3
  
 print(f" your final bill is ${bill}")

else :
 print("you can't ride")

