from cryptography.fernet import Fernet


#def write_key():
    #key = Fernet.generate_key()
    #with open("key.key", 'wb') as key_file:
      #  key_file.write(key)

def load_key():
    file = open("key.key", "rb")
    key = file.read ()
    file.close()
    return key



master_password = input("What is the master password? ")
key = load_key() + master_password.bytes
fer = Fernet(key)


def view():
    with open('password.txt', 'r') as f:
        data = f.readlines()[0].strip()
        user, passw = data.split("|")[0], data.split("|")[1]
        print("User:", user, "Password:", passw)
        print(data)


def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + "|" + pwd + '\n')

while True:
    mode = input("Would you like to add a new password or view existing ones? (view, add and q to quit): ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invalid mode.")
        continue
