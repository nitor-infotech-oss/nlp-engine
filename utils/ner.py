import spacy
from utils.spell import SpellCorrect
from utils.extract_date import DateExtractor
from spacy.pipeline import EntityRuler
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span
from utils.csv_helper import read_csv
import os
import glob

nlp = spacy.load("en_core_web_sm")

dirname, filename = os.path.split(os.path.abspath(__file__))

csv_files = '/home/bhartendu.bharti/personal/projects/nlp-engine/entities_files/*.csv'

mylist = [f for f in glob.glob(csv_files)]

lables = []
terms = []

for filepath in mylist:
    data = read_csv(filepath)
    for key, value in data.items():
       lables.append(key)
       terms.append(tuple(value))

print(lables)
print(terms)

class EntityMatcher(object):
    name = 'entity_matcher'

    def __init__(self, nlp, terms_list, labels_list):
        idx = 0
        for terms in terms_list:
            print(terms)
            patterns = [nlp(text) for text in terms]
            print(patterns)
            self.matcher = PhraseMatcher(nlp.vocab)
            self.matcher.add(labels_list[idx], None, *patterns)
            idx = idx + 1

    def __call__(self, doc):
        matches = self.matcher(doc)
        for match_id, start, end in matches:
            span = Span(doc, start, end, label=match_id)
            doc.ents = list(doc.ents) + [span]
        return doc

if terms:
    entity_matcher = EntityMatcher(nlp, terms, lables)

    nlp.add_pipe(entity_matcher, after="ner")

    print(nlp.pipe_names)  # The components in the pipeline

ENTITY_LABEL = (
    'DATE',
    'PERSON',
    'NORP',
    'FAC',
    'ORG',
    'GPE',
    'LOC',
    'PRODUCT',
    'EVENT',
    'WORK_OF_ART',
    'LAW',
    'LANGUAGE',
    'DATE',
    'TIME',
    'PERCENT',
    'MONEY',
    'QUANTITY',
    'ORDINAL',
    'CARDINAL'
)



class NLP(object):
    """docstring for ClassName"""

    @staticmethod
    def ner(text):
        doc = nlp(text)
        entities = []
        entities_dict = {}
        for ent in doc.ents:
            entities.append({
                'entity': ent.label_,
                'text': ent.text,
            })
        #entities = Struct(**entities)
        for ent in entities:
            if ent['entity'] in entities_dict:
                if (ent['entity'] == 'DATE'):
                    entities_dict[ent['entity']] = entities_dict[ent['entity']].append(ent['text'])
                    entities_dict['dates'] = entities_dict[ent.entity].append({ent['text']: DateExtractor.get_date(ent['text'])})
                else:
                    entities_dict[ent['entity']] = entities_dict[ent['entity']].append(ent['text'])
            else:
                if (ent['entity'] == 'DATE'):
                    entities_dict[ent['entity']] = [ent['text']]
                    entities_dict['dates'] = [{ent['text']: DateExtractor.get_date(ent['text'])}]
                entities_dict[ent['entity']] = [ent['text']]
        return {
            'entities': entities_dict, 
            'text': text
        }
                


    
if __name__ == "__main__":
    res = NLP.ner(text='India is a great country and I am flying there next day for white mango')
    print(res)

