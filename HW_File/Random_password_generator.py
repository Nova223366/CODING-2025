import random
import string
print("Welcome to Random password generator! ")
print("this can make password above to 62 characters lenths (last limit).")
print("Make lowercase, uppercase and digits.""\n")
want = input("Do you want to generate an random password? (yes/no): ").lower()
if want == 'yes':
    while want == 'yes':
        def password_generator(length):
            lowercase = string.ascii_lowercase
            uppercase = string.ascii_uppercase
            digits = string.digits
            all_characters = lowercase + uppercase + digits 
            password_list = random.sample(all_characters, length)
            random.shuffle(password_list)
            return ''.join(password_list)
        length = int(input("Enter the length of the password you want: "))
        password = password_generator(length)
        print("Generated password is:""\n\n\t", password,"\n")
        want = input("Do you want to generate another password? (yes/no): ").lower()
    else:
        print("If you want you can use it later. Goodbye!")
else:
    print("Okay, have a nice day!")