"""
Name: (Abigail Gladstone)
Peers: (add any collaborators)
References: (anything you checked to solve this)
"""

def get_letter():
    """ Add your own Docstring """
    let = input("Give an single uppercase letter: ")
    my_list = [65, 66, 67]
    d = len(let)
    b = False
    while b == False:
        if d > 1:
            print("Error: it needs to be a single character.")
            let = input("Give an single uppercase letter: ")
            d = len(let)
            continue
        elif ord(let) not in my_list:
            print("Error: You provided the wrong character.")
            let = input("Give an single uppercase letter: ")
            d = len(let)
            continue
        else:

            b == True
            break
        

    

    return let

def get_digit():
    """ Add your own Docstring """
    num = input("Give an single number character: ")
    my_num_list = [ "1", "2", "3"]
    while True:
        if num.isdigit() == False:
            print("Error: your input should be only digits.")
            num = input("Give an single number character: ")
            continue
        elif num not in my_num_list:
            print("Error: a single digit needs to be in [1,3].")
            num = input("Give an single number character: ")
            continue
        else:
            break
            
    
    return num


def check_pattern(letter, digit, lst):
    """ Add your own Docstring """
    # remove the default pass and add your code
    pass


#  The function main is INCOMPLETE, you must finish it
# before you submit
def main ():
    """ gets a letter-num pair and searches inside a list for matches"""

    # The list inside of which we will search the user pair (DO NOT MODIFY)
    # -------------------------------------------------
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]

    # TODO: Add your calls to get_letter, get_digit, and check_pattern
    # Inside a loop so that:
    #     After printing the results, a prompt appears requiring an input
    #          with the text: "Try Again? (y/n): "
    #     AND
    #          IF the user replies with 'y', the loop continues
    #          IF the user replies with anything else, the loop ends
    # ADD YOUR CODE UNDER THIS LINE
    # -------------------------------------------------

    get_letter()
    get_digit()

    # -------------------------------------------------
    # No need to modify anything Below this line
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()