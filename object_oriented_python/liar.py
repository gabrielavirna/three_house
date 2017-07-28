"""Now I want you to make a subclass of list. Name it Liar. Override the __len__ method so that it always returns the 
wrong number of items in the list. For example, if a list has 5 members, the Liar class might say it has 8 or 2.
You'll probably need super() for this."""


class Liar(list):
    def __len__(self):
        wrong_len = super().__len__()
        wrong_len += 3
        return wrong_len

lr = Liar([1, 2, 3])
print(lr, len(lr))

