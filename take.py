def getAllIngredientsInShopList(cls, user):

       ingredients = db.session.query(Ingredient.name).\
                     join(ShoppingList).\
                     filter(ShoppingList.ingredient_fk == Ingredient.name).\
                     filter(ShoppingList.user_fk == user).\
                     order_by(Ingredient.name).all()

return ingredients