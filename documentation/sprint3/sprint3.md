
# Sprint 3 Documentation
Group B
- Calvin Kwong
- Nabeel Javed
- Jonella Wong
- Shanelle Rowe Poole
- Brandon Henriques

## Calvin Kwong
### Use Case: Create Meal Plans
Each user has a calendar in their profile that can contain events. These events consist of meals that the user has planned as well as any notes. Users can add recipes to their meal plans directly from the search and can edit/remove them from the calendar screen. This allows the user to schedule their upcoming meals on a calendar which takes into account the estimated time to complete each recipe.

### Sequence Diagrams
![Add recipe](https://i.imgur.com/czgraox.png)
![Edit/remove recipe](https://i.imgur.com/EpdjKUn.png)

### Database Modelling
![PlannedRecipeAssociation](https://i.imgur.com/cdcMxOR.png)

### Tasks Rendered
`calendar.py`:
- Route for viewing a user's calendar.
- Route to return a JSON list of a user's planned recipes and the extra data from PlannedRecipeAssociation.
- Routes to add, edit, and remove recipes from a user's meal plan.

`calendar.html`:
- Renders a calendar and events using [FullCalendar4](https://fullcalendar.io/).
- User can click on an event to view information.
- Event modal allows the user to edit or remove the event from the meal plan. This uses jQuery Form Plugin so that the user can stay on the same page while the calendar is re-rendered.

I modified User and Recipe in `models.py` so I could create a PlannedRecipeAssociation table. The user profiles now contain a button to visit that user's calendar, although you can only modify your own calendar. I also modified `search.html` so that each search result would have a button allowing the user to add the recipe to the meal plan. This keeps the user on the same page, but a toast gives the user confirmation and the ability to redirect to their calendar.

I started refactoring some of the forms to use `flask-wtf`. This involved the creation of `forms.py` and the modifications needed in templates and routes to support the use of these forms.

## Nabeel Javed
### Use Case: Create Recipes
If the user is logged in they can access their settings and create a recipe. Through forms the recipes: name, description, ingredients, picture, cooking time and calorie count are added to the database and are immediately searchable.
### Sequence Diagrams
### Database Models
### Tasks Rendered
To achieve this I modified:
- The settings.html file to include a createrecipetab and all the UI.
- The users.py to define a new route and function to add the recipe to the database.
- The models.py file was accessed by both the settings.html and users.py for the database Recipe attributes.

## Jonella Wong
### Use Case: Write comments and post photos
The user can comment on a recipe and upload a photo of their own creations. The comment will be sent to the system and saved in the database and will be viewed when the webpage is retrieved again. Previous comments and uploads will be able to be viewed when the page is refreshed.
### Sequence Diagrams
### Database Models
### Tasks Rendered
To achieve this I modified:
- The recipes.html file to include comment box and upload photo option button.
- The forms.py to define a new form for the comment box and upload photo option through the implementation of flask_wtf.
- The app.py file to define a function in which the comment and photos will be saved into the database and be retrieved when the website is recalled.

The use-case has not been merged onto the master branch since it does not completely work. Instead it is on the dev-comments branch.

## Shanelle Rowe Poole
### Use Case: Like and favorite recipes
My use case was to create a favorite / like or unlike for each recipe. Users should be able to favorite the recipes they tried, and enjoyed. They can also like or unlike a recipe that they might have tried. We are trying to keep track of the likes because we want to provide a reward program.
### Sequence Diagrams
### Database Models
### Tasks Rendered
Created the like, unlike, and favorite routes. Created html to display likes and favorites for users. This is not pushed onto release v0.3, but should be on a later commit.

## Brandon Henriques
### Use Case: Generate shopping list
### Sequence Diagrams
![Use Case 2](https://i.imgur.com/XvtybK1.png)
### Database Models
![Use Case 2](https://i.imgur.com/C4bTnKK.png)
### Tasks Rendered
Partially finished Sprint 2 Use Case:
- Create a database for ingredients
- Filtering to type of ingredients (unfinished)

A database that can be searched to piece together recipes or hold general information on the simple ingredients.
