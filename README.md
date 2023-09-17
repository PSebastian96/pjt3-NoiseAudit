<a name="topofpage"></a>

# pjt3-NoiseAudit

Third Milestone Project - Code Institute 

<hr>

# Table of Contents

*   [Student Details](#student)
*   [Introduction](#intro)
*   [User Experience (UX)](#userexp)
    *   [User Stories](#userstory)
    *   [Design](#design)
    *   [Wireframing](#wireframe)
*   [Technologies used](#tech)
*   [Content Sources](#sources)
*   [Deployment](#deploy)
*   [Acknowledgements](#acknowledgements)

<hr>

<a name="student"></a>
# Student Details

Name: Szebasztian Pintyer

Student ID: 715159

Institution: City of Bristol College (https://www.cityofbristol.ac.uk) in partnership with Code Institute (https://codeinstitute.net) 

<hr>

<a name="intro"></a>
# Introduction

Welcome to my third project milestone's readme file!

NoiseAudit is a music oriented blogging site, where visitors of the site can join, create an account and publish blogs, reviews about: musical instruments, equipment and albums/artists.

This project is part of the third milestone project within the course from City of Bristol College in partnership with Code Institute.

The third milestone project's objective is to make a website that contains frontend and backend technologies with focus on the backend with python and flask framework. This enables to create a fully functional website, where users can join a website and interact with the content found on the website. 

<hr>

<a name="userexp"></a>
# User Experience (UX)
<a name="userstory"></a>

### First time visitor goals :

### Frequent user goals :

<a name="design"></a>
<a name="wireframe"></a>
## Wireframing :
### Large screen view : 
### Tablet view : 
### Phone view :
## Site map :
## Visuals :

<hr>

<a name="tech"></a>
# Technologies Used

### Languages Used :
  - HTML [https://developer.mozilla.org/en-US/docs/Web/HTML]
  - CSS [https://developer.mozilla.org/en-US/docs/Web/CSS]
  - Javascript/JQuery [https://api.jquery.com]
  - Python3 [https://docs.python.org/3/]

#### Front-end :
  - Materialize [https://materializecss.com]
  - Google fonts [https://fonts.google.com]
  - Font Awesome [https://fontawesome.com]

### Back-end :
  - Python3 [https://docs.python.org/3/]
  - Flask [https://flask.palletsprojects.com/en/2.3.x/#user-s-guide]
  - MongoDB [https://www.mongodb.com/docs/]

### Environment Used

1. Github - [https://github.com]
    - Was used to store the repository and files for the project.

2. Codeanywhere - [https://codeanywhere.com]
    - was used as code editor for the project.

<hr>

<a name="sources"></a>
# Sources


<hr>

<a name="deploy"></a>
# Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
    - Alternatively Click [Here](https://raw.githubusercontent.com/) for a GIF demonstrating the process starting from Step 2.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://github.com) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

<hr>

### Heroku Deployment 

The project was deployed on Heroku from the master branch. 
In order to successfully deploy the project, the following is necessary:

1. create a requirements.txt and Procfile within the CLI :

a. -- pip3 freeze --local > requirements.txt <br>
b. -- echo web: python app.py > Procfile

2. Sign in to Heroku and create a new app.

Select Deploy tab, then Deployment Method and select Github. <br>
Under Connect to Github enter your details and connect your repository. <br>
Followed by settings and select Config Vars and then Reveal Config Vars.

3. In Config Vars use the env.py file variables and values:

-- IP : 0.0.0.0 <br>
-- PORT : 5000 <br>
-- DATABASE_URI : [your_db_URI] <br>
-- SECRET_KEY : [your_secret_key]

4. Under the Deploy tab go to Automatic Deploys and press Enable. <br>
5. Under Manual Deploy, choose Master and click Deploy Branch.
Heroku will begin building the app. When it is ready, you can click Open app to launch it.

<a name="acknowledgements"></a>
# Acknowledgements

-   Tutor support at Code Institute for their support.

-   City of Bristol College for their support and help with my studies.