import random 
import faker
import csv 

fake = faker.Faker(['fr_FR','it_IT'])

with open("fake.csv", "w", encoding="utf-8", newline = "") as f:
    writer = csv.DictWriter(f, fieldnames = ["nom", "prenom", "telephone"])
    writer.writeheader()
    for i in range(10000):
        try:
            contact = {}
            contact["prenom"], contact["nom"] = fake.name().split(" ")
            contact["telephone"] = random.choice(["06","07","02"]) + str(random.randint(10000000,99999999))
            writer.writerow(contact)
        except:
            pass