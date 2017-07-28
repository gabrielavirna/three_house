"""I want you to add a __str__ method to the Letter class that loops through the pattern attribute of an instance and 
returns "dot" for every "." (period) and "dash" for every "_" (underscore). Join them with a hyphen.

 Add an __iter__ method to the Letter class so the letter's pattern can be iterated through. You'll want to use yield 
 or yield from. Do not convert the pattern to dots and dashes in __iter__.
 
 Let's practice using @classmethod! Create a class method in Letter named from_string that takes a string like 
 "dash-dot" and creates an instance with the correct pattern (['_', '.']).
 """


class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern

    def __str__(self):
        output = []
        for c in self:
            if c == '.':
                output.append('dot')
            elif c == '_':
                output.append('dash')
        return "-".join(output)

    def __iter__(self):
        # for item in self.pattern:
        #     yield item
        yield from self.pattern

    @classmethod
    def from_string(cls, string):
        string_list = string.split('-')
        pattern_list = []
        for item in string_list:
            if item.lower() == 'dash':
                pattern_list.append('_')
            elif item.lower() == 'dot':
                pattern_list.append('.')
            else:
                pass
        return cls(pattern_list)


class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)


s = S()
print(s.__str__())

l = Letter().from_string("dash-dot-dash")
print(l)
