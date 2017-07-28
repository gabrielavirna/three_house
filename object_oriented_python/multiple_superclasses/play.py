from object_oriented_python.multiple_superclasses.thieves import Thief
from object_oriented_python.multiple_superclasses.characters import Character

kenneth = Thief(name="Kenneth", sneaky=False)

print(kenneth)
print(kenneth.sneaky)
print(kenneth.agile)
print(kenneth.hide(8))
print("\n")

print(issubclass(Thief, Character))
kenneth = Thief(name="Kenneth")
print(type(kenneth))
print("\n")

print(kenneth.__class__)
print(kenneth.__class__.__name__)
