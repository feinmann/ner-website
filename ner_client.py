import spacy

class NamedEntityClient:
    def __init__(self, model):
        self.model = model

    def get_ents(self, sentence):
        doc = self.model(sentence)
        entities = [{'ent': ent.text, 'label': self.map_label(ent.label_)} for ent in doc.ents]
        return { 'ents': entities, 'html': ''}

    def map_label(self, label):
        label_map = {
            'PERSON': 'Person',
            'NORP'  : 'Group'
        }
        return label_map[label]