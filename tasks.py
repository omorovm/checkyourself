# first task

class CreateMixin:
    def create(self, todo, key):
        if key in self.todos.keys():
            return "Задача под таким ключом уже существует"
        self.todos[key] = todo
        return self.todos

class DeleteMixin:
    def delete(self, key):
        return self.todos.pop(key,1111)


class UpdateMixin:
    def update(self, key, new_value):
        self.todos[key] = new_value
        return self.todos
class ReadMixin:
    def read(self):
        return sorted(self.todos.items())

class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin): 
    todos = {}

    def set_deadline(self, date):
        import datetime
        date = date.split('/')
        date_now = datetime.datetime.now()
        date = datetime.datetime(int(date[2]), int(date[1]), int(date[0]))
        return -(date_now - date).days

# second task

class Person:
    def __init__(self, name = None, last_name = None, age = None, email = None) -> None:
        self._name = name
        self._last_name = last_name
        self._age = age
        self._email = email
    
    @property
    def name(self):
        return self._name
    
    @property
    def last_name(self):
        return self._last_name
    
    @property
    def age(self):
        return self._age
    
    @property
    def email(self):
        return self._email
    
    @name.setter
    def name(self, a):
        self._name = a

    @last_name.setter
    def last_name(self, a):
        self._last_name = a

    @age.setter
    def age(self, a):
        self._age =  a

    @email.setter
    def email(self, a):
        self._email = a

john = Person()
print(john.name) # None
print(john.last_name) # None
print(john.age) # None
print(john.email) # None
john.name = 'John'
john.last_name = 'Snow'
john.age = 30
john.email = 'johnsnow@gmail.com'
print(john.name) # John
print(john.last_name) # Snow
print(john.age) # 30
print(john.email) # johnsnow@gmail.com

# third task

class Dog:
    def voice(self):
        print('Гав')

class Cat:
    def voice(self):
        print('Мяу')

def to_pet(pet):
    pet.voice()

barsik = Cat()
rex = Dog()
to_pet(barsik)
to_pet(rex)
        

