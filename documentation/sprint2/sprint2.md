# Sprint 2 Documentation
Group B
- Calvin Kwong
- Nabeel Javed
- Jonella Wong
- Shanelle Rowe Poole
- Brandon Henriques

## Calvin Kwong
### Use Case: Create User Profiles and Filters

The user can create an account that will be used to save their own eating preferences so they don’t have to keep using the filter. There needs to be a way for the user to register for an account as well as log-in. Users who have an account will be able to access their user preferences (allowing them to change their avatar, description, privacy settings, etc.) The user will be able to access and save filters directly to their profile instead of needing to use the search filter every single time. The search filter and the user’s saved filters have the same options.

The user also needs a profile page so that social elements can be added later on (recipes, favorites, followers).

### Sequence Diagrams
**Sign in**
User enters information into fields -> system validates credentials -> user is added to the current session.

**Editing preferences**
User opens a settings page -> user enters preferences into fields (dropdown and numerical input) -> system saves the data into a filter object

**Searching with filters**
If the user has an account: System loads the saved filters into the modal -> user enters search term into search bar -> system retrieves all items which the user's input matches
If the user does not have an account: System shows empty form in modal -> user enters in filters via dropdown and numerical input -> system retrieves items that match the user's input

### Database Modelling
![User and Filter Models](https://i.imgur.com/mrqEcio.png)

### Tasks Rendered
In addition to creating the User and Filter models, I created the routes and templates for signing in, registering a new user, logging out, editing settings, having a profile page, and different errors. These routes were added in the `users.py` file. The templates I created include `login.html`, `settings.html`, `signup.html`, `user.html`, and all the files in the errors folder.

Furthermore, I modified the `layout.html` file so that the filters are now located in the `filter.html`. The end result is that users are able to create accounts and use these accounts to save filters.

While the search function without any filters applied works, I am waiting for my team members to implement the functionality of using different filters. The search filters are dependent on the completion of the functionality to search by type of ingredient or by calorie count. As of writing this documentation, the only search functionality that has been implemented is the basic keyword search without any filters that I implemented in Sprint 1. The filters are being sent in the POST request and simply need to be applied.

## Nabeel Javed
### Use Case: Filter by Calories and Cooking Time
### Sequence Diagrams
### Database Models
### Tasks Rendered
Updated filter form to provide input for calorie range and cooking time range.

No documentation provided.

## Jonella Wong
### Use Case: Filter by Price
### Sequence Diagrams
### Database Models
### Tasks Rendered
No documentation provided.

## Shanelle Rowe Poole
### Use Case: Filter by Meal Type, Meal Style, and Dietary Preferences
### Sequence Diagrams
### Database Models
### Tasks Rendered
Updated filter form to provide input for meal type, meal style, and dietary preferences.

No documentation provided.

## Brandon Henriques
### Use Case: Filtering by Ingredient
### Sequence Diagrams
### Database Models
### Tasks Rendered
No documentation provided.