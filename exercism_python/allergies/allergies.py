class Allergies(object):
    _all_allergens = {'eggs': 1,
                      'peanuts': 2,
                      'shellfish': 4,
                      'strawberries': 8,
                      'tomatoes': 16,
                      'chocolate': 32,
                      'pollen': 64,
                      'cats': 128}

    def __init__(self, score):
        self.allergy_score = score
        self.allergies = []
        self._set_allergies()

    def _set_allergies(self):
        for allergen in Allergies._all_allergens:
            if self.is_allergic_to(allergen):
                self.allergies.append(allergen)

    def is_allergic_to(self, item):
        return bool(Allergies._all_allergens[item] & self.allergy_score)

    @property
    def lst(self):
        return self.allergies