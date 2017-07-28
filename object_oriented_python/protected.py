""" locking information away, instead of hiding - nothing's totally locked away in python
_dont_use - if you don't want people to use this attribute or method
__dont_use - you cannot get to them- better protected"""


class Protected:
    __name = "Security"

    def __method(self):
        return self.__name

prot = Protected()
print(dir(prot))
print(prot._Protected__method())
print(prot._Protected__name)

