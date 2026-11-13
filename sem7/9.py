nom = {
    "Python": {
        "zohiolch": "Bat",
        "too": 1995
    },
    "Java": {
        "zohiolch": "Bold",
        "too": 2013
    },
    "HTML": {
        "zohiolch": "Dorj",
        "too": 2004
    }
}

for ner, medeelel in nom.items():
    print("Номын нэр:", ner)
    print("Зохиогч:", medeelel["zohiolch"])
    print("Номын on:", medeelel["too"])
    print()