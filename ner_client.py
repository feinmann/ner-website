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
            'PERSON'   : 'Person',
            'NORP'     : 'Group',
            'LOC'      : 'Location',
            'LANGUAGE' : 'Language',
            'GPE'      : 'Location'
        }
        return label_map[label]