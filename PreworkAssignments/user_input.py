user_input = int(input("Please Enter Your Age as of Today: "))

# Created a user input and start of the if  
if user_input <= 10:
    print("""Hey there pal/gal! We know you want to play Death Rangers, 
but ya gotta be 13! Your parent can sign for you if you can't wait 
and then have fun young duck!""")

elif 11 <= user_input < 18: # Conditional checking input
    print("Looks like you can come in on a teen pass, have fun!")

elif user_input >= 21:
    print("Oh cool, you can buy adult juice")

else:
    print("Congrats! you are an adult. Allegedly!") # Default print state just in case

