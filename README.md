<a name="topofpage"></a>

# pjt3-NoiseAudit

Third Milestone Project - Code Institute 

<img width="712" alt="image" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/b239032a-87d5-4925-a4ed-3b2346884a72">


<hr>

# Table of Contents

*   [Student Details](#student)
*   [Introduction](#intro)
*   [User Experience (UX)](#userexp)
    *   [Design](#design)
    *   [Wireframing](#wireframe)
    *   [User Stories](#userstory)
    *   [Database Schema](#dbschema)
    *   [How To Blog](#how2blog)
*   [Technologies used](#tech)
*   [Testing](#testing)
    *   [HTML](#html)
    *   [CSS](#css)
    *   [Javascript](#js)
    *   [Python](#python)
    *   [Lighthouse](#lighthouse)
    *   [Responsivness](#responsive)
    *   [User Stories Testing](#uitest)
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

Github Repo - [https://github.com/PSebastian96/pjt3-NoiseAudit]

Heroku Deployed Link - [https://noiseaudit-03-eec0b584a334.herokuapp.com]

<hr>

<a name="userexp"></a>
# User Experience (UX)
<a name="design"></a>

### Design :

- Desing of the website is very minimalistic. The primary colours are black, green and white.
<img width="119" alt="color pallette" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/1596275f-bec7-40b7-811a-9ff2c0b23d90">

  
- The colour black is used to style the menu bar and footer.
- Body of the website is black/grey colour.
- The text is mostly green, which pairs with the black background colour.
- Menu links are green when hovered over as well as the footer links.

<img width="229" alt="green pallette" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/8b040696-3c06-4323-98c0-0570c9e39c51">

- Current page view is highlighted when viewed by green colour
<img width="226" alt="image" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/b807a4d5-c1f0-417c-9088-7cb4ab261ae4">

- Current page view highlighted when viewed from registered user's perspective
<img width="359" alt="image" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/c8c060de-54d4-4dc0-8c43-dd954c4e57a2">

- For the Logo, I have used the 'Rubik Distressed' google font family.

<img width="144" alt="Logo font" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/35695192-ab8e-42e1-86e7-32593e0ff4d1">

- For the menu links, 'Henny Penny' google font family is used.

<img width="207" alt="menu font type" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/e374ebc2-a501-4866-93d6-7e7c3b39cde4">

- For the titles, reviews and blog font style, I have used the 'Gloria Hallelujah' google font-family.

<img width="256" alt="general_txt_font" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/d5267c94-f515-4695-8d5c-a08c368d5b99">


<a name="userstory"></a>

### First time visitor goals :

As a first time visitor, I want to give basic information about the website, the purpose and what community this website is made for. In this case, this blogging website is about music lovers and musicians, where users can post reviews about artists, albums, music genre, music scene, criticism and musical instruments & equipment reviews.

- The About Us section is on the top of the page, in order for first time visitors to get the general information about the website and for who it is made for and what's the purpose of the site.

- On the main page the visitor has 3 reviews from frequent users:

<img width="890" alt="image" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/d2a1500e-8a91-4905-b0ff-63667b54e25f">


- Visitor have a accordion F.A.Q. for their curiosity to find more info about the page:

<img width="301" alt="image" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/33b3914f-165e-4e7d-8f15-03e22d50ec13">

- In the Contact section, first time users can send their queries to the website owner.
- Here is the automated reply set up by EMailJS API:

<img width="902" alt="image" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/eab459e7-5f05-41a5-87f6-f0197bdfdf32">

### Frequent user goals :

1. Encourage the user to share and make reviews.

2. Let the users update their blogs. 

3. Connect the members and share with eachother their thoughts via comment section. 

4. Make possible removing and/or update their comments.

5. Encourage members of the community to visit the site frequently by reading, creating and updating 
   their blogs, comments and share new knowledge or music with eachother.

- The user while reading the Blog on medium-large devices, on the top-right side has a box of options to act on the Blog:
<img width="913" alt="image" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/b0a5f7ee-c5d5-4197-adf5-4deda9b27ccf">
 
- On the mobile view this is hidden and instead these options are available on the bottom between the content and comments section:
<img width="316" alt="image" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/9e773dfc-d76b-4bd1-91c1-163892336f8a">

- With the comments, if the user is creator of blog or admin, on the comments there are two options, to delete and edit the comment:
<img width="740" alt="image" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/15ca41d7-3d6a-4c3e-bfe1-5efd7fda7391">

- On the menu section MyBlogs, gives an option for the creators to see their list of published blogs and have CRUD functionalities available.
<img width="895" alt="image" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/395149d3-46c9-43bf-ae10-e846b0d9c1ed">

- Main page Blogs, the users have access to every blog posted on the site, with the search bar on the top the user can search for blogs by categories, titles and text:
<img width="901" alt="image" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/6c4dcf98-1b9a-445b-9090-0c50985aa6ec">

- The registered users can update their profile details on the Profile page and also have the option to delete (Danger Zone) their account:
<img width="317" alt="image" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/9ad72c14-8a8d-497a-b15f-d40a1a0ae98b">

### Admin user:

- Admin user has access to every registered users information and every blog posted on the site.
- Admin has enabled CRUD functions for Creating/Reading/Updating/Deleting blog post and comments.
- Since the admin has access to the registered user list, it can delete any account.

- Admin Dashboard page :

1. <img width="903" alt="image" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/0f63fa08-7b15-4bca-8244-e89a27caa229">

2. <img width="895" alt="image" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/b05ff28a-76ed-4749-962c-2f2051f600d0">

<a name="dbschema"></a>
### Database Schema

- Non-Relational Database (MongoDB) has been used in this project.
- The database collections for this project:
 <img width="220" alt="image" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/af27f9e0-ee34-4109-b037-654008d33b88">

- users database:
<img width="866" alt="image" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/4b2dbb67-2ccd-40d1-b399-c402248acd53">


- blogsdb database:
<img width="937" alt="image" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/cc4b7bac-40a8-467e-b09c-15ee01640663">


- commentsdb database:
<img width="899" alt="image" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/fd0eddb2-f85e-41ff-8575-3e96464e534f">


- categorydb database:
<img width="922" alt="image" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/4e9840b0-2dce-406b-9cbf-295f40e88abb">


- Schema:

<img width="404" alt="image" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/98aa6627-7c78-4c32-9aeb-df9a6003afb8">

- comment_id takes the value of the _id from blogsdb.
- comment_by takes the value of the username in order to record the author of comment.
- username and created_by have the same value to connect the author and users value.
- category_name is used in blogsdb to connect the category of the blog.
  
<hr>

<a name="how2blog"></a>
# How to Blog

## How to post an Audit:

1. Register on the site and log in to your account.
2. On the top right, in the menu bar the "Create" option is available, by selecting the option it will transfer the user to the form to create the blog.
3. Fill all the fields in the form and on the bottom of the page, press the blue button which says SUBMIT AUDIT.
4. The site will flash a message notifying the user that the blog has been posted successfully.
5. The page will load the get_blogs page and by clicking on the READ button, the user can review the blog.

### How to Edit a Blog:
1. If you are the creator, select the My Blogs on the menu bar and you will have the option to Edit or Delete.
2. If it is the admin user, the same applies as step 1.
3. Other way to edit the blog is by selecting READ button and reading the full blog.
4. On the right side there is a little box, which contains options BACK,EDIT,DELETE,COMMENT.
5. Select the EDIT option and the page will load the form to edit the content of the blog.

### How to Delete a Blog:
1. If you are the creator, select the My Blogs on the menu bar and you will have the option to Delete.
2. If it is the admin user, the same applies as step 1.

### How to Comment on a Blog:
1.On the right side there is a little box, which contains options BACK,EDIT,DELETE,COMMENT.
2.Select the Comment option and the page will load the form to edit the comment on the blog.

### How to Edit or Delete a Comment:

- Similar as Editing or Deleting the blog.
- If you are the creator or admin, you will have the option to Edit or Delete your own comments or as admin other users comments.

### How to embed videos in the text editor:

1. For youtube videos, on the bottom of the video select the SHARE button and then press EMBED, copy the link.
2. Within the text editor select SOURCE button.
<img width="576" alt="image" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/a5d42211-c62d-4571-865b-5791b9a9167a">

3. This option will load the HTML version of the content in the text area.
<img width="559" alt="image" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/3f691ed5-97d4-43af-8e61-92f5ca230ca7">

4. Under your content paste the embeded link copied from youtube.
<img width="547" alt="image" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/d80bdb78-f82d-4708-812f-eeffa0a44f17">

5. If you finished the writing just press the SUBMIT AUDIT button to submit the blog.
6. If not done, just carry on within the text area with `<p></p>` elements and make sure to `<p>` use open tag in the beginning and closed `</p>` tag at the end of the text.
7. After that press the SUBMIT AUDIT button to submit the blog.
   
<hr>

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

### Front-end :
  - Materialize [https://materializecss.com]
  - Google fonts [https://fonts.google.com]
  - Font Awesome [https://fontawesome.com]

### Back-end :
  - Python3 [https://docs.python.org/3/]
  - Flask [https://flask.palletsprojects.com/en/2.3.x/#user-s-guide]
  - MongoDB [https://www.mongodb.com/docs/]

### Emailjs API :

- Emailjs - [https://www.emailjs.com]

- Emailjs offers an emailing service for websites. This includes two type of API's : 1. free and personal use of up to 200 session/month and 2. a business API.
  For this project I have signed up for the free/personal use of email service with 200 available sessions/month.
  This API is allowing the developer to receive emails from the forms which are designed for the website for various pourposes.
  The emailjs API makes the following possible:
   
   - The user can fill out the contact form with their details and their query or message.
   - The API connects the "business" or personal email account (gmail,outlook etc) with the websites form and makes it possible to receive the visitors inputs from 
     the same form.
   - API also offers an auto reply mode and it's content is customizable and can fit any business/personal needs for emailing.

 - For any further details about the application of this API, please find the details in the official documentation of the emailjs API [https://www.emailjs.com/docs/].

### Environment Used

1. Github - [https://github.com]
    - Was used to store the repository and files for the project.

2. Codeanywhere - [https://codeanywhere.com]
    - Was used as code editor for the project.

<hr>

<a name="testing"></a>
# Testing

<a name="html"></a>
### HTML

- HTML Validator [https://validator.w3.org]

- Most of the errors/warnings I received from the validator are due to the validator not recognising the Flask-Jinja templating language. Other than that there were no issues with the HTML documents.

<img width="879" alt="image" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/e5a9a410-9974-4f41-b425-8fdf318fe2ec">

<a name="css"></a>
### CSS

- CSS Validator [https://jigsaw.w3.org/css-validator/]

<img width="890" alt="image" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/a8810a74-47ee-4f54-bbf9-7aa1d048e99c">

<a name="js"></a>
### Javascript

- JSHint was used to validate the Javascript code - [https://jshint.com/docs/]

<img width="719" alt="image" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/8b95296e-e35c-4b1d-9950-ef033acfd07a">
  
<a name="python"></a>
### Python

- Pylint was used as python validator [https://pylint.pycqa.org/en/latest/user_guide/usage/run.html]
- Pylint was used within the IDE terminal with pylint "file.py"
- Within the IDE's command line, there were no issues with python code validity and is PEP8 compliant.

<img width="440" alt="image" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/6c91f8f4-eb07-440e-8428-c8fb1ead1e76">

<a name="lighthouse"></a>
### Lighthouse Testing

- Lighthouse is an open-source, automated tool for improving the performance, quality, and correctness of your web apps. [https://developer.chrome.com/docs/lighthouse/overview/]

- Results of testing the index page:
  
<img width="920" alt="image" src="https://github.com/PSebastian96/pjt3-NoiseAudit/assets/123810890/34d75e67-5a27-4cf1-9210-34a0fc9c268d">

<hr>

<a name="responsive"></a>
### Responsivness

Testing was done on three browsers: Chrome & FireFox on laptop and Opera on the below screen sizes:

- iPhone SE (375 x 667)
- iPhone XR (414 x 736)
- iPhone 12Pro (390 x 844)
- Pixel 5 (393 x 851)
- Samsung Galaxy S8+ (360 x 740)
- Samsung Galaxy S20 Ultra (412 x 915)
- Galaxy Fold (280 x 653)
- iPad Air (820 x 1180)
- iPad Mini (768 x 1024)
- Surface Pro 7 ( 912 x 1368)
- Surface Duo ( 540 x 720)

<a name="uitest"></a>
### User Stories Testing

#### First Time User
| First Time User  | Criteria & Features | Outcome/Comments  |
| -------------    | -------------       | -------------     |             
| Have access to basic information     | First time user has access and information on 'About us', Reviews and FAQ section |+PASSED+|
| Website responsivness on devices     | Mobile phone friendly,tablet and large devices responsive   |+PASSED+|
| Easily navigate through site     | Navbar can be found on the top-right side and each page is highlighted when the user visits selected section|+PASSED+|
| Easily understand the purpose of site    | The welcoming text gives a brief summary and invitation for the first time user to join and share their musical interests with other music enthusiasts|+PASSED+|
| Option to Register    | First time user has the Join menu, where by filling out a basic registration form enables the user to become a member and start Bloging|+PASSED+|
| Contact the website administrators for further queries | Thanks to EmailJS API, on the Contact section, the API is used to receive the users query or message and the user gets notified by receiving a automated response email confirming that their query has been sent as well as on the forms bottom section a message is displayed 'Query sent successfully'|+PASSED+|

#### Admin User Goals
| Task | Criteria & Features | Outcome/Comments  |
| -------------    | -------------       | -------------     |   
| Be able to perform basic CRUD operations     | Be able to create, read, update and delete blogs & comments on the website by having access to the same user functions as the creators of the blog or comments |+PASSED+|
| Dashboard    | Admin user has a extra page named 'Dashboard', where the admin can search through database by usernames, blog titles contents and perform 'Delete' functionality on users  |+PASSED+|
| Query through blogs     | On the 'Dashboard' section the admin can search through all the blogs published on the site and perform CRUD functionalities on blogs and by selecting a desired blog and within that, CRUD funcitonalities can be performed on comments |+PASSED+|
| Defensive programming | Modals have been put in place in order to avoid deleting blogs, comments or users by mistake, by each delete request a modal is triggered and asks the admin if the choice wants to be done and warns about the consequences of the action|+PASSED+|
| Oversee the content |  The admins role to oversee content on the website is made possible by having access to all CRUD functionalities on each blog, every comment and users accounts, the admin can manipulate every content or delete a user in case of violation of the sites policy|+PASSED+|

#### Member User Goals
| Task | Criteria & Features | Outcome/Comments  |
| -------------    | -------------       | -------------     |
| Update Profile Details | Registered member on the 'Profile' page has access to edit personal details such as first, last name, email address |+PASSED+|
| Delete Account | Registered member on the 'Profile' page has access to permanently delete their account, by deleting the account the user loses all access to the blogs and also is popped out of session therefore the same information will be available as to the first time user |+PASSED+|
| Create Blog | Registered member on the 'Create' page has access to the form, which by filling out creates the blog and after the submit button the blog is created and pushed to the database. The user also has an option to create a blog on the 'Profile' page, making it more accessible to create a blog |+PASSED+|
| Read blog | Registered member by selecting 'Blogs' option can access all the blogs published on the website and the blogs are ordered by latest date |+PASSED+|
| Text editor | Within the form for blog creation, CKEditor has been used, which is a general purpose text editor and makes it easy for the user to enter the text, change fonts and also include youtube videos or pictures in the blog |+PASSED+|
| Update blog | If the user is the author of a blog, has 2 options to edit the blog, one by reading the blog and on the right side have a helper which allows the user to comment, edit or delete the blog. By selecting the 'EditBlog' the user can add or remove content from the blog |+PASSED+|
| Delete blog | Registered user by reading the blog, on the right side will have a helper box with options to go back, comment, edit or delete the blog. Thus by selecting 'DeleteBlog' a modal is triggered to warn the user that the blog is about to be deleted and to confirm the deletion the user must select 'Delete' or has the option to cancel which will redirect the user to Read Mode of the blog |+PASSED+|
| Comment | Registered users can leave comments on every blog and also if the user is the author of the comment, the user will have access to 2 buttons Edit and Delete, which allows the Update and Delete elements of the CRUD functions |+PASSED+|
| Delete Comment | Registered user by deleting their comment are warned by a modal about the action and have the option to cancel or to go forward with the action |+PASSED+|
| Search Blogs | Registered users can query the blog list of published blogs by blog title, author and content within the blog if search criteria doesnt match it will throw a message 'No Audits Found' |+PASSED+|

#### Features
| Task | Criteria & Features | Outcome/Comments  |
| -------------    | -------------       | -------------     |
| Contact Page | On the Contact page the registered member can contact the administration of the website with any queries they might have, by sending the message the user gets notified if the query has been sent and receives an automated response to the email address that is passed in the contact form |+PASSED+|
| Flash Messages | Flash message method have been used to let the user know if the requested action was succesfull, which can be found between the navbar and content of the website when a particular action is executed (post blog, edit, delete or login and out of the website)  |+PASSED+|
| Logout Flash Message | Flash messages tells the user that they have been logged out of the website |+PASSED+|
| Security Test   | In order to access any CRUD elements of the website, the user has to be registered, otherwise if the user tries to manipulate the url link to access any page will be thrown a flash message saying either not having access or must be logged in to access the link |+PASSED+|

<a name="sources"></a>
# Sources

### WTF-forms

- WTF form package [https://flask-wtf.readthedocs.io/en/0.15.x/install/]

### CKEditor

- Text editor used with Flask [https://flask-ckeditor.readthedocs.io/en/latest/]

### Flask Error Handling

- 404 & 500 Error Handlers - [https://pythonprogramming.net/flask-error-handling-basics/#:~:text=wrapper%20above%20it.-,app.,function%20to%20render%20a%20404.]

### Flask -current page view:

- [https://stackoverflow.com/questions/21498694/flask-get-current-route]
- [https://python-web.teclado.com/section12/lectures/03_base_template_and_nav_bar/]

### Images

- Pexels [https://www.pexels.com]

### Wireframe

- Diagrams [https://app.diagrams.net]

### Responsivness

- Responsive Images made with Am I Responsive? [https://ui.dev/amiresponsive]

<hr>

<a name="deploy"></a>
# Deployment

### Heroku Deployment 

The project was deployed on Heroku from the master branch. 
In order to successfully deploy the project, the following is necessary:

1. create a requirements.txt and Procfile within the CLI :

a. -- pip3 freeze --local > requirements.txt (contains all the Flask packages) <br>
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

### Make a clone of Git Repo
1. Select the Repo you wish to clone in GitHub
2. Click on the code dropdown button
3. Copy the https link to your clipboard
4. Open your gitpod workspace
5. In the terminal type "git clone" and paste the copied link
6. Hit enter to create the clone
7. To install the required packages type pip install -r requirements.txt into the command line
8. To view what the code will look like in a browser from here type "python3 app.py" into the console and hit enter or replace "app.py" with your `filename.py`
9. A pop-up will appear stating "A service is available on Port 8080" select Open Browser

<a name="acknowledgements"></a>
# Acknowledgements

-   Tutor support at Code Institute for their support.

-   City of Bristol College for their support and help with my studies.
