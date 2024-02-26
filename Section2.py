from random import randint

def battle(
    pHP,
    pATK,
    pDEF,
    pS,
    eHP,
    eATK,
    eDEF,
    eS,
    eName,
):
  print(f"Your HP: {pHP} | Your ATK: {pATK} | Your DEF: {pDEF}")
  while pHP > 0 and eHP > 0:
    print("ATK to attack | DEF to shield")
    pAct = input("> ")
    if pAct != "ATK" and pAct != "DEF":
      print("Invalid action")
      print("Your action will be chosen randomly")
      pAct = random.randint(1, 2)
      continue

    if pAct == 1:
      pAct = "ATK"
    elif pAct == 2:
      pAct = "DEF"

    eAct = random.randint(1, 3)
    if eAct == 1:
      eAct = "ATK"
    elif eAct == 2:
      eAct = "DEF"
    elif eAct == 3:
      eAct = "NONE"

    # DEAL DAMAGE

    eEATK = (eATK / 100) * (100 - pDEF)
    pEATK = (pATK / 100) * (100 - eDEF)

    if pAct == "ATK" and eAct == "ATK":
      print("You both attacked")
      pHP -= eEATK
      eHP -= pEATK
    elif pAct == "ATK" and eAct == "DEF":
      print(f"The {eName} blocked your attack")
    elif pAct == "DEF" and eAct == "ATK":
      print(f"You blocked the {eName}s attack")
    elif pAct == "DEF" and eAct == "DEF":
      print("You both blocked")
    else:
      if pAct == "ATK":
        print("The enemy did nothing")
        eHP -= pEATK
      else:
        print("You did nothing")

    # PRINT RESULTS
    print(f"Your HP: {pHP}")
    print(f"{eName}s HP: {eHP}")
  if eHP <= 0:
    print(f"You defeated the {eName}")
    return True
  else:
    print(f"You were defeated by the {eName}")
    return False
