CODE_TO_COLOR={
    "absoulute zero": "#0048ba",
    "acid green": "#b0bf1a",
    "alice blue": "#f0f8ff",
    "amber": "#ffbf00",
    "methyst":"#9966cc",
    "Aqua":"#00ffff",
    "Army Green":"#4b5320",
}
print(CODE_TO_COLOR)
color_code_original=input("Enter Color:")
color_code=color_code_original.lower()
output=[]

while color_code !="":
    try:
        print(color_code_original ,"is",CODE_TO_COLOR[color_code])
        output.append(color_code_original)
    except KeyError:
        print("Invalid Color")
    color_code_original = input("Enter Color:")
    color_code = color_code_original.lower()
for color in output:
    print(f"{color:10} is {CODE_TO_COLOR[color]}")