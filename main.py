import Costelo_script1_stat as stats
import Costelo_script2_ev as evs 

while True:
    
    print("=====================Welcome to Gen III Pokemon =======================") 
    typeq=input("PRESS [STAT] for STAT CALCULATOR OR PRESS [EV]for EV CALCULATOR \n Type here:")

    if typeq == 'STAT':
        while True:
            try:
                print("---------Calculate Health-----------")
                base_hp = int(input("Base HP:"))
                iv = int(input("Individual Value (0-31):"))
                ev = int(input("Effort Value (0-255):"))
                level = int(input("Level:"))
                assert 0 < iv < 32
                assert 0 < ev < 256
            except AssertionError:
                print("ERROR!")
                print("Individual Value must be in the range of 0-255")
                print("Effort Value must be in the range of 0-31")
            else:
                print("HEALTH >>>", stats.health.compute_hp(base_hp, iv, ev, level))
                break
                
        while True:
            print("-------------------------------CALCULATE OTHERSTAT-------------------------------------------")
            compute = input("Do you want to compute other stat? if yes just type the stat you want to compute \n ""[Atk], [Def], [Sp.Atk], [Sp.Def], [Spd]"".\n If no just type stop. \n >>>")
            if compute == 'Atk':
                print("---------Calculate Atk------------\n")
                base_hp = int(input("Base HP:"))
                iv = int(input("Individual Value (0-31):"))
                ev = int(input("Effort Value (0-255):"))
                level = int(input("Level:"))
                nat = float(input("Nature (1.1 or 0.9):"))
                
                print("Atk >>>", stats.health.compute_otherstat(base_hp, iv, ev, level, nat))
            elif compute == "Def":
                print("---------Calculate Def------------\n")
                base_hp = int(input("Base HP:"))
                iv = int(input("Individual Value (0-31):"))
                ev = int(input("Effort Value (0-255):"))
                level = int(input("Level:"))
                nat = float(input("Nature (1.1 or 0.9):"))
                print("Def >>>", stats.health.compute_otherstat(base_hp, iv, ev, level, nat))
            

            elif compute == "Sp.Atk":
                print("---------Calculate Sp.Atk------------\n")
                base_hp = int(input("Base HP:"))
                iv = int(input("Individual Value (0-31):"))
                ev = int(input("Effort Value (0-255):"))
                level = int(input("Level:"))
                nat = float(input("Nature (1.1 or 0.9):"))
                print("Sp.Atk >>>", stats.health.compute_otherstat(base_hp, iv, ev, level, nat))
            

            elif compute == "Sp.Def":
                print("---------Calculate Sp.Def------------\n")
                base_hp = int(input("Base HP:"))
                iv = int(input("Individual Value (0-31):"))
                ev = int(input("Effort Value (0-255):"))
                level = int(input("Level:"))
                nat = float(input("Nature (1.1 or 0.9):"))
                print("Sp.Def >>>", stats.health.compute_otherstat(base_hp, iv, ev, level, nat))
            

            elif compute == "Spd":
                print("---------Calculate Spd------------\n")
                base_hp = int(input("Base HP:"))
                iv = int(input("Individual Value (0-31):"))
                ev = int(input("Effort Value (0-255):"))
                level = int(input("Level:"))
                nat = float(input("Nature (1.1 or 0.9):"))
                print("Spd >>>", stats.health.compute_otherstat(base_hp, iv, ev, level, nat))
            elif compute == "stop":
                print("Thanks!")
                break

            else:
                print("Invalid input just read the instruction carefully!\n")
            
        

    elif typeq == 'EV':
        while True:
            try:
                stat=int(input("Stat:"))        
                modifier=float(input("Modifier (1.1 OR 0.9):"))        
                level=int(input("Level:"))
                base=int(input("Base HP:"))             
                iv=int(input("Individual Value (0-255):"))
                ev=int(input("Effort Value (0-31):"))
                assert 0 < iv < 256
                assert modifier == 1.1 or 0.9
                assert 0 < ev < 32
                
            except AssertionError:
                print("\n Input Error")
                print("The individual Value must be in the range of 0-255") 
                print("The Effects Value must be in the range of 0-31")
                print("The Modifier must be 1.1 or 0.9")
            else:  
                print("EV>>", evs.EffortValue.compute_ev(stat, modifier, level, base, iv, ev))
            break

                    
    else:
        print("Wrong Input!")
     
    
