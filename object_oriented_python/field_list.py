import copy

class FieldList(list):
    def __init__(self, count, value, *args, **kwargs):
        super().__init__() # creates a new empty list instance
        for _ in range(count): # ignores the value of count
            self.append(copy.copy(value)) # appends copies to get new versions of the list instead of references

fl = FieldList(9, 2)
print(len(fl), fl)
fl2 = FieldList(2, [1, 2, 3])
print(fl2)
fl2[0][1] = 5
print(fl2)


