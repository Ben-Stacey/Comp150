def rate_movie(movie, rate):
    print("Movie: ",  movie,  "; Your rating: ", rate, " ", get_stars(rate), ".")

def age(name, current_age):
    print("Hello ", name, ", you are ", current_age, " years old.")
    print("Next year you will be ", current_age + 1, ".")
    
def get_stars(rate):
    if rate == 0:
        print("BOMB!")
    elif rate == 1:
        print("Bad")
    elif rate == 2:
        print("Below average")
    elif rate == 3:
        print("Average")
    elif rate == 4:
        print("Good")
    elif rate == 5:
        print("Must See")
    
rate_movie("The Meaning of Life", 4)
age("Eric", 67)