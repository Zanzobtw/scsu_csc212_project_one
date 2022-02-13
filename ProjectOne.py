# step one
#   read file line by line -> figure out how to do this
# step one.five
#   split the line on "," to get the key and value for the line
# step one.seven_five
#   dictionary[key] = value
# step one.eight_two_five
#   go back to step one.five

# Phase One

state_capitals = open("state_capitals.txt", "r")

state_capitals_dict = {}

capitals_line = state_capitals.readline()

while capitals_line != '':
    capitals_line = capitals_line.rstrip()
    capitals_line = capitals_line.split(",")
    key = capitals_line[1].strip()
    value = capitals_line[0].strip()
    state_capitals_dict[key] = value
    capitals_line = state_capitals.readline()

user_input = input("Do you want to start, yes or no? " )

while user_input.lower() != 'yes' and user_input.lower() != 'no':
    user_input = input("Do you want to start, yes or no? " )

while user_input.lower() == "yes" and user_input.lower() != "no":
    state_input = input("Enter a state, I will output the capital. ")
    print(state_capitals_dict[state_input.title()])
    user_input = input("Do you want to continue, yes or no? " )
    while user_input.lower() != 'yes' and user_input.lower() != 'no':
        user_input = input("Do you want to continue, yes or no? " )

states_list = state_capitals_dict.keys()
states_list = list(states_list)
