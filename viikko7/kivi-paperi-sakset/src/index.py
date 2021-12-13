from kps_tehdas import tehdas

def main():
    vaihtoehdot = ["a", "b", "c"]
    vaihtoehdot_teksti = ("Valitse pelataanko"
            "\n {} Ihmistä vastaan"
            "\n {} Tekoälyä vastaan"
            "\n {} Parannettua tekoälyä vastaan"
            "\nMuilla valinnoilla lopetetaan"
            ).format(vaihtoehdot[0], vaihtoehdot[1], vaihtoehdot[2])
    siirrot = ["k", "p", "s"]
    siirto_ohje_teksti = (
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin {}, {} tai {}"
            ).format(siirrot[0], siirrot[1], siirrot[2])
    
    while True:
        print(vaihtoehdot_teksti)

        vastaus = input()
        if vastaus not in vaihtoehdot:
            break

        print(siirto_ohje_teksti)

        tehdas.pelityyppi(vastaus).pelaa()

if __name__ == "__main__":
    main()
