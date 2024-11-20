# AI HEROES

Here is a link to the live project. (https://dashboard.heroku.com/apps/ai-heroes-blog)

AI HEROES is a website where users come together to share their favourite created recipes. It is built using the Django Framework in python.

![responsive](assets/images/responsive.png)

## Contents 

- [User Experience (UX)](#user-experience-ux)
   * [User Stories](#user-stories)
   
- [Design](#design)
   * [Colour Scheme](#colour-scheme)
   * [Typography](#typography)
   * [Imagery](#imagery)
   * [Wireframes](#wireframes)
   * [Database Schema](#database-schema)

- [Features](#features)
   * [Home page](#home-page)
   * [Accounts](#accounts)
   * [All Recipes page](#all-recipes-page)
   * [Favourite Recipes](#favourite-recipes)
   * [Your Recipes](#your-recipes)
   * [Searched Recipes](#searched-recipes)
   * [Recipe Detail page](#recipe-detail-page)
   * [Add Recipe page](#add-recipe-page)
   * [Edit Recipe page](#edit-recipe-page)
   * [Features to add](#features-to-add)

- [Technologies](#technologies)
   * [Languages used](#languages-used)
   * [Libraries & Programs Used](#libraries-and-programs-used)

- [Testing](#eat-me)
  
- [Deployment](#deployment)
   * [Github pages](#github)
   * [Django and Heroku](#django-and-heroku)
   * [Forking](#forking)
   * [Clone](#clone)

- [Credits](#credits)
   * [Code](#code)
   * [Media](#media)

## User Experience (UX)

AI HEROES visitor is a person that is familiar wiht the term "AI" but doesn't really ubnderstand it .This person is curious and would like to explore the field and looking for sometjhing that can explain with examples the use of the best AI tools available.

## User Stories

A list of user stories grouped into epics for better structure and clarity.

### EPIC | User Experience and Interface
- As a visitor, I want the website to be visually appealing and easy to navigate so that I have an enjoyable experience while exploring AI tools.
- As a visitor, I want to view the homepage so that I can learn about the website and the AI tools it features.
- As a visitor, I can navigate the website with ease so that I have an enjoyable experience exploring AI tools.
- As a user, I want to see tools in paginated format so that I don’t have to scroll through a long list of tools.
- As a visitor, I want to receive feedback (success/error messages) after completing actions so that I understand the outcome of my interaction.
- As a visitor, I want to access an error page with an option to navigate back to the homepage.
- As a visitor, I want to see social media links to follow and contact the project online.

### EPIC | Content Management
- As an admin, I want to create, read, update, and delete posts so that I can easily manage my page content.
- As a Site Admin, I can approve or disapprove comments so that I can only display relevant topics.
- As a Site User, I can modify or delete my comment on a post so that I can be involved in the conversation.
- As a Site Admin, I can create draft posts so that I can finish writing the content later.
- As a Site Admin, I can create, update, or delete the about page content so that it is available on the site.

### EPIC | User Interaction and Engagement
- As a Site User, I am able to leave comments on a post so that I can share my opinion on the topic.
- As a user, I can view the comments so that I can be up to date with the recent engagement.
- As a Site User, I am able to click on the About link so that I can read the content of the site.
- As a user, I want to be able to send a message to the site owner so that I can address my query to the relevant people.
- As an admin, I can read the message sent by the user so that I can have a better understanding of their inquiries, needs, or feedback.

### EPIC | Voting and AI Tools Ranking
- As a visitor, I want to see the AI tools ranked by popularity based on votes so that I can easily identify the top-rated tools.
- As a user, I want to vote for an AI tool so that I can express my fascination and interest.
- As an admin, I want to monitor votes to prevent misuse and ensure fair voting.
- As a user, I want to see tools in a paginated format so that I don’t have to scroll through a long list of tools.

### EPIC | User Accounts and Authentication
- As a user, I want to log in using my email and password so that I can access personalized features.
- As a user, I want to register an account using my email and password so that I can interact more deeply with the website.

### EPIC | Deployment and Testing
- As an admin, I want to deploy the website successfully so that it is accessible to users and can be included in my portfolio.

[Back to top ⇧](#AI-Heroes-PP4)




 #DONE UP TO HERE 

## Design

The look of this website was based loosely around The Code Institute's 'I think therefore I Blog' project.  

### Colour Scheme
- I wanted to keep the colour scheme simple so I stuck with black, white and different shades of grey. This is because the uploaded pictures from users could be any host of colours, so by keeping the colour scheme neutral the site minimises the risk of clashing with any images, keeping them the main focus of the user.

### Typography
- On the site I will be using the default bootstrap fonts as I find them clean, elegant and easy to read so I feel they will fit in with the site's theme nicely. The only font used on the site will be Imbue which is solely used to style the logo.

### Imagery
- All the imagery will be food related with only 4 images being static. The rest will be uploaded by various users.

### Wireframes

Wireframes for each page are linked here:

* [Home Page](assets/documents/home_page.pdf)
* [All Recipes](assets/documents/all_recipes.pdf)
* [Detailed Recipe](assets/documents/detailed_recipe.pdf)
* [Your Recipes](assets/documents/your_recipes.pdf)
* [Favourite Recipes](assets/documents/favourite_recipes.pdf)
* [Searched Recipes](assets/documents/searched_recipes.pdf)
* [Add Recipe](assets/documents/add_recipe.pdf)
* [Register, log in/out](assets/documents/register_log_in_out.pdf)


### Database Schema 

![Database Schemas can be found here](assets/images/eat-me-schema.png)
*<i>note</i> - I forgot to add a Body section to the Comment table when designing. By the time I realised that I left it out my trial period for the schema creator website had expired so I could not rectify the mistake.

I ended up removing the email field from the comment model in the final build of the site, as I didn't like the overall look of the comment box when it featured the user's email.

[Back to top ⇧](#eat-me)

## Features

### Home Page

- #### Navigation bar
    - The navigation bar is present at the top of every page and houses all links to the various other pages.
    - The active page will be shown to have a bolder font helping users understand what page they're on.
    - Hovering over the links will darken the font.
    - The options to Register or Log in will change to the option to log out once a user has logged in. 
    - Once a user has signed in, more options such as 'Your Recipes' and 'Favourite Recipes' become available.
    - Text will also appear in the bar stating which user is signed in if any.
    - A search bar is nested in the navbar to find recipes quickly.
    - The navbar is fully responsive, collapsing into a hamburger menu when the screen size becomes too small. 

    ![Navbar](assets/images/navbar.png)


- #### Hero Image
    - The hero image welcomes the user with a short message advertising what the website is about.
    - A button to sign up and a short message is present in the image. Clicking this takes you to the register page.
    - If a user is already signed in the message changes to 'welcome back' and the sign up button changes to a 'view recipes' button, which takes you to the all recipes page.

    ![Hero image](assets/images/hero.png)

- #### Carousel
    - The carousel displays any recipes that the admin has selected to be featured.
    - Clicking the image will take you to that recipe's detail page.
    - Buttons on the edge of the carousel scroll through all the featured recipes.

    ![carousel](assets/images/carousel.png)

- #### Most Loved Recipes
    - The most loved recipes section displays the top 5 recipes with the most likes.
    - Clicking each recipe takes you to its detail page.
    - A link to all recipes can be found at the bottom of the list.

    ![most loved](assets/images/most-loved.png)

- #### Features
    - This section displays a couple short messages with images to showcase the site's basic features.

    ![features](assets/images/features.png)

- #### Footer
    - The footer rests at the bottom of each page and has links to all social media accounts.
    - Clicking the links in the footer opens a separate browser to avoid pulling the user away from the site.

    ![footer](assets/images/footer.png)

[Back to top ⇧](#eat-me)

### Accounts
- #### Register Page
    - The register page is used to create an account.

    ![sign up page](assets/images/sign-up-page.png)

- #### Login Page
    - The login page is used to log in users with an existing account.
    - A success message will appear once a user successfully logs in.

    ![sign in page](assets/images/sign-in-page.png)

- #### Log out Page
    - The log out page is used to log out users who are signed in.
    - A success message will appear once a user successfully logs out.

    ![log out page](assets/images/sign-out-page.png)

[Back to top ⇧](#eat-me)

### All Recipes Page

- #### Recipe Cards
    - The site will paginate all recipe cards to display 6 to a page.
    - Each card will display the recipe's image, Title, Author, Description, Published date and how many likes it has received.
    - If the recipe is vegetarian or vegan a small green corresponding label will be present in the bottom left corner.
    - Clicking anywhere inside the recipes card will take you directly to that recipes detail page.

    ![all recipes page](assets/images/all-recipes.png)

### Favourite Recipes Page

- #### Favourite Recipes
    - This page shows only recipes that the user has liked.
    - If a user tries to access this page without being signed in they will receive a not logged in error.

    ![favourite recipes](assets/images/fav-recipes.png)

### Your Recipes Page

- #### Your Recipes
    - This page displays only the recipes that the user has created. 
    - At the top of the page is an 'Add Recipe' button which takes the user to the add recipe page.
    - Each recipe will have two buttons, an edit and a delete button.
    - The edit button will take users to the edit recipe page for that particular recipe.
    - Clicking the delete button will bring up a modal which asks the user if they are sure they want to delete that particular recipe.
    - A success message appears if a recipe is deleted successfully. 
    - If a user tries to access this page without being signed in they will receive a not logged in error. 

    ![your recipes](assets/images/your-recipes.png)

### Searched Recipes Page

- #### Searched Recipes
    - Anything entered into the search bar in the navigation bar displays results here.
    - If the word vegetarian or vegan is entered into the search bar, it will result in all vegetarian or vegan recipes, not just ones with those words in the title. 

    ![search page](assets/images/searched-page.png)

[Back to top ⇧](#eat-me)

### Recipe Detail Page

- #### Recipe Card
    - At the top of the page the recipe card will show the image, title, author, published date and any dietary information.

    ![recipe card top](assets/images/recipe-card-top.png)

- #### Main Section
    - The main body of the page consists of the description, ingredients, and method. These combined is what creates the whole recipe.
    - At the bottom of the section is an icon and counter for both likes and comments.
    - Clicking the outlined heart renders the recipe 'liked' by the user which will then fill in the heart, add 1 to the counter, and add the recipe to the users favourite recipes page.
    - Alternatively, clicking a filled in heart renders the recipe 'unliked' which will then change the heart back to an outline, reduce the counter by 1 and remove the recipe from the user's favourite recipe page.

    ![recipe main section](assets/images/recipe-main-section.png)

- #### Comments
    - At the bottom of the page is the comment section. Here you can view all comments left by users.
    - Only signed in users can leave a comment.
    - Comments with profanity automatically fail and will not upload.
    - Any comments left by the user that is currently signed in can be edited or deleted.
    - A success message appears once comments are left.
    - A success message appears once comments are deleted.
    - If a user tries to edit a comment without being signed in they receive a not logged in error.
    - If a user tries to edit a comment that does not belong to them they receive a forbidden access error. 

    ![comment section](assets/images/comment.png)

### Add Recipe Page

- #### Adding Recipes
    - The adding recipe page is where users upload their creations.
    - Each recipe is uploaded by filling out a form.
    - Failing to fill out either the recipes Title, Description, Ingredients, or Method, results in the form failing and rendering a message stating which fields you have missed.
    - Using profanity will result in the form failing and the relevant section will be flagged with a message.
    - The form has two checkbox's that toggle whether the recipe is suitable for vegetarians or vegans. 
    - Clicking the vegan checkbox automatically checks the vegetarian checkbox and subsequently unchecking the vegetarian box unchecks the vegan box.
    - The user has two options to upload an image of their recipe. They can either choose a file to upload or simply put in the URL address of the image. 
    - If neither of the image options are used a default image will be generated.
    - An add Recipe button is present at the bottom of the page once the form is ready to send.
    - If a user tries to access this page without being signed in they will receive a not logged in error.
    - A success message appears once a recipe is added successfully.  

    ![add recipe page](assets/images/add-recipe-page.png)

### Edit Recipe Page

- #### Editing Recipes
    - Editing a recipe brings up the form that was filled in when the recipe was created and has all the fields filled out with the original content.
    - Changing the content and hitting save at the bottom of the page saves the recipe.
    - A success message appears once a recipe is edited successfully.
    - If a user tries to access this page without being signed in they will receive a not logged in error.
    - If a user tries to edit a recipe that does not belong to them they receive a forbidden access error.

    ![edit recipe page](assets/images/edit-recipe-page.png)

- #### Features to add
    - A star rating system to replace the like button. Users would score each recipe out of 5 with the average reflected as filled stars.
    - Submenus for All Recipes. Sections such as breakfast, lunch, dinner, dessert, or cultural sections such as mediterranean, asian, spanish etc.
    - Option to share recipes on social media.

[Back to top ⇧](#eat-me)

## Technologies

### Languages used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://www.python.org/)

### Libraries and Programs Used

- [Git](https://git-scm.com/)
    - Version control.
- [GitHub](https://github.com/)
    - For storing code and deploying the site.
- [Gitpod](https://www.gitpod.io/)
    - Used for building and editing my code.
- [Django](https://www.djangoproject.com/)
    - A python based framework that was used to develop the site.
- [Bootstrap](https://getbootstrap.com/)
    - For help designing the html templates.
- [Google Fonts](https://fonts.google.com/)
    - Used to style the website's logo.
- [Font Awesome](https://fontawesome.com/)
    - Used to obtain the icons used.
- [Google Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
    - Used to help fix problem areas and identify bugs.
- [Cloudinary](https://cloudinary.com/)
    - Used to store static files and images.
- [Favicon.io](https://favicon.io/)
    - Used to generate the site's favicon.
- [SQlite](https://www.sqlite.org/index.html)
    - Used when performing unit tests.
- [PostgreSQL](https://www.postgresql.org/)
    - Database used through heroku.
- [SmartDraw](https://cloud.smartdraw.com/)
    - To draw out the database schema.
- [Balsamiq](https://balsamiq.com/)
    - To create the wireframes.
- [W3C Markup Validation Service](https://validator.w3.org/) 
    - Used to validate HTML code.
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - Used to validate CSS code.
- [Pep8](http://pep8online.com/)
    - Used to validate Python code.
- [JSHint](https://jshint.com/)
    - Used to validate JS code.
- [Summernote](https://summernote.org/)
    - Used to add a WYSIWYG text box to the add recipe page.
- [Profanity Filter](https://github.com/ReconCubed/django-profanity-filter)
    - App used to remove profanity from recipes and comments.
- [Tinyjpg](https://tinyjpg.com/)
    - Used to compress images.
- [Screen to Gif](https://www.screentogif.com/)
    - Used to create gifs for my readme.
- [Heroku](https://www.heroku.com/)
    - To deploy the project.

[Back to top ⇧](#eat-me)

## Testing 

Testing and results can be found [here](TESTING.md)

## Deployment

This project was deployed using Github and Heroku.

- ### Github 

    To create a new repository I took the following steps:

    1. Logged into Github.
    2. Clicked over to the ‘repositories’ section.
    3. Clicked the green ‘new’ button. This takes you to the create new repository page.
    4. Once there under ‘repository template’ I chose the code institute template from the dropdown menu.
    5. I input a repository name then clicked the green ‘create repository button’ at the bottom of the page.
    6. Once created I opened the new repository and clicked the green ‘Gitpod’ button to create a workspace in Gitpod for editing.

- ### Django and Heroku

    To get the Django framework installed and set up I followed the Code institutes [Django Blog cheatsheet](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf).

    
- ### Forking

    To fork my project you must;
    1. Sign in to Github and go to my [repository](https://github.com/Delboy/Colour-Type)
    2. Locate the Fork button at the top right of the page.
    3. Select this. 
    4. The fork is now in your repositories.

- ### Clone
    To clone my project you must;

    1. Sign in to Github and go to my [repository](https://github.com/Delboy/eatme)
    2. Above the list of files click the green ‘code’ button.
    3. This will bring up a few options as to how you would like to clone. You can select HTTPS, SSH or Github CLI, then click the clipboard icon to copy the URL.
    4. Open git bash
    5. Type ‘git clone’ and then paste the URL you copied. Press Enter.

    For more information on cloning check out the github documentation [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

## Credits

### Code

 -  I learnt how to change the form's field's label in this thread [stackoverflow.com](https://stackoverflow.com/questions/636905/django-form-set-label).

 - I learnt how to reflect the active page in the navbar here on [tekshinobi.com](https://tekshinobi.com/setting-active-navbar-link-in-django-template/).

 - I used this page to help me write unit tests for my admin functions [Google Groups](https://groups.google.com/g/django-users/c/2zN3BlFLIFE).

 ### Media

 - The hero image was taken from [coop.co.uk](https://www.coop.co.uk/recipes/earl-grey-poached-pears-with-ice-cream).
 - All other food images were taken from [bbc.co.uk/food](https://www.bbc.co.uk/food).

 ### Other

 - [The code insitutes](https://codeinstitute.net/) 'I think therefore I blog' project which inspired the overall feel of the paginated and recipe detail pages.
 - The [Django documentation](https://docs.djangoproject.com/en/4.0/) which was instrumental in helping me solve problems.

[Back to top ⇧](#eat-me)