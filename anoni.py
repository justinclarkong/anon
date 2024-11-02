#!/usr/bin/env python3
import spacy
from faker import Faker

fake = Faker()
# use the small model for efficiency
nlp = spacy.load('en_core_web_sm')
# merge entities so we can replace them as a whole
nlp.add_pipe("merge_entities")

text = open('a.txt').read()

print(text)
doc = nlp(text)

for ent in doc:
    print(ent.orth_, ent.lemma_, ent.pos_, ent.ent_type_)


for ent in doc.ents:
    print(f"{ent.label_}: {ent.text}")

print()

print([t.text if not t.ent_type_ else t.ent_type_ for t in doc])
print(" ".join([t.text if not t.ent_type_ else t.ent_type_ for t in doc]) )

# Replace the PII with anonymized data
anon = " ".join([fake.name() if t.ent_type_ == "PERSON" else fake.company() if t.ent_type_ == "ORG" else fake.date() if t.ent_type_ == "DATE" else t.text if not t.ent_type_ else t.ent_type_ for t in doc])

# Remove extranneous spaces before punctuation.
print(anon.replace(" .", "."))
