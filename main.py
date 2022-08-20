from DBhelper import  DBrelation

def main():
    db= DBrelation()
    while True:
        print("**********WELCOME*********")
        print("Press 1 to insert new user")
        print("Press 2 to display all users")
        print("Press 3 to delete user")
        print("Press 4 to update user")
        print("Press 5 to exit program")
        print("\n")

        try:
            choice=int(input())

            if(choice==1):
                uid = int(input("Enter userId: "))
                userName  = input("Enter userName: ")
                Phone = input("Enter user Phone no: ")
                email = input("Enter usermail: ")
                db.insert_user(uid,userName,Phone,email)

            elif (choice == 2):
                db.Fetch_all()

            elif (choice == 3):
                userId = int(input("Enter user id which you want to delete: "))
                db.delete_user(userId)

            elif (choice == 4):
                uid = int(input("Enter userId: "))
                userName = input("Enter new userName: ")
                Phone = input("Enter new user Phone no: ")
                email = input("Enter new usermail: ")
                db.update_user(uid,userName,Phone,email)

            elif (choice == 5):
                break

            else:
                print("invalid input, try again!")

        except Exception as e:
            print(e)
            print("invalid details, try again!")

if __name__ == "__main__":
    main()

