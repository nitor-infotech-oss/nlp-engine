import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span

class EntityMatcher(object):
    name = 'entity_matcher'

    def __init__(self, nlp, terms_list, labels_list):
        idx = 0
        for terms in terms_list:
            patterns = [nlp(text) for text in terms]
            self.matcher = PhraseMatcher(nlp.vocab)
            self.matcher.add(labels_list[idx], None, *patterns)
            idx = idx + 1

    def __call__(self, doc):
        matches = self.matcher(doc)
        for match_id, start, end in matches:
            span = Span(doc, start, end, label=match_id)
            doc.ents = list(doc.ents) + [span]
        return doc

nlp = spacy.load("en_core_web_sm")
terms = [(u"cat", u"dog", u"tree kangaroo", u"giant sea spider"), ('mango', 'carrot')]
entity_matcher = EntityMatcher(nlp, terms, ["ANIMAL", 'FRUIT'])

nlp.add_pipe(entity_matcher, after="ner")

print(nlp.pipe_names)  # The components in the pipeline

doc = nlp(u"India is a great country and I am flying there next day for mango and carrot soe")
print([(ent.text, ent.label_) for ent in doc.ents])