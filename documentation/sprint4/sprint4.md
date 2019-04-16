
  
# Sprint 4 Documentation
Group B
- Calvin Kwong
- Nabeel Javed
- Jonella Wong
- Shanelle Rowe Poole
- Brandon Henriques

## Calvin Kwong
### Use Case: Follow users and generate feed
Any user with an account can follow or unfollow another account. When a user visits their feed, they can see the recent activity of the users they follow - new recipes that are posted by the users that are followed. This allows a user to stay updated with new recipes if they particularly like a certain author's recipes. When a new recipe is posted, the user's feed should be automatically updated to include the new recipe. This functions similar to the profile page of Facebook or Twitter.

### Sequence Diagrams
![Following/Unfollowing](https://i.imgur.com/FM2J9Pj.png)
![Edit/remove recipe](https://i.imgur.com/EDG226P.png)

### Database Modelling
![Following/Followed](https://i.imgur.com/b9v0E2Y.png)

### Tasks Rendered

`models.py`:
- Updated User model to contain a self-referencing relationship
- User model includes a list of followed posts

`blueprints/users.py`:
- Routes for following/unfollowing user.
- Modified add_recipe() route to send a SocketIO event upon the creation of a recipe.

`templates/feed.html`:
- Renders a list of cards. These cards display the 10 most recent recipes from authors that the user follows.
- SocketIO new recipe event can re-render the list of cards, displaying the new recipe at the top.

`sockets.py`:
- SocketIO events for managing a user's SocketIO session ID
- Sends event to signal a new recipe being created to users who follow the author of the recipe

## Nabeel Javed
### Use Case: Editor's Recommendations
Certain users with elevated permissions can choose recipes to be displayed as editor's recommendations, such as on the front page.
### Sequence Diagrams
### Database Models
### Tasks Rendered

## Jonella Wong
### Use Case: Get popular recipes
The system will sort the database based on recipe ratings and will do a reverse sort on the list in order to retrieve the higher ratings first. It will then display this information to the user via image links.
### Sequence Diagrams
### Database Models
### Tasks Rendered
To achieve this I modified:
- The `index.html` file to create a section on the website dedicated to popular recipes. Only 2 recipes are displayed in order to maintain website simplicity, and it gives the user an option to view more recipes via a link that will retrieve the sorted list of recipes based on rating.
- The `app.py` to define the popular recipe list. This method will sort the list and print out 2 of the top recipes thriving on the site.

## Shanelle Rowe Poole
### Use Case: View leaderboard/reward users
Users can keep track of where they are in the point system. Users receive an award such as trophies or badges.
### Sequence Diagrams
### Database Models
### Tasks Rendered

## Brandon Henriques
### Use Case: Generate shopping list
The user can generate a shopping list of all necessary ingredients from a recipe. Originally was the use-case for sprint 3.
### Sequence Diagrams
### Database Models
A database that can be searched to piece together recipes or hold general information on the simple ingredients.
### Tasks Rendered
Files –  add recipe. Used to reference from shopping list
Shoppinglist, main code for the hopping list file.
Showlist, used to grab the shopping list
Take – get ingredients from show list and compile all into shopping list
