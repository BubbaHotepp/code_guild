# **Capstone Project**

## **Name:** Waiting on confirmation of phrasing of "Our Stories" but I think it's "Nanna poya".com

#
## **PROJECT OVERVIEW**
​
### Discription:
- This is an application to bring together Chickasaw tribal members to enable sharing of historical and familial information.  As Chickasaw are spread throughout the United States and as families have grown and spread throughout the years, records and information has become equally spread out and fragmented.  The Holisso Research Center at the Chickasaw Cultural center has an incredible collection of books, tribal records, archival records, and photographs available but currently neccessitates travelling to Sulphur Oklahoma to access.  This application and site aims to solve many of those issues.

- Through this application it will allow tribal members to access digital versions of archival records, books, and materials remotely while also helping to preserve and protect those records that are light and temperature sensitive by reduced physical access.  
  
  Through a member forum it will create an easily accessible area for members to share stories and information with each other regardless of geographical location.  
  
  And finally, a memorium section will allow tribal members to honor, share photos and tell stories of Chickasaw elders who came before them.  

    ### Libraries/Frameworks
​
    - Django - Will be used for backend web framework.
    - Bootstrap4 - Will be used for frontend HTML formatting.
#
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

3. User Profile Page--  Users will be able to provide profile information and a picture if they so desire for other members to view.​

### USER Messaging:
3. Direct Message Inbox-- Users will be able to view and send messages to other users via direct messaging through this page as well as staff responses to user archive submission.s

### USER FORUM:
4. User Forum Page-- Users can post message threads and their repsonses to threads via this page.

### ELDER MEMORIAL PAGE:
5. Memorial Home Page-- Main page listing Elders with photo and name info and a user submission link.

6. Elder Page-- Page containing information about each Chickasaw elder.

7. User Elder Submission Page-- Users can submit information and uploads about Chickasaw elders.

### ARCHIVES:
4. Archives Page-- Archival home page listing available materials and formats.

5. Archive Search Page-- Users will be able to enter searchs and access archival materials through this page.

6. Archival Submission Page--  Users will be able to submit materials such as familial photos and documents for review by Archival staff for possible addition to Holisso
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

- Messages MODEL: django user-to-user system
    - Private messages 
    - Forum messages.

#
## **SCHEDULE**
1. WEEK:

2. WEEK:

3. WEEK:

4. WEEK:
​
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
​
