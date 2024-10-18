aura= 0

# question 1:
answer = input("would you rather A) play fortnite, or B) not play fortnite?")
if answer == "A":
	aura += 100
elif answer == "B":
    aura -= 100

# question 2:
answer2 = input("do you like A) ksi new song, or B) not like ksi new song? or c) do you listen to talk tuah?")
if answer2 == "A":
	aura-= 100
elif answer2 == "B":
	aura += 100
elif answer2 == "c":
    aura += 300
# question 3:
answer3 = input("would you rather A) work for elon musk, or B) be elon musk?")
if answer3 == "A":
	aura -= 100
elif answer3 == "B":
	aura += 100
	
if aura > aura:
	print("you have aura")
elif aura > aura:
	print("You have negative aura")


