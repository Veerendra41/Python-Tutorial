d = {
    "Name": "Veeru",
    "Place": "Vijayawada",
    "College": "JNTUK"
}
if "Name" in d:
    print("Name is present in the dictionary")
for key, value in d.items():
    print(key, value)
print(d.keys())
print(d.values())
print(d.items())    
print(d["Name"])
print(d.get("Place"))