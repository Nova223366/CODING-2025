def shutdown(user_input):
    if user_input == "Yes":
        print("Shutting down")
    elif user_input == "No":
        print("Abort shutdown")
    else:
        print("Sorry")

# Take input from user
user_choice = input("Do you want to shutdown? (Yes/No): ")

# Call the function
shutdown(user_choice)