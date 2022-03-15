def greet(name):
    print("good day, "+ name)

a = greet("smit")


# is case me name ki jagah par smit aa gaya par agar smit na ho aur khali () aise ho to 
# programme error throw karega, par hum default argument set karde, it means ki hum uper
# hi name ki jagah par kuch likh de to error nahi ayega.
#ex: def greet(name="stranger") abhi age hum khali () rakhenge to koi error nahi ayega.

def greet(name = "stranger"):
    print("good day, "+ name)

a = greet()

