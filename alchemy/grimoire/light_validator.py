def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    valid_ingredients = light_spell_allowed_ingredients()
    list = []
    for item in ingredients.split(","):
        list.append(item.strip().lower())
    if any(ingredient in valid_ingredients for ingredient in list):
        return f"{list} - VALID"
    return f"{list} - INVALID"
