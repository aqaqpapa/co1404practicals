CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}


print(CODE_TO_NAME)
output=[]
state_code = input("Enter short state: ").upper()

while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
        output.append(state_code)
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
for code in output:
    print(f"{code:4} is   {CODE_TO_NAME[code]}")