import n_stat as ns
import n_ev as ne

counter = 1
while counter == 1:
    print ("\n[1] Stat Calculator")
    print ("[2] EV Calculator")
    num0 = int(input("Choose number: "))

    bas = int (input("\nBase Stat:"))
    lvl = int (input("Lvl:"))
    ev = int (input("evhp:"))
    iv = int (input("ivhp:"))
    stat = int(input("Desired increase in stat:"))

    if num0 == 1:
        print ("\nHp = ", ns.neil.hpcal(bas,iv,ev,lvl))
        print ("attack = ", ns.neil.otherstat(bas,iv,ev,lvl))
        print ("def = ", ns.neil.otherstat(bas,iv,ev,lvl))
        print ("sp attack = ", ns.neil.otherstat(bas,iv,ev,lvl))
        print ("sp def = ", ns.neil.otherstat(bas,iv,ev,lvl))
        print ("speed = ", ns.neil.otherstat(bas,iv,ev,lvl))
        print ("\nThe needed Evs to increase stat is ", ne.otep.evneed(stat,bas,iv,ev,lvl))
    
    elif num0 == 2:
        print ("\n[1] Single stat")
        print ("[2] All stat")
        num1 = int (input("Choose a number:"))

        if num1 == 1:
            print ("\n[1] Attack")
            print ("[2] def")
            print ("[3] sp.attack")
            print ("[4] sp.def")
            print ("[5] speed")
            print ("[6] hp")
            num20= int (input ("Choose Stat:"))

            if num20 == 1 or 2 or 3 or 4 or 5:
                print ("\nThe Stat is", ns.neil.otherstat(bas,iv,ev,lvl))
            elif num20 == 6:
                print ("\nHp = ", ns.neil.hpcal(bas,iv,ev,lvl))

        elif num1 == 2:
            print ("\nHp =", ns.neil.hpcal(bas,iv,ev,lvl))
            print ("attack =", ns.neil.otherstat(bas,iv,ev,lvl))
            print ("def =", ns.neil.otherstat(bas,iv,ev,lvl))
            print ("sp. attack =", ns.neil.otherstat(bas,iv,ev,lvl))
            print ("sp. def =", ns.neil.otherstat(bas,iv,ev,lvl))
            print ("speed =", ns.neil.otherstat(bas,iv,ev,lvl))
    
    print ("\n[1] Perform another calculation")
    print ("[2] End the program")
    num3 = int (input("choose a number:"))
    if num3 ==2:
        break
    elif num3 == 1:
        continue
