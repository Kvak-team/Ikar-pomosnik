import json
from pathlib import Path


def proverit_otvety(voprosy, otvety):
    verno = 0
    oshibki = []
    propushcheno = []

    for i in range(len(voprosy)):
        vopros = voprosy[i]  
        nomer = vopros["номер"]  
        pravilnyy = vopros["правильный_вариант"]  
        otvet = otvety[i]  

        if otvet == 0:
            propushcheno.append(nomer)
        elif otvet == pravilnyy:
            verno += 1
        else:
            oshibki.append(nomer)

    return {
        "всего": len(voprosy),
        "верно": verno,
        "ошибки": oshibki,
        "пропущено": propushcheno,
    }


if __name__ == "__main__":
    put = Path(__file__).with_name("Учебная_тема.json")
    with put.open("r", encoding="utf-8-sig") as file:
        tema = json.load(file)

    voprosy = tema["вопросы"]
    otvety = [2, 0, 0]
    rezultat = proverit_otvety(voprosy, otvety)
    print(rezultat)
