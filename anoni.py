#!/usr/bin/env python3
from faker import Faker
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig

text = open('a.txt').read()
print(text)

fake = Faker()

def operators():
    return {
        "PERSON": OperatorConfig("custom", {"lambda": lambda x : fake.name()}),
        "DATE_TIME": OperatorConfig("custom", {"lambda": lambda x : fake.date()}),
        "IP_ADDRESS": OperatorConfig("custom", {"lambda": lambda x : fake.ipv4()}),
        "PHONE_NUMBER": OperatorConfig("custom", {"lambda": lambda x : fake.phone_number()}),
        "CREDIT_CARD": OperatorConfig("custom", {"lambda": lambda x : fake.credit_card_number()}),
        "EMAIL_ADDRESS": OperatorConfig("custom", {"lambda": lambda x : fake.email()}),
        "LOCATION": OperatorConfig("custom", {"lambda": lambda x : fake.city()}),
    }

analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()
analyzer_result = analyzer.analyze(
            text=text,
            language="en",
)

anonymizer_result = anonymizer.anonymize(
    text=text,
    analyzer_results=analyzer_result,
    operators=operators()
)

print(anonymizer_result)
