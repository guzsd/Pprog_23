def adatbeolv():
    urhajosok = []
    with open('astronauts.csv', 'r', encoding='utf-8') as forrasfajl:
        megnevezes = forrasfajl.readline().strip().split(",")
        for sor in forrasfajl:
            adatok = sor.strip().split(',')
            urhajos = {
                megnevezes[0]: adatok[0],
                megnevezes[1]: adatok[1],
                megnevezes[2]: adatok[2],
                megnevezes[3]: adatok[3],
                megnevezes[4]: adatok[4]
            }
            urhajosok.append(urhajos)
    return urhajosok


def sorszam(honapok_gyakorisaga, leggyakoribb_ertek):
    index = 0
    leggyakoribb_sorszam = 0
    for elem in honapok_gyakorisaga:
        if elem == leggyakoribb_ertek:
            leggyakoribb_sorszam = index
        index += 1
    return leggyakoribb_sorszam


def honapok(urhajos_adatok):
    honapok_gyakorisaga = []
    for _ in range(12):
        honapok_gyakorisaga.append(0)
    for elem in urhajos_adatok:
        adat = elem['Birth Date'].split('/')
        honapok_gyakorisaga[int(adat[0]) - 1] += 1
    osszes = len(urhajos_adatok)

    seged_lista = []
    for elem in honapok_gyakorisaga:
        seged_lista.append(elem)
    elso_leggyakoribb_ertek = max(seged_lista)
    seged_lista.remove(elso_leggyakoribb_ertek)
    masodik_leggyakoribb_ertek = max(seged_lista)
    seged_lista.remove(masodik_leggyakoribb_ertek)
    harmadik_leggyakoribb_ertek = max(seged_lista)

    elso_leggyakoribb_sorszam = sorszam(honapok_gyakorisaga, elso_leggyakoribb_ertek)
    masodik_leggyakoribb_sorszam = sorszam(honapok_gyakorisaga, masodik_leggyakoribb_ertek)
    harmadik_leggyakoribb_sorszam = sorszam(honapok_gyakorisaga, harmadik_leggyakoribb_ertek)

    print(f'{elso_leggyakoribb_sorszam + 1}.honap: {round((elso_leggyakoribb_ertek / osszes) * 100, 1)}%\n'
          f'{masodik_leggyakoribb_sorszam + 1}.honap: {round((masodik_leggyakoribb_ertek / osszes) * 100, 1)}%\n'
          f'{harmadik_leggyakoribb_sorszam + 1}.honap: {round((harmadik_leggyakoribb_ertek / osszes) * 100, 1)}%')


def main():
    honapok(adatbeolv())


main()
