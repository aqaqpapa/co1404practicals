Name_to_Email={}
emails=input("Emails: ")
while emails!="":
    full_name=emails.split("@")[0]
    first_name=full_name.split(".")[0]
    last_name=full_name.split(".")[1]
    answer = input(f"Is your name {first_name} {last_name}? (Y/N)")
    if answer.upper()=="Y":
        Name_to_Email[full_name]=emails
        emails = input("Emails: ")
    else:
        full_name=input("Name")
        Name_to_Email[full_name] = emails
        emails = input("Emails: ")
for Name,Email in Name_to_Email.items():
    print(f"{Name} ({Email})")