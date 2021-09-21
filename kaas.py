kaaskleur = input('is de kaas geel?')
if kaaskleur == "ja":
    kaasgat = input('zitten er gaten in?')
    if kaasgat == "ja":
        kaasprijs = input('is de kaas belachelijk duur?')
        if kaasprijs == "ja":
            print("je kaas is emmenhaler")
        elif kaasprijs == "nee":
            print("je kaas is leerdammer")
    elif kaasgat == "nee":
        kaashard = input('is de kaas hard als steen?')
        if kaashard == "ja":
            print("je kaas is pamigiano reggiano")
        elif kaashard == "nee":
            print("je kaas is goudsekaas")
elif kaaskleur == "nee":
    kaasschimmel = input('heeft de kaas blauwe schimmels?')
    if kaasschimmel == "ja":
        kaaskorst = input('heeft de kaas een korst')
        if kaaskorst == "ja":
            print("je kaas is blue de rochbaron")
        elif kaaskorst == "nee":
            print("je kaas is foume d'ambert")
    elif kaasschimmel == "nee":
        kaaskorst2 = input('heeft de kaas een korst')
        if kaaskorst2 == "ja":
            print("je kaas is camembert")
        elif kaaskorst2 == "nee":
            print("je kaas is mozerella")
