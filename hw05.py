"""
Name: (Abigail Gladstone)
Peers: (add any collaborators)
References: (anything you checked to solve this)
"""

def get_letter():
    """ This function will get an input from the user, then tnhat input is checked to make sure it follows the parameters, if it doesnt the loop will repeat"""
    let = input("Give an single uppercase letter: ")
    my_list = [ 65, 66, 67] #will be used for ascii values
    d = len(let)
    b = False
    while b == False:
        if d > 1:
            print("Error: it needs to be a single character.")
            let = input("Give an single uppercase letter: ")
            d = len(let) #makes sure the input is only a single letter each time
            continue
        elif ord(let) in my_list:
            b = True
        else:
            print("Error: You provided the wrong character.")
            let = input("Give an single uppercase letter: ")
            d = len(let)
    return let #lets main() access this value

    

def get_digit():
    """ gets a digit from the user,  makes sure this digit is in the correct range. if not the loop will continue till a correct digit is inputed"""
    num = input("Give an single number character: ")
    my_num_list = [ "1", "2", "3"] #list of correct numbers
    while True:
        if num.isdigit() == False: # makes sure only a number was inputed 
            print("Error: your input should be only digits.")
            num = input("Give an single number character: ")
            continue
        elif num not in my_num_list:
            print("Error: a single digit needs to be in [1,3].")
            num = input("Give an single number character: ")
            continue
        else:
            break #exits the loop
            
    
    return num #lets main access this variable


def check_pattern(letter, digit, lst):
    """ takes the correct inouts from the user, and matches it with words in the list"""
    s = 0
    print("Strings with the pattern:")
    for i in lst: # i runs through every word in the list
        if letter in i and digit in i:
            if i.index(letter) < i.index(digit):
                print(lst[s], end=" ") #makes sure they all go on the same line
                s +=1 # moves to the next item
            else:
                s +=1
        else:
            s +=1 #moves to the next item
    print()
    


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
    false = False
    while false == False:
        let = get_letter()
        num = get_digit()
        check_pattern(let, num, st_list)
        ask_user = input("Try Again? (y/n): ")
        while ask_user == "y":
            let = get_letter()
            num = get_digit()
            check_pattern(let, num, st_list)
            ask_user = input("Try Again? (y/n): ")
            if ask_user == "y":
                continue
            else:
                false = True
                ask_user == "n"
                break
                
        
        
            


    # -------------------------------------------------
    # No need to modify anything Below this line
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()