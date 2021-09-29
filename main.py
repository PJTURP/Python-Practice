#Homemade dictionary
def define(word):

    #word lowercase
    word = word.lower()

#1
    if word=="school":
        return "A place of learning"
#2
    elif word=="starwars":
        return "A place far far away a long time ago"
#3
    elif word=="racoon":
        return "Trash panda"
#4  
    elif word=="v8":
        return "An 8 cylinder driven engine in a V configuration"
#5
    elif word=="minecraft":
        return "A perfect chieldhood"
#6
    elif word=="Pencil":
        return "A wood writing untencil"
#7
    elif word=="Homework":
        return "A teachers good idea"
#8
    elif word=="Landmine":
        return "The fordiden Tuna"
#9
    elif word=="Dictionary":
        return "A book with no pictures"
#10
    elif word=="Car Parts":
        return "The ability to buy happiness"
#11
    else:
        return "Your word dose not exist, leave."


#run dictionary
print(define("lol"))