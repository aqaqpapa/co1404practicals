with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
 in_file.readline()
 Name_to_Number={}
 Contry_to_Champion={}
 for line in in_file:
    infor=line.strip().split(",")
    Contry_to_Champion[infor[1]] = 1
    try:
        Name_to_Number[infor[2]]+=1

    except KeyError:
        Name_to_Number[infor[2]]=1



 print("Wimbledon Champions: ")
 for Name,Number in Name_to_Number.items():
     print(f"{Name} {Number}")

 Num=len(Contry_to_Champion)
 print(f"These {Num} countries have won Wimbledon: ")
 for Contry in Contry_to_Champion.keys():
     print(Contry,end=", ")