Final Build Hosted on Heroku -- [Resume Database](https://cvstorage.herokuapp.com/)

This project is a basic database where employees in a recruitment company can add their clients resumes and have them stored in an SQL database.

## User Experience (UX)

-   ### User stories
    
    -   #### User Goals
        As a User I want:
        1. To unserstand how to use easily navigate the website.
        2. To be able to have access to all the resumes.
        3. To be able to add a new resume.
        4. To be able to update/edit or delete a resume.
        5. To be able to search for any resume by name.
        

        
## Features

-   The user has access to all the resumes by clicking on the "Resumes" button on the navigation bar. The resumes are displayed on cards that include an default image and resume name. 

-   The user can add a new resume by clicking on the "Add Resume" button on the navigation bar.

-  Eight resumes are displayed per page, the next page can be accessed by clicking the page numbers at the bottom.

-   The user can edit/update or delete a resume by clicking on the "edit" or "delete" buttons. The buttons are located be at the bottom of each resume page.

-   The user can use a search bar to look for a person by name. The search bar is located in the "Resumes" page.

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used

1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the "Josefin Sans" and "Open Sans" fonts into the style.css file, which are the fonts used in this project.
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the project's code after being pushed from Git.
1. [Figma:](https://figma.com/)
    - Figma was used to create the wireframes for this project.
1. [Pymongo:](https://pymongo.readthedocs.io/en/stable/#)
    - The PyMongo library was used for interaction with the MongoDB database through Python.
1. [jQuery:](https://jquery.com/)
    - jQuery was used to make certain Bootstrap components to function.
1. [Bootstrap:](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
1. [Flask:](https://flask.palletsprojects.com/en/1.1.x/)
    - Flask was the micro framework used to build the application.
1. [MongoDB:](https://mongodb.com/)
    - MongoDB Atlas was the database service used to store the project's data.
    
## Testing

The two services used to validate the code in this project and to ensure there were no syntax errors were W3C Markup Validator and W3C CSS Validator.

-   [W3C Markup Validator](https://validator.w3.org/) - [Results](https://validator.w3.org/nu/?doc=http%3A%2F%2Fthe-food-library.herokuapp.com%2F)
-   [W3C CSS Validator](http://jigsaw.w3.org/css-validator/) - [Results](http://jigsaw.w3.org/css-validator/validator?uri=http%3A%2F%2Fthe-food-library.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) (By direct input, the css code passes without any errors.)



## Deployment

### Deployment to Heroku

This project was deployed to Heroku. Find the steps bellow:

1. Install Heroku on Gitpod (npm install -g heroku)
2. Go to Heroku webpage and create a new app
3. Go to the app Settings, choose Reveal Config. Vars and set the IP, PORT and MONGO_URI variables
4. Login to Heroku from Gitpod
5. Check if the app was created successfully (heroku apps)
6. Create requirements.txt file
7. Create Procfile (echo web: python nameOfPythonFile.py > Procfile)
8. Commit to Github
9. Create a remote to my local repository (heroku git:remote -a appName)
10. Push to Github and Heroku simulataneously (git push && git push heroku master)

To deploy new code I simply type the command "git push". This is possible because my Github and Heroku profiles are connected and the option to deploy to heroku automatically has been enabled. 

If the automatic deployment is not enabled, the alternative is to follow steps number 9 and 10 from the previous list:
- Create a remote to my local repository (heroku git:remote -a appName)
- Push to Github and Heroku simulataneously (git push && git push heroku master)	
