#!/usr/bin/env python3
from faker import Faker
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig

fake = Faker()

def anonymize(ent, func):
    if ent == "PII":
        return ent

    while True:
        anon = func()
        yn = input(f"Anonymize the entity '{ent}' to '{anon}'? [y/n] ").lower()
        if yn == "y":
            return anon
        elif yn == "n":
            return ent

operators = {
        "PERSON": OperatorConfig("custom", {"lambda": lambda ent : anonymize(ent, fake.name)}),
        "DATE_TIME": OperatorConfig("custom", {"lambda": lambda ent : anonymize(ent, fake.date)}),
        "IP_ADDRESS": OperatorConfig("custom", {"lambda": lambda ent : anonymize(ent, fake.ipv4)}),
        "PHONE_NUMBER": OperatorConfig("custom", {"lambda": lambda ent : anonymize(ent, fake.phone_number)}),
        "CREDIT_CARD": OperatorConfig("custom", {"lambda": lambda ent : anonymize(ent, fake.credit_card_number)}),
        "EMAIL_ADDRESS": OperatorConfig("custom", {"lambda": lambda ent : anonymize(ent, fake.email)}),
        "LOCATION": OperatorConfig("custom", {"lambda": lambda ent : anonymize(ent, fake.city)}),
}

def analyze(text):
    analyzer = AnalyzerEngine()
    anonymizer = AnonymizerEngine()

    analyzer_result = analyzer.analyze(
        text=text,
        language="en",
    )
    
    return anonymizer.anonymize(
        text=text,
        analyzer_results=analyzer_result,
        operators=operators
    )


def main():
    text = input("Please input your text to be anonymized:\n")
    print("\nYou will be prompted to choose whether to anonymize each instance of PII. To regenerate the result, simply enter it as blank.\n")
    result = analyze(text)
    print(f"\nAnonymized result:\n{result.text}")

if __name__ == "__main__":
    main()
