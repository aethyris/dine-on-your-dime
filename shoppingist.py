print ("Ready to do some shopping? what would you like to add to your shoppinglist?")
shoplist = []

add = input("would you like to add something to the shoppinglist today? yes or no")

while add.lower () == "yes";

    item = input("what would you like to add?")
    shoplist.add(item)
    add = input("do you want to add that to your list? yes or no?")


def delete_from_list():
    delete_me = input("Which item would you like to delete from the list? ")
    shopping_list.remove(delete_me)
    print("{} has been removed from the list. You now have {}items".format(delete_me, len(shopping_list)))

    print()
    print("here is what's on your list")
    shoplist.sort()

      for item in shoplist:
      print(item)


def show_list(list):
    clear_console()
    # Print out the list
    if len(list) == 0:
        print("You have 0 items in your list.")
    else:
        print("Here's your list:\n")
        for item in list:
        print(item)
