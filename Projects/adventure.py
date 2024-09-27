#intro
print("welcome to the cat scavenger hunt!")
print("you are being assesed with a secret mission to FIND this cat")
print("make sure you chose the right options in order to save the cat!")


#start choice 1
s1 = input("would you like to [start] ?")
if "start" in s1 or "yes" in s1:
    print("alright")
    print("get ready!")

else:
    print("so you think your smart huh? you think your funny right?")



#choice 2
c2 = input("do you wanna start at the [house] or the [park] ?")
if "house" in c2:
    
    
    #choice 3
    print("you arrive at the house.")
    c3 = input("would you like to go to the [kitchen] or the [basement] ?")
    if "kitchen" in c3: 
        print("you go to the kitchen and find the cat!")
        print("YAY")
    else:
        #choice 4
        print("you go to the basement and find a mysterious door.")
        c4 = input("would you like to open the door?")
        if "yes" in c4:
            print("--------------------------------------------")
            print("theres a note behind the door. it says ")
            print("---------------------------------------------------")
            print("hey owner! i just left the basement to go to the kitchen. From:Your Cat")
            c5 = input("would you like to go there?[yes][no]")
            #choice 5
            if "yes" in c5:
                print("you found him!")
            else:
                #choice 6
                c6 = input ("why bro.[idk][i didnt want to][on skib]")
                if "idk" in c6:
                    print("your useless")
                
                elif "i didnt want to":
                    print("then why are you playing my game in the first place. your supposed to EXPLORE.")
                
                else:
                    print("how much tuah can a hawk tuah tuah if a hawk tuah could hawk tuah")
        
        else:
            print("bruh")

else:
    print("on your way to the park, you crash your car and die a horrible death.")
    print("just restart")