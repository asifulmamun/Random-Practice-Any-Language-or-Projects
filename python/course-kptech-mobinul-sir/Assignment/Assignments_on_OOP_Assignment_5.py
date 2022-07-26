""" Scene 1:- """
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
class GenderGreat(User):
    def gender_great(self, gender):
        if gender == 'Male':
            print('Hello Mister ', self.first_name, ' ', self.last_name)
        else:
            print('Hello Lady ', self.first_name, ' ', self.last_name)
# Male Call
gg = GenderGreat('Al', 'Mamun')
gg.gender_great('Male')
# Lady Call
gg = GenderGreat('Jennifer', 'Lawrence')
gg.gender_great('Female')


""" Scene 2:- """

class Admin():
    def __init__(self, admin_name):
        self.admin_name = admin_name

    def add_post(self):
        print('Admin Add Post ', self.admin_name)

    def view_post(self):
        print('Admin View Post ', self.admin_name)
    
    def delete_post(self):
        print('Admin Delete Post ', self.admin_name)

class NewUser(Admin):
    def create_post(self):
        print('Child Create Post ', self.admin_name)

    def view_post(self):
        print('New User View Post ', self.admin_name)

user = NewUser('Mamun')
user.add_post()
user.view_post()
user.delete_post()