name=input("Enter name:")
print("(H)ello""\n""(G)oodbye""\n""(Q)uit")
c=input(">>> ")
while c!="Q":
    if c=="H":
        print("HELLO",name)
    elif c=="G":
        print("GOODBYE",name)
    else:
        print("invalid message")
    print("(H)ello""\n""(G)oodbye""\n""(Q)uit" )
    c = input(">>> ")
print("Finished.")
    