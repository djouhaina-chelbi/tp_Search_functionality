CITIES = [
    "Algiers", "El Oued", "Tamanrasset", "Ouargla", "Bejaia",
    "Constantine", "Annaba", "Biskra", "Batna", "Jijel", "Setif",
    "Skikda", "Medea", "Mostaganem", "Mascara", "Oran"
]
def city_search(query: str):
    if len(query) < 2:
        return []
