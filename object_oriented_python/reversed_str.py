"""Subclassing Built-ins"""


class ReversedStr(str):
    # strings are immutable - we should change it only at creation time
    def __new__(*args, **kwargs):
        self = str.__new__(*args, **kwargs)
        self = self[::-1]
        return self


rs = ReversedStr('hello')
print(rs, len(rs))

