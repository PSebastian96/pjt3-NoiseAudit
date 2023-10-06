<a name="topofpage"></a>

# pjt3-NoiseAudit

Third Milestone Project - Code Institute 

<hr>

# Table of Contents

*   [Student Details](#student)
*   [Introduction](#intro)
*   [User Experience (UX)](#userexp)
    *   [Design](#design)
    *   [User Stories](#userstory)
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

The third milestone project's objective is to make a website that contains frontend and backend technologies with the backend: python and flask framework, while creating a web app that focuses on the CRUD (Create, Read, Update, Delete) functionalities and user interactivity. This enables to create a fully functional website, where users can join a website and interact with the content found on the website.

<hr>

<a name="userexp"></a>
# User Experience (UX)
<a name="design"></a>

### Design :

- Desing of the website is very minimalistic. The primary colours are black, green and white.
- The colour black is used to style the menu bar and footer.
- Body of the website is black/grey colour.
- The text is mostly green, which pairs with the black background colour.
- Menu links are green when hovered over as well as the footer links.
- For the Logo, I have used the 'Rubik Distressed' google font family.
- For the menu links, 'Henny Penny' google font family is used.
- For the titles, I have used the 'Gloria Hallelujah' google font.

<a name="userstory"></a>

### First time visitor goals :

As a first time visitor, I want to give basic information about the website, the purpose and what community this website is made for. In this case, this blogging website is about music lovers and musicians, where users can post reviews about artists, albums, music genre, music scene, criticism and musical instruments & equipment reviews.

### Frequent user goals :

1. Encourage the user to share and make reviews.

2. Let the users update their blogs. 

3. Connect the members and share with eachother their thoughts via comment section. 

4. Make possible removing and/or update their comments.

5. Encourage members of the community to visit the site frequently by reading, creating and updating 
   their blogs, comments and share new knowledge or music with eachother.

<a name="wireframe"></a>
## Wireframing :

### Site map :

1. Non member web view:
<img width="497" alt="blog_non_user_view" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/a27a25fe-fee4-4750-8712-20922552a3b9">


2. Member web view:
<img width="491" alt="blog_user_view" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/f2080d44-2358-4600-90b3-923b5ec2198c">


### Large screen view :
<img width="382" alt="image" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/d5d70c6f-cf0d-415d-940d-fcd1181d70ea">


### Tablet view : 
<img width="382" alt="image" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/7319d35c-2f59-4602-8dbb-5ec6b499e21b">


### Phone view :
<img width="166" alt="image" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/12835689-88f4-4203-b01b-d3a72a3770e1">


## Visuals :
### Large screen view : 
<img width="610" alt="large_view" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/ce799fd1-6cc5-4dcd-9a17-8b050df0c901">


### Tablet view : 
<img width="265" alt="tablet_view" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/5f6a326c-9840-4091-a22e-57ffb72b42d1">

### Phone view :
<img width="208" alt="mobile_view" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/24306afa-33cc-43fc-bb36-4f9d2be44ed8">


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

<a name="dbschema"></a>
# Database Schema


<hr>

<a name="testing"></a>
# Testing

### HTML

### CSS

### Javascript

### Python

<hr>

<a name="sources"></a>
# Sources

### WTF-forms

- WTF form package [https://flask-wtf.readthedocs.io/en/0.15.x/install/]

### CKEditor

- Text editor used with Flask [https://flask-ckeditor.readthedocs.io/en/latest/]

### Flask Error Handling

- 404 & 500 Error Handlers - [https://pythonprogramming.net/flask-error-handling-basics/#:~:text=wrapper%20above%20it.-,app.,function%20to%20render%20a%20404.]

### Images

- Pexels [https://www.pexels.com]

### Wireframe

- Diagrams [https://app.diagrams.net]

### Responsivnes

- Responsive Images made with Am I Responsive? [https://ui.dev/amiresponsive]

<hr>

<a name="deploy"></a>
# Deployment

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
