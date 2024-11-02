# anoni.py

A Python module and script to anonymize personally identifiable information (PII).

## Installation

As anonipy works as a self-contained script, simply install the dependencies:

```bash
pip install presidio_anonymizer presidio_analyzer faker
```

## Technical Details

Anonipy uses Spacy's natural language processing (NLP) capabilities to identify PII and replaces them with fake, anonymized data from Faker.
