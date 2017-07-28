"""Make a class named Double that extends int. For now, just put pass inside the class.
Now override __new__. Create a new int instance from whatever is passed in as arguments and keyword arguments. 
Return that instance. You should remove the pass. And, finally, double (multiply by two) the int that you created 
in __new__. Return the new, doubled value. For example, Double(5) would return a 10.
"""


class Double(int):
    def __new__(*args, **kwargs):
        self = int.__new__(*args, **kwargs)
        self *= 2
        return self