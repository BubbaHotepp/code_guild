# **Capstone Project**

## **Name:** Waiting on confirmation of phrasing of "Our Stories" but I think it's "Nanna poya".com

#

## **PROJECT OVERVIEW**

​

### Discription:

- This is an application to bring together Chickasaw tribal members to enable sharing of historical and familial information. As Chickasaw are spread throughout the United States and as families have grown and spread throughout the years, records and information has become equally spread out and fragmented. The Holisso Research Center at the Chickasaw Cultural center has an incredible collection of books, tribal records, archival records, and photographs available but currently neccessitates travelling to Sulphur Oklahoma to access. This application and site aims to solve many of those issues.

- Through this application it will allow tribal members to access digital versions of archival records, books, and materials remotely while also helping to preserve and protect those records that are light and temperature sensitive by reduced physical access.

  Through a member forum it will create an easily accessible area for members to share stories and information with each other regardless of geographical location.

  And finally, a memorium section will allow tribal members to honor, share photos and tell stories of Chickasaw elders who came before them.

      ### Libraries/Frameworks

  ​ - Django - Will be used for backend web framework. - Bootstrap4 - Will be used for frontend HTML formatting. - Amazon AWS - Will be used for hosting services.
  <span style="color:cadetblue"> if you're going to host this, you should also consider a few things. switch the database to postgres, buy a domain, and figure out if you really want to host through AWS. there are other services and some are easier to use than others.</span>

​

## **FUNCTIONALITY**

​

### PLAY-BY-PLAY ----

### USER:

1. Home Page-- Register, Login/Logout, description with links to various sections as well as weblinks to other Chickasaw services (i.e. Chickasaw.net, Chickasaw.tv etc.)
   ​
2. User Registration Page-- User enters name, email and address information.

   - User data will be stored in the user model database after submission.
   - User will then be redirected to the Home Page.

3. User Profile Page-- Users will be able to provide profile information and a picture if they so desire for other members to view.​

### USER Messaging:

3. Direct Message Inbox-- Users will be able to view and send messages to other users via direct messaging through this page as well as staff responses to user archive submission.

- <span style="color:cadetblue"> this is fine, but consider using django channels instead. the kind of in-app mail systems like that aren't very common or popular anymore. using websockets will get you better functionality, and it will teach you how to use a modern technology.</span>

### USER FORUM:

4. User Forum Page-- Users can post message threads and their repsonses to threads via this page.

- <span style="color:cadetblue"> how are you going to implement the forum? </span>

### ELDER MEMORIAL PAGE:

5. Memorial Home Page-- Main page listing Elders with photo and name info and a user submission link.

6. Elder Page-- Page containing information about each Chickasaw elder.

7. User Elder Submission Page-- Users can submit information and uploads about Chickasaw elders.

### ARCHIVES:

4. Archives Page-- Archival home page listing available materials and formats.

5. Archive Search Page-- Users will be able to enter searchs and access archival materials through this page.

6. Archival Submission Page-- Users will be able to submit materials such as familial photos and documents for review by Archival staff for possible addition to Holisso
   research center archives.

### PLAY-BY-PLAY-end ----

### PAGES:

- Home Page
- Registration page
- User Profile Page
- Inbox page
- Forum page
- Memorial Home page
- Elders page
- User Elder Submission page
- Archives main page
- Archive search page
- Archive submission page

### Functions:

- User Registration form.

- User Authentication.

- Profile Customization.

  - Saves to profile model and allows edits when user is authenticated.

- Archive search page, able to search through Archive database.

  - User is able to filter/order results.

- Direct messaging.

- Forum Bulletin Board.

- Archival staff scan uploads.

- Archival user scan upload submissions.

- Elder profile page customization.

  - Saves data to elder model and allows edits when authored user is authenticated (or staff).

- Forum thread and post creation.

## **DATA MODEL**

- USER MODEL and PROFILE MODEL is One to One

- MESSAGES MODEL is One to Many
  ​
- FORUM MODEL is many to many

- ARCHIVE MODEL:

  - Staff scan upload
  - User scan upload
  - User database search

- User MODEL:

  - Username
  - Password
  - Email
  - First name
  - Last name
  - Address

- Profile MODEL:

  - Profile picture
  - Username
  - User First and Last name

- Elder Model:

  - Name
  - bio
  - photos

- Forum Model:

  - Thread creation
  - Thread posting

- Messages MODEL: django user-to-user system
  - Private messages
  - Forum messages.

#

## **SCHEDULE**

1. WEEK:
   Setup Django backend framework
   Setup templates
   Setup AWS database service
   Setup User Model

2. WEEK:
   Setup Profile Model
   Setup Archive Model
   Setup Forum Model

3. WEEK:
   Setup Elder Model
   Setup Messages Model
   Example Data creation and inclusion
4. WEEK:
   ​ Testing
   After Presentation
   ​
5. WEEK:

6. WEEK:

7. WEEK:

8. WEEK:
   ​

#

​

# INSTRUCTOR NOTES TO WORK ON

- <span style="color:cadetblue"> interesting project and a good idea for a capstone </span>

- <span style="color:cadetblue"> how are you going to store the files? what types of files will you store? how will you retrieve those files after they're stored so other users can view them?</span>

- <span style="color:cadetblue"> I know nothing of the Chickasaw culture. Can their language be displayed using characters available on keyboards? You'll need to make sure you can correctly display the language in a browser. I'm sure you can, but this isn't a language I'm familiar with, so I'm just putting that out there.</span>
  ​
- <span style="color:cadetblue"> are there any apis or other external data sources you can make use of for this project to add additional features or enhance the ones you already have planned?</span>
