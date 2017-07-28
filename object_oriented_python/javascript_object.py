"""look up keys with a dot"""


class JavaScriptObject(dict):
    def __getattribute__(self, item):
        try:
            return self[item]
        except KeyError:
            return super().__getattribute__(item)

jso = JavaScriptObject({'name':'Kenneth'})
jso.language = 'Python'
print(jso.language, jso.name)
