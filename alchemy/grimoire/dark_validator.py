from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    valid_ingredients = dark_spell_allowed_ingredients()
    list = []
    for item in ingredients.split(","):
        list.append(item.strip().lower())
    if any(ingredient in valid_ingredients for ingredient in list):
        return f"{list} - VALID"
    return f"{list} - INVALID"
