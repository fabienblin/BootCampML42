from vector import Vector

v1 = Vector([4.0, 1.0, 2.0, 3.0])
v2 = Vector(4)
v3 = Vector((5, 10))

print("v1=", v1)
print("v2=", v2)
print("v3=", v3)
print("\n")

print("v1+v2=", v1+v2)
print("v1-v2=", v1-v2)
print("v1*v2=", v1*v2)
print("v2/v1=", v2/v1)
print("\n")

# commented = Error

# print("v1+1=", v1+1)
# print("v1-1=", v1-1)
print("v1*2=", v1*2)
print("v1/2=", v1/2)
print("\n")

# print("1+v1=", 1+v1)
# print("1-v1=", 1-v1)
print("2*v1=", 2*v1)
# print("2/v1=", 2/v1)
print("\n")

# print("v1/0="v1/0)
# print("v1+'a'", v1+"a")

print("str(v1)=", str(v1))
print("repr(v1)=", repr(v1))
