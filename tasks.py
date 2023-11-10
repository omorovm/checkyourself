# first task
class AutoMixin:
    def ride(self):
        print("Riding on a ground")

class BoatMixin:
    def swim(self):
        print("Floating on water")

class Amphibian(AutoMixin, BoatMixin):
    pass

obj = Amphibian()
obj.ride()
obj.swim()

# second task

class ContactList(list): 
    def __init__(self, list_): 
        self.list_ = list_ 
    def search_by_name(self, name): 
        a = [i for i in self.list_ if name in i] 

        return a 

all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
print(all_contacts.search_by_name('Olya'))