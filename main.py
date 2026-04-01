import json                     # Importē json moduli, lai varētu nolasīt JSON failus
import os                       # Importē os moduli, lai varētu pārbaudīt failu esamību

# funkcija datu ielādei
def ieladet_failus(faila_vards):
    """
    Funkcija ielādē datus no faila.
    Parametrs faila_vards ir string, kas norāda faila nosaukumu.
    Funkcija atgriež dictionary ar datiem.
    """
    if os.path.exists(faila_vards):      # Pārbauda, vai fails ar doto nosaukumu eksistē
        with open(faila_vards, 'r', encoding='utf-8') as f:   # Ja eksistē, atver to lasīšanai ar UTF‑8 kodējumu
            return json.load(f)          # Nolasa faila saturu kā JSON un atgriež kā Python dict

    return {"logs": [], "alerts": []}    # Ja fails neeksistē, atgriež noklusējuma datu struktūru


# funkcija datu saglabāšanai
def saglabat_datus(dati, faila_vards):
    """
    Funkcija saglabā datus failā.
    Parametrs dati ir dictionary ar datiem.
    Parametrs faila_vards ir string, kas norāda faila nosaukumu.
    Funkcija neatgriež vērtību.
    """
    with open(faila_vards, 'w', encoding='utf-8') as f:
        json.dump(dati, f, indent=4, ensure_ascii=False)


# funkcija žurnālfailu ielādei
def ieladet_zurnala_failus(dati):
    """
    Funkcija ielādē datus no faila.
    Parametrs faila_vards ir string, kas norāda faila nosaukumu.
    Funkcija atgriež dictionary ar datiem.
    """
    # Stub: vēl nav realizēta
    print("Žurnālfailu ielāde vēl nav realizēta.")
    return dati


# funkcija visu žurnāla ierakstu apskatei
def apskatit_visus_ierakstus(dati):
    """
    Funkcija apskata visus sistēmā pieejamos žurnāla ierakstus.
    Parametrs dati ir dictionary ar datiem.
    Funkcija neatgriež vērtību.
    """
    # Stub: vēl nav realizēta
    print("Visu ierakstu apskate vēl nav realizēta.")


# funkcija meklēšanai žurnālos
def meklet_informaciju(dati):
    """
    Funkcija meklē informāciju žurnālos.
    Parametrs dati ir dictionary ar datiem.
    Funkcija neatgriež vērtību.
    """
    # Stub: vēl nav realizēta
    print("Meklēšana vēl nav realizēta.")


# funkcija žurnāla datu analīzei
def analizet_datus(dati):
    """
    Funkcija analizē žurnāla datus izmantojot definētus noteikumus.
    Parametrs dati ir dictionary ar datiem.
    Funkcija atgriež atjauninātu dictionary.
    """
    # Stub: vēl nav realizēta
    print("Datu analīze vēl nav realizēta.")
    return dati


# funkcija aizdomīgu darbību atzīmēšanai
def atzimet_aizdomigas_darbibas(dati):
    """
    Funkcija atzīmē aizdomīgas darbības.
    Parametrs dati ir dictionary ar datiem.
    Funkcija atgriež atjauninātu dictionary.
    """
    # Stub: vēl nav realizēta
    print("Aizdomīgu darbību atzīmēšana vēl nav realizēta.")
    return dati


# funkcija brīdinājumu ģenerēšanai
def generet_bridinajumus(dati):
    """
    Funkcija ģenerē brīdinājumus.
    Parametrs dati ir dictionary ar datiem.
    Funkcija atgriež atjauninātu dictionary.
    """
    # Stub: vēl nav realizēta
    print("Brīdinājumu ģenerēšana vēl nav realizēta.")
    return dati


# funkcija brīdinājumu saraksta apskatei
def apskatit_bridinajumus(dati):
    """
    Funkcija apskata izveidoto brīdinājumu sarakstu.
    Parametrs dati ir dictionary ar datiem.
    Funkcija neatgriež vērtību.
    """
    # Stub: vēl nav realizēta
    print("Brīdinājumu apskate vēl nav realizēta.")


# funkcija statistikas analīzei
def analizet_statistiku(dati):
    """
    Funkcija analizē un apskata statistiku par sistēmās notikumiem.
    Parametrs dati ir dictionary ar datiem.
    Funkcija neatgriež vērtību.
    """
    # Stub: vēl nav realizēta
    print("Statistikas analīze vēl nav realizēta.")


# funkcija datu saglabāšanai datubāzē
def saglabat_datubaze(dati):
    """
    Funkcija saglabā analizētos datus datubāzē.
    Parametrs dati ir dictionary ar datiem.
    Funkcija neatgriež vērtību.
    """
    # Stub: vēl nav realizēta
    print("Datu saglabāšana datubāzē vēl nav realizēta.")


# galvenā funkcija ar izvēlni
def galvena_izvelne():
    """
    Funkcija parāda galveno izvēlni un apstrādā lietotāja izvēles.
    Funkcija neatgriež vērtību.
    """
    faila_vards = "siem_dati.json"  # Datu faila nosaukums
    dati = ieladet_failus(faila_vards)  # Ielādē datus no faila

    while True:
        print("\n=== SIEM Rīks ===")
        print("1. Ielādēt žurnālfailus")
        print("2. Apskatīt visus žurnāla ierakstus")
        print("3. Meklēt informāciju žurnālos")
        print("4. Analizēt žurnāla datus")
        print("5. Atzīmēt aizdomīgas darbības")
        print("6. Ģenerēt brīdinājumus")
        print("7. Apskatīt brīdinājumu sarakstu")
        print("8. Analizēt statistiku")
        print("9. Saglabāt datus datubāzē")
        print("0. Iziet")

        izvele = input("Izvēlieties darbību (0-9): ").strip()

        if izvele == "1":
            dati = ieladet_zurnala_failus(dati)
        elif izvele == "2":
            apskatit_visus_ierakstus(dati)
        elif izvele == "3":
            meklet_informaciju(dati)
        elif izvele == "4":
            dati = analizet_datus(dati)
        elif izvele == "5":
            dati = atzimet_aizdomigas_darbibas(dati)
        elif izvele == "6":
            dati = generet_bridinajumus(dati)
        elif izvele == "7":
            apskatit_bridinajumus(dati)
        elif izvele == "8":
            analizet_statistiku(dati)
        elif izvele == "9":
            saglabat_datubaze(dati)
        elif izvele == "0":
            saglabat_datus(dati, faila_vards)  # Saglabā datus pirms izejas
            print("Programma beidzas. Dati saglabāti.")
            break
        else:
            print("Nepareiza izvēle. Lūdzu, mēģiniet vēlreiz.")


# programmas sākums
if __name__ == "__main__":
    galvena_izvelne()