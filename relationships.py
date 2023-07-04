#Code to extract entities and relationships from a scientific paperd
from extract_pdf import all_text
import spacy
from spacy import displacy

# Load the spaCy English model
nlp = spacy.load('en_core_web_sm')



# Process the paper text with spaCy
doc = nlp(all_text)

# Extract entities and their labels
entities = [(ent.text, ent.label_) for ent in doc.ents]

# Display the entities
print('Entities:')
for entity in entities:
    print(entity)

# Extract relationships from the document
relationships = []
for sent in doc.sents:
    for token in sent:
        if token.dep_ == 'ROOT' and token.pos_ == 'VERB':
            relationship = (token.text, [child.text for child in token.children])
            relationships.append(relationship)

# Display the relationships
print('\nRelationships:')
for relationship in relationships:
    print(relationship)
