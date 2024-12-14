# Импорт модуля для красивого отображения вывода

from pprint import pprint

class Cooking:

    def __init__(self):
        self.cook_book = {}
        self.recipes = {}

    def create_cook_book(self, text_file):

        # Создаем словарь с блюдами из файла, перебирая его построчно

        with open(text_file, 'r', encoding='utf-8') as f:
            temp = 1
            for line in f:
                if line == '\n':
                    temp += 1
                    continue
                if self.recipes.get(temp):
                    self.recipes[temp] += [line.strip()]
                else:
                    self.recipes[temp] = [line.strip()]
            for recipe, about in self.recipes.items():
                ingredients_dict = []
                for i in range(2, len(about)):
                    ingredient = about[i].split(' | ')
                    ingredients_dict.append({'ingredient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]})
                self.cook_book[about[0]] = ingredients_dict
        return self.cook_book

    def get_shop_list_by_dishes(self, dishes, person_count):
        full_ingredients = {}
        for dish in dishes:
            if dish in self.cook_book:
                for ingredient in self.cook_book[dish]:
                    about_dict = {'measure' : ingredient['measure'], 'quantity' : int(ingredient['quantity']) * person_count}
                    if full_ingredients.get(ingredient['ingredient_name']):
                        full_ingredients[ingredient['ingredient_name']]['quantity'] = int(full_ingredients[ingredient['ingredient_name']]['quantity']) + int(about_dict['quantity'])
                    else:
                        full_ingredients[ingredient['ingredient_name']] = about_dict
            else:
                return 'Такого блюда нет в меню'
        return full_ingredients

master = Cooking()
master.create_cook_book('recipe.txt')
pprint(master.get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))