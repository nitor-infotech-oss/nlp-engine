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


class SpacyNlp(object):
    """docstring for Nlp"""

    def __init__(self, sentance=None, lang=None):
        super(SpacyNlp, self).__init__()
        self.sentance = sentance
        self.lang = lang
        nlp = spacy.load('en_core_web_sm')
        self.doc = nlp(sentance)
        self.entities = []

    def ner(self):
        for ent in self.doc.ents:
            self.entities.append({'text': ent.text, 'entity': ent.label_})

    def custom_ner(self):
        pass
