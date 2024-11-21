
# AI Heroes

Here is a link to the live project: [AI Heroes](https://8000-monikamak-aiheroespp4-y4ys4ixf98g.ws.codeinstitute-ide.net/)

AI Heroes is a platform designed to demystify AI by showcasing powerful, user-friendly AI tools that improve daily life efficiency and productivity. The website aims to bridge the gap for users familiar with the term "AI" but seeking practical, accessible examples of its use.

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
   * [Home Page](#home-page)
   * [AI Tools Page](#ai-tools-page)
   * [Voting and Ranking](#voting-and-ranking)
   * [About Page](#about-page)
   * [Contact Page](#contact-page)
   * [Features to Add](#features-to-add)

- [Technologies](#technologies)
   * [Languages Used](#languages-used)
   * [Libraries & Programs Used](#libraries-and-programs-used)

- [Testing](#testing)

- [Deployment](#deployment)
   * [Deployment Process](#deployment-process)
   * [Forking](#forking)
   * [Clone](#clone)

- [Credits](#credits)
   * [Code](#code)
   * [Media](#media)

---

## User Experience (UX)

AI Heroes visitors are individuals curious about AI, eager to explore its applications through straightforward examples and easy-to-understand explanations. They are looking for insights and guidance into the best AI tools available.

## User Stories

A list of user stories grouped into epics for better structure and clarity.

### EPIC | User Experience and Interface
- As a visitor, I want the website to be visually appealing and easy to navigate so that I have an enjoyable experience while exploring AI tools.
- As a visitor, I want to view the homepage so that I can learn about the website and the AI tools it features.
- As a visitor, I can navigate the website with ease so that I have an enjoyable experience exploring AI tools.
- As a user, I want to see tools in paginated format so that I don’t have to scroll through a long list of tools.
- As a visitor, I want to receive feedback (success/error messages) after completing actions so that I understand the outcome of my interaction.
- As a visitor, I want to access an error page with an option to navigate back to the homepage.
- As a visitor, I want to see social media links to follow the project and its author online. 

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

[Back to top ⇧](#ai-heroes)


 # *DONE UP TO HERE*


## Design

The look of this website was based loosely around The Code Institute's 'Codestar' wlakthorguh project as well as [EatME](https://eatme-production.up.railway.app/), project that cought my attention due to it's classy and clean looking style, felt very inspired. 

### Colour Scheme

- # *PLACEHOLDER*

### Typography
- The **Audiowide** font is used as the primary typeface, chosen for its retro style that complements the futuristic and technological concept of AI Heroes. It gives the site a unique personality while remaining readable and visually appealing

### Imagery

- The **main image** features a matrix-style blue background with a superhero robot flying across, representing the fusion of futuristic ideas and AI technology.

- **Illustrative Elements**:  
  Additional robot-themed images are used throughout the site to emphasize the blog's core theme. For example:
  - A robot holding a trophy symbolizes the leaderboard and the ranking of AI tools, highlighting hierarchy and competition.
  - Futuristic visuals and icons help maintain consistency with the blog's modern AI narrative.
  
These design choices work together to immerse visitors in the world of AI while keeping the interface clean and engaging.

### Wireframes
- # *PLACEHOLDER*

Wireframes for each page are linked here:
<!-- 
* [Home Page](assets/documents/home_page.pdf)
* [All Recipes](assets/documents/all_recipes.pdf)
* [Detailed Recipe](assets/documents/detailed_recipe.pdf)
* [Your Recipes](assets/documents/your_recipes.pdf)
* [Favourite Recipes](assets/documents/favourite_recipes.pdf)
* [Searched Recipes](assets/documents/searched_recipes.pdf)
* [Add Recipe](assets/documents/add_recipe.pdf)
* [Register, log in/out](assets/documents/register_log_in_out.pdf) -->


### Database Schema 

![Database Schemas can be found here](assets/images/ai-heroes-schema.png)

[Back to top ⇧](#ai-heroes)

## Features

### Home Page
- **Hero Section**:  
  A visually striking hero section welcomes users with a title and a brief explanation of the website's purpose. This section draws attention to AI Heroes' mission of making AI accessible and practical for everyday use.

- **Navigation Bar**:  
  A responsive navigation bar is present across all pages, providing easy access to key sections such as Home, Leaderboard, About, and Contact. The navigation bar includes links to login and register for imediate action and engagement.

- **Introductory Content**:  
  A concise introduction explains the website's goals, targeting users who are curious about AI and its practical applications.

- **Call-to-Action Buttons**:  
  Buttons encourage users to explore tools, learn more about the site, or connect with the team.

### AI Tools Page

- **Card Display Format**:  
  AI tools are presented in a card format, each card featuring:
  - Tool Name
  - A brief description
  - Voting buttons to express user preference
- **Pagination**:  
  Tools are paginated, with a manageable number of tools displayed per page, ensuring optimal readability and navigation.

### Voting and Ranking

- **Voting Mechanism**:  
  Users can vote on their favourite tools by clicking a vote button on each tool card.

- **Dynamic Ranking**:  
  Tools are ranked based on the number of votes they receive, helping users identify the most popular and impactful tools.

- **Vote Monitoring**:  
  Admin can monitor and manage votes to ensure fair play and prevent misuse.

### About & Contact Page
The **About & Contact page** is designed to foster meaningful connections and encourage user engagement by combining two essential sections: the introduction of the blog owner and an easy way to reach out. By merging these sections, users who visit to learn more about the blog are naturally presented with the opportunity to communicate, and those seeking to contact the owner are more likely to read the "About" section, creating a stronger sense of connection.
- **Purpose Highlight**: 
  The page introduces the blog owner and outlines the mission and vision of AI Heroes, highlighting the importance of making AI tools accessible and useful to everyone. Immediately below the "About" section, users can find the contact form, simplifying the process of reaching out.

- **Visuals**:
  A profile image of the blog owner is prominently displayed, adding a personal touch and helping to establish trust and rapport with the audience. 
- **Contact Form**:  
  The contact form is straightforward, allowing users to easily send queries or feedback. The form includes:
  - Name
  - Email
  - Message

- **Feedback Messages**:  
  After submitting the form, users receive clear feedback with success or error messages, ensuring they understand the outcome of their inquiry and feel reassured their communication has been handled properly.


### Features to Add
- **Tool Recommendations**:  
  A recommendation engine to suggest AI tools based on user preferences or browsing history.

- **User Profiles**:  
  Allow users to create accounts, save their favorite tools, and manage their interactions on the site.

- **Search and Filtering**:  
  Enhanced search functionality with filtering options to sort tools by categories, popularity, or user ratings.

- **Tool Reviews and Ratings**:  
  Enable users to leave reviews and rate tools for more detailed feedback.

- **Social Media Integration**:  
  Options to share AI tools directly on social media platforms.

[Back to top ⇧](#ai-heroes)


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
<!-- - [SmartDraw](https://cloud.smartdraw.com/)
    - To draw out the database schema. -->
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
<!-- - [Profanity Filter](https://github.com/ReconCubed/django-profanity-filter)
    - App used to remove profanity from recipes and comments. -->
- [Tinyjpg](https://tinyjpg.com/)
    - Used to compress images.
- [Screen to Gif](https://www.screentogif.com/)
    - Used to create gifs for my readme.
- [Heroku](https://www.heroku.com/)
    - To deploy the project.
- [Canva](https://www.canva.com/)
    - Used for robot and  background images as well as inspiration.
- [ChatGPT](https://chatgpt.com/)
    - Used for general queries and quick help.

[Back to top ⇧](#ai-heroes)

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
    1. Sign in to Github and go to my [repository](https://github.com/monika-mak/AI-Heroes-PP4)
    2. Locate the Fork button at the top right of the page.
    3. Select this. 
    4. The fork is now in your repositories.

- ### Clone
    To clone my project you must;

    1. Sign in to Github and go to my [repository](https://github.com/monika-mak/AI-Heroes-PP4)
    2. Above the list of files click the green ‘code’ button.
    3. This will bring up a few options as to how you would like to clone. You can select HTTPS, SSH or Github CLI, then click the clipboard icon to copy the URL.
    4. Open git bash
    5. Type ‘git clone’ and then paste the URL you copied. Press Enter.

    For more information on cloning check out the github documentation [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

## Credits


### Code

 -  I learnt how to ..... [youtube](link).

 ### Media

 - All images were taken from [canva](https://www.canva.com/).

 ### README 

 - readme was modeled from [Eat-Me](https://github.com/Delboy/EatMe/blob/main/README.md)

 ### Other

 - [The code insitutes](https://codeinstitute.net/) 'I think therefore I blog' project which inspired the overall feel of the paginated and recipe detail pages.
 - The [Django documentation](https://docs.djangoproject.com/en/4.0/) which was instrumental in helping me solve problems.

[Back to top ⇧](#eat-me)