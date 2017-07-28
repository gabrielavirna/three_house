class Student:

    def __init__(self, name, **kwargs):
        self.name = name

        for key,value in kwargs.items():
            setattr(self, key, value)

    def praise(self):
        return "Hello, {}".format(self.name)

    def reassurance(self):
        return "Chin up, {}. You'll get it next time!".format(self.name, )

    def feedback(self, grade):
        if grade > 50:
            return self.praise()
        return self.reassurance()


me = Student("Gabriela")
print(me.name)
print(me.praise())
print(me.feedback(40))