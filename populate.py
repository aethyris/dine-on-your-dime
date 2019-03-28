from models import *

def pop():
    #ingredients
    egg = Ingredient(ingredient_name="Egg",
        ingredient_description="Eggs are laid by female animals of many different species.",
        ingredient_picture="https://i.imgur.com/AbYTl7W.png",
        ingredient_calorie_count=78
    )
    bread = Ingredient(ingredient_name="White Bread",
        ingredient_description="A food made from a dough of flour and water.",
        ingredient_picture="https://i.imgur.com/6NDGJVC.png",
        ingredient_calorie_count=79
    )
    peanut_butter = Ingredient(ingredient_name="Peanut Butter",
        ingredient_description="Peanut butter is a food spread made from ground dry-roasted peanuts.",
        ingredient_picture="https://i.imgur.com/gIpaejP.jpg",
        ingredient_calorie_count=188
    )

    #recipe
    recipe=Recipe(recipe_title="Eggy Toasted Bread with Peanut Butter",
        recipe_author="Calvin Kwong",
        recipe_date=20190321,
        recipe_description="A description.",
        recipe_rating=1,
        recipe_picture="https://i.imgur.com/gIpaejP.jpg",
        recipe_cooking_time=10,
        recipe_calorie_count=600
    )
    db.session.add(egg)
    db.session.add(bread)
    db.session.add(peanut_butter)
    db.session.add(recipe)
    db.session.commit()

if __name__ == "__main__":
        main()
    