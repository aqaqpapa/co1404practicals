
def main():
  score = float(input("Enter score: "))
  print(outcome(score))

def outcome(s):
  if s<0 or s>100:
    return "Invalid score"
  elif s>=90 :
    return"Excellent"
  elif s>=50 :
    return"Passable"
  else:
    return"Bad"

main()

