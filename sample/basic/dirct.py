

scoreDir = { "Li Lei": 99,
             "Han Meimei": 100,
             "Lucy": 90,
             "Jim": 80,
             "Lin Tao": 97,}


print(scoreDir["Li Lei"])
print(scoreDir["Lin Tao"])
print(scoreDir["Jim"])

print(scoreDir.get("Han Meimei"))

print(len(scoreDir))

## for invalid non exist
print(scoreDir["Lily"])