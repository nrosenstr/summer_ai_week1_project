#########WHEN TYPING A NUMBER IN THE INNERMENU YOU HAVE TO TYPE IT TWICE FOR IT TO WORK
# Various import statements can go here

from social_network_classes import SocialNetwork
import social_network_ui

# Create instance of the main social network object
ai_social_network = SocialNetwork()

# The line below is a python keyword to specify which
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()
    currentfriends = []
    blocked = ""
    messegesNathan = ""
    messegesMary = ""
    messegesFromNathan = "Nathan: Hi, nice to meet you!"
    messegesFromMary = "Mary: Hope you are having a good day today!"
    
      
    while True:
        if choice == "1":
            inner_menu_choice = social_network_ui.manageAccountMenu()

            # Handle inner menu here
            while True:
                if inner_menu_choice == "8":
                    break
                elif inner_menu_choice == "1":
                    account_details = input("Please enter your new username and password here:")
                    newVar = input(f'Here is your current username and password: {account_details} type y if that is correct and n if it is incorrect')
                    if newVar == 'y':
                        # Bring the user back to the inner menu options
                        inner_menu_choice = social_network_ui.manageAccountMenu()
                    elif newVar == 'n':
                        account_details = input("Please enter your new username and password here:")
                    else:
                        print("Please enter one of the following letters: n y")
                elif inner_menu_choice == "2":
                    friendlist = input("Here is your current friends list: Nathan, Mary. Please type the name of the person you would like to add as a friend")
                    if friendlist == "Mary":
                        currentfriends.append("Mary")
                        inner_menu_choice = social_network_ui.manageAccountMenu()
                    elif friendlist == "Nathan":
                        currentfriends.append("Nathan")
                        inner_menu_choice = social_network_ui.manageAccountMenu()
                    else:
                        print("You did not enter the name of anyone on your friends list")

                elif inner_menu_choice == "3":
                    if currentfriends:
                        print(f'Here is your current list of people added: {", ".join(currentfriends)}')
                    else:
                        print("Your friends list is empty.")
                elif inner_menu_choice == "4":
                    blocked = input(f'If you would like to block {currentfriends}, type their name')
                    if blocked in currentfriends:
                        currentfriends.remove(blocked)
                        print(f"{blocked} has been blocked.")
                    else:
                        print(f"{blocked} is not in your friend list.")
                elif inner_menu_choice == "5":
                    messeges = input(f'Here are your current friends: {currentfriends}. Type the name of the person you would like to message')
                    if messeges == "Nathan":
                        messegesNathan = input("type the messege you would like to send to Nathan here:")
                    elif messeges == "Mary":
                        messegesMary = input("type the messege you would like to send to Nathan here:")

                    else:
                        print("The person you entered is not in your friendslist")

                elif inner_menu_choice == "6":
                    whichMesseges = input(f'Here are your current friends: {currentfriends}. Type the name of the friend you would like to check messeges you have recieved from them.')
                    if whichMesseges == "Mary":
                        print(messegesFromMary)
                    elif whichMesseges == "Nathan":
                        print(messegesFromNathan)
                    else:
                        print("The person you entered is not in your friendslist")
                elif inner_menu_choice == "7":
                    sentMessage = input(f'Here are your current friends: {currentfriends}. Type the name of the friend you would like to see message you sent')
                    if sentMessage == "Mary":
                        print(messegesMary)
                    elif sentMessage == "Nathan":
                        print(messegesNathan)
                    else:
                        print("The person you entered is not in your friendslist")

                
                else:
                    print("Your input is invalid. Try Again!")

                
                    
                

                inner_menu_choice = social_network_ui.manageAccountMenu()

        elif choice == "2":
            print("Thank you for visiting. Goodbye!")
            break

        else:
            print("Your input is invalid. Try Again!")

        # Restart menu
        choice = social_network_ui.mainMenu()
