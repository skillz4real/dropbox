#!/usr/bin/python3
import secrets
import string

def Gen(param: tuple)->string:
  """Returns a complicated string based on the param"""
  symb,digits,size=param
  pword=""
  tmp=""
  chars = []

  if symb is True:
    chars.append(string.punctuation)
  
  if digits is True:
    chars.append(string.digits)

  chars.append(string.ascii_uppercase)
  chars.append(string.ascii_lowercase)

  #Generates a password twice as big as the specified size made of random char
  #char would be a list of either ascii char digits or punctuation
  #Works well but need to refractor this entire thing
  #increase entropy
  for i in range(size*2):
    for char in chars:
      tmp += str(secrets.choice(char))

  while True:
    pword=""
    for i in range(size):
      pword+=secrets.choice(tmp) 
  
      #verification
    if symb and digits:
      if any(c.isdigit() for c in pword) and any(c in string.punctuation for c in pword) and any(c.isupper() for c in pword) and any(c.islower() for c in pword):
        return pword

    elif symb: 
      if any(c in string.punctuation for c in pword) and any(c.isupper() for c in pword) and any(c.islower() for c in pword):
        return pword
    
    elif digits:
      if any(c.isdigit for c in pword) and any(c.isupper for c in pword) and any(c.islower for c in pword):
        return pword
    else:
      if any(c.isupper for c in pword) and any(c.islower for c in pword):
        return pword
  

if __name__=="__main__":
    import argparse

    parser = argparse.ArgumentParser(
        prog = "rpg",
        description = "Generate cryptographically secure and random string of character, to be used as tokens or password",
        epilog=""
            )
    parser.add_argument("-s", "--symbol", help="set symboles to True", action="store_true", default=False)
    parser.add_argument("-d", "--digit", help="set digits to True", action="store_true", default=False)
    parser.add_argument("-l", "--length", help="specify length", default=6)

    args = parser.parse_args()
    
    p = Gen((args.symbol, args.digit, int(args.length)))
    print()
    print(f"Here is your password: {p}")
    print()
