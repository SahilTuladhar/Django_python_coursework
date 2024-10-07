newUsername = input("Enter New Username:")
newPassword = input("Enter New Password:")
confirmPassword = input("Re-Enter Password:")



class newUser: 

    def __init__(self , username , password , checkpassword) -> None:

        self.un = username
        self.pw = password
        self.re = checkpassword

    def checkPassword(self):

        if self.pw == self.re:
            print("Account Successfully Created")
        else:
            print("Password not Validated")


class userLogin(newUser):
    def __init__(self, username, password, checkpassword , loginusername , loginpassword ) -> None:
        super().__init__(username, password, checkpassword)
        self.luser = loginusername
        self.lpass = loginpassword
    
    def checkAccess(self):
        if self.un == self.luser and self.pw == self.lpass:
            print("Logged In Successfully")
        else:
            print("Credentials Incorrect....Please Try Again")
        

u1 = newUser(newUsername , newPassword , confirmPassword )
u1.checkPassword()

loginUsername = input("Enter Username:")

loginPassword = input("Enter Password:")


u2 = userLogin(newUsername , newPassword , confirmPassword , loginUsername , loginPassword)
u2.checkAccess()
