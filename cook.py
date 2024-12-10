def create_cook_book(text_file):
    cook_book = {}
    recipes = {}
    with open(text_file, 'r', encoding='utf-8') as f:
        temp = 1
        for line in f:
            if line == '\n':
                temp += 1
                continue
            if recipes.get(temp):
                recipes[temp] += [line.strip()]
            else:
                recipes[temp] = [line.strip()]
        for recipe, about in recipes.items():
            ingredients_dict = []
            for i in range(2, len(about)):
                ingredients = about[i].split(' | ')
                ingredients_dict.append({'ingredient_name': ingredients[0], 'quantity': ingredients[1], 'measure': ingredients[2]})
            cook_book[about[0]] = ingredients_dict
    return cook_book

print(create_cook_book('recipe.txt'))