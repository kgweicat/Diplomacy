
def diplomacy_read(s):
    """

    """
    wordlist = s.split()
    return wordlist

# ------------
# collatz_eval
# ------------


def diplomacy_print(w, a):
    """

    """
    w.write(str(a))


def diplomacy_solve(r, w):
    """
    r a reader
    w a writer
    """
    if r == "\n" or r == "":
        return
    cities = {}
    xsupporty = []
    for s in r:
        listofline = diplomacy_read(s)

        if listofline[1] not in cities:
            cities[listofline[1]] = {}
        cities[listofline[1]][listofline[0]] = 0

        if listofline[2] == "Hold":
            cities[listofline[1]][listofline[0]] += 1

        if listofline[2] == "Move":
            if listofline[3] in cities:
                # print(cities)
                cities[listofline[3]][listofline[0]] = 1
                del cities[listofline[1]][listofline[0]]
            else:
                cities[listofline[3]] = {}
                cities[listofline[3]][listofline[0]] = 1
                del cities[listofline[1]][listofline[0]]
        if listofline[2] == "Support":
            for entries in list(cities.values()):
                for x in entries:
                    if listofline[3] == x:
                        entries[x] += 1
                        xsupporty.append([listofline[0], x])

    finished = False
    for city, army_strength in list(cities.items()):
        if len(army_strength) > 1:
            for army, power in list(army_strength.items()):
                if not finished:
                    if army_strength[army] == 0:
                        for x, y in xsupporty:
                            if army == x:
                                cities[city][x] += 1
                        for city, army_strength in list(cities.items()):
                            if not finished:
                                for army, power in list(army_strength.items()):
                                    for x, y in xsupporty:
                                        if army == y:
                                            cities[city][y] -= 1
                                            finished = True
                                            break

    finallist = []
    for city, army_strength in list(cities.items()):
        count = 0
        max = 0
        for number in list(army_strength.values()):
            if number > max:
                max = number
        for number in list(army_strength.values()):
            if number == max:
                count += 1

        if count == 1:
            for army, power in army_strength.items():
                if army_strength[army] != max:
                    finallist.append(army + " [dead]")
                if army_strength[army] == max:
                    finallist.append(army + " " + city)
        if count != 1:
            for army, power in army_strength.items():
                finallist.append(army + " [dead]")

    sortedfinal = sorted(finallist)
    a = "\n".join(sortedfinal)

    diplomacy_print(w, a)
