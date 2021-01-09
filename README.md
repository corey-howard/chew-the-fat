# H1 Heading
## H2 Heading
### H3 Heading
#### H4 Heading

---

## Lists

1. A list with Numbers
2. A list with Numbers
3. A list with Numbers

* A list with bulletpoints
* A list with bullet points
* A list with bulletpoints

---

## Links and images

[A link to github](https://github.com)
![alt text here](icon.png)

# Third Milestone Project - Chew The Fat

Welcome to Chew the Fat, a place for curious minds to learn Cockney Rhyming Slang, or for veterans in the art of speaking
Chitty Chitty Bang Bang (Cockney Rhyming Slang), to add to the ever expanding dictionary for all to see. Perhaps you've visited
London on a day trip, had a confusing conversation with a Black Cab driver, and thought "What was that all about?". Or maybe
heard a phrase on telly, most notoriously on Only Fools and Horses, and thought "What's a Pony?". This is where Chew The Fat
comes in!

I decided to make this site because I have always had a keen interest in Cockney Rhyming Slang and it's origins.
The language is believed to have been created for a few reasons, some of which include; market traders wanting to converse between
each other without onlookers knowing what is being said, providing a sense of community by having their own language only
locals knew, but the most common reason is known to be for criminals to communicate with each other without Police
knowing what is being said. What I find fascinating is that it is still used to this day, there are so many terms that we would all
use in our day to day conversations, not knowing that it is derived from Cockney Rhyming Slang. 

## Table of Contents

1. [UXD - User Experience Design](#1.-uxd---user-experience-design)
    * [Strategy](#strategy)
    * [User Stories](#user-stories)
    * [Scope Plane](#scope-plane)
    * [Structure Plane](#structure-plane)
    * [Skeleton Plane](#skeleton-plane)
    * [Wireframes](#wireframes)
    * [Surface Plane](#surface-plane)

2. [Features](#2.-features)
    * [Existing Features](#existing-features)
    * [Features left to implement](#features-left-to-implement)

3. [Technologies Used](#3.-technologies-used)

4. [Testing](#4.-testing)

5. [Deployment](#5.-deployment)
    * [How to run this project locally](#how-to-run-this-project-locally)

6. [Credits](#6.-credits)
    * [Content](#content)
    * [Media](#media)
    * [Code](#media)
    * [Acknowledgements](#acknowledgements)

## 1. UXD - User Experience Design

---

### Strategy

---

The purpose of this site is to create a dictionary of rhyming slang terms and their definitions, potential users may have heard 
a term that they are not familiar with and can find it on this site. Users are encouraged to make accounts and add terms/definitions 
to the site to expand on the ever-growing database. The site should be simplistic and have the information that the user is searching
for straight in front of them on the first page. There should also be minimal content to read from the start of the start, as the user
has come to this site for a quick answer to a question and are not there to read a backstory to the site's existence.

As the site owner, going forward, it would be great to turn it into more of a platform for socialising. Perhaps adding a forum/chat
funtionality. It could become a place for users to converse about London life, share experiences and of course continue to expand on
the Cockney Rhyming Slang dictionary. These actions can be implemented along side the main focus of the website being a dictionary, to
perhaps bring in revenuse by eventually advertising tourist attractions and forwarding users to ticket sales for these attractions as
an example.

#### User Stories

* As a new user I want to be presented with a simple, enjoyable and easy to use site, that is also visually appealing.
* As a new user I want to be able to navigate around the site with ease.
* As a new user I want to be able to easily find the slang term I am looking for, via a logical ordering system.
* As a new user I would like the option to add to the dictionary of slang terms.
* As a new user I want to have access to the slang terms/defintions i've created and have the option to edit/remove them.
* As a new user I want to enjoy using the site enough to want to return.
    
* As a returning user I want all the requirements as a new user.
* As a returning user I want to be able to see that any new slang terms have since been added in a logical order.

* As a frequent user, going forward I would like to be able to interact with other users on the site on a social level.
* As a frequent user, going forward I would like to be able to see recommendations for tourist attractions in London.

---

### Scope Plane

---

#### Functional Specifications

* The functional specifications will mostly follow the information set out in the user stories.

#### Content Requirements

* The user will be immediately faced with a simplistic site, with all the slang terms on the first page they reach.
* There will be easy to follow navigation with limited pages to choose depending on if the user is logged in or not.
* The Background will be fitting for the sites purpose and not distracting.
* The colour scheme and font choices used throughout the site will be complimentary of each other and display clearly for users
on all devices. The aim is not to be flambouyant in this case, the purpose is to provide clear and concise content for the user
and maintain consistent at all times.
* With simplicity in mind and taking into consideration all the points above, the site still needs to fill like it belongs to
it's purpose and makes sense. For example, it is a dictionary for a language originating from London, so a bright, rural theme/feel
probably wouldn't fit.
* The site will include it's main funtionality of being a dictionary search tool and, for users to be able to create accounts and
add slang terms themselves from the initial site creation. Future content could include forums, chat functionalities, advertising
or even sale of merchandise.

---

### Structure Plane

---

The site has been structured with the user in mind from the offset. Simplicity has been reiterated a lot so far but it has been
at the forefront of every idea and design aspect for this site. To achieve this, I decided to use Materialize as I think it
provides very straight-forward styling that is easily achieved. I will explain in more detail the structure of each component that
makes up the site in the following Skeleton Plane section, as I believe it links better with how the information is represented
via the wireframes. However, the basic structure logistically can be described in the following priorities:

1. The first page that is presented to the user is the Home page, which contains all the slang terms they have come to find.
2. The first page should be designed in such a way that makes it clear what it is straightaway.
3. The logo and navigation bar will be present at the very top of the page horizontally, logo central, navigation buttons to the right
with the most commonly used buttons/pages displayed left to right.
4. As the name of the site isn't inherently clear as to what the site does, the heading will displayed directly below the top nav-wrapper.
5. An alphabet that includes href links for users to navigate to slang terms beginning with the letter they choose will be displayed
next, before the dictionary begins.
6. The dictionary will then be displayed, with all terms separated by large headers of the corresponding starting letter to the term.
The slang term will come first, followed by it's definition. Each slang term will be within a materialize collapsable which displays
more information when clicked on, such as the name of the user who created the entry and the date it was created on.
7. The next page along in the navigation will be the Log In page, for user to log in and add slang entries..
8. The next page along in the navigation will be the register page, for users who wish to add slang entries to the site, they must
register an account to do this.
9. When a user is logged in the Add Slang page will appear on the navigation bar, this is to prevent users adding slang entries without
an account.
10. The other page that is available to users is their Profile page, here will be an explanation as to what a user has access to on the
site. Also available are navagation buttons to return back to the Home page or the option to Add Slang.
11. Lastly, the Log Out button will be available at the end of the navigation bar, only for users that are logged in, to log out.

---

### Skeleton Plane

---

I used Wireframes when designing how the information will be represented and how the user will be able to navigate across the site.
Once the wireframes were created, I had a clear direction on where to begin creating the site and what pages should be created thereafter.
As the contents of the dictionary and the information of the sites user accounts are stored as data and retrieved from a database, 
I also designed how the database would work for the site. I decided to use MongoDB which is a NoSQL document-oriented database.
The database is quite simple and named cockney_rhyming_slang, it is comprised of two collections, one named words and the other users. 
All the slang entries created are stored/retrieved in the words collections and all the user account details are stored/retrieved in the 
users collection. The structuring of these collections can be viewed in the images below:

cockney_rhyming_slang.words:

![Words Collection](static/images/words-collection.png)

cockney_rhyming_slang.users:
(Password manipulated so cannot be seen)

![Users Collection](static/images/users-collection.png)

#### Wireframes

You can find the pdf file to my Wireframes in the wireframe folder of this repository.

---

### Surface Plane

---

I've stated previously that I decided to use Materialize for styling this site along with utilising many of the options it had to
offer. When deciding on Typography I wanted to have a font that could be conceived as 'handwritten', as it is a site for words and
in a dictionary function, I thought a handwritten font would be quite apt. I used google fonts to find a suitable font that followed
the criteria I set out but was also clear to read, I eventually decided on the font [Delius](https://fonts.google.com/specimen/Delius?selection.family=Delius).

I decided on a background that would match the urban feel I was trying to achieve, so I searched for London brick wall backgrounds and
eventually found one I thought was suitable.

I tried to choose a colour scheme that would compliment the background but also so they did not clash, whilst making sure all content was
clear and visible. I ended up using materialize colour of blue-gray darken-1, Gray is neutral and tends to be quite a popular choice in
web design so it fit my criteria. I went with a traditional white font throughout the site apart from where backgrounds are white, I chose
the contrasting blue-gray. I also have multiple flash messages that appear throughout the site, I wanted these to be bold and stand out well,
so I chose the background colour of these to be yellow accent-4 with white font.

The site only has one image which is the background image, apart from that I have also used [font awesome](https://fontawesome.com/) icons
throughout the site as a visual aid for users.

---

## 2. Features

---

### Existing Features

---

#### Home

#### Log In

#### Register

#### Add Slang

#### Profile

---

### Features left to implement

---

---

## 3. Technologies Used

---

---

## 4. Testing

---

---

## 5. Deployment

---

### How to run this project locally

---

## 6. Credits

---

### Content

### Media

### Code

### Acknowledgements


5. I want the dictionary to be easily scaled, so an alphabet of href links that correspond to scrollspy's throughout the page. For example,
clicking on 'A' will take the user to all the slang terms beginning with 'A', and so on. This will help the user as more often than
not, they will be on the site knowing what the slang term it is they are looking for and can jump straight to the letter it begins with.
6. The slang terms will be in alphabetical order as this makes the most sense for a dictionary, and again helps the user locate what they
need. To separate the slang terms alphabetically, there will be a large letter heading at the beginning of each new set of words starting
with the next letter of the alphabet. These letter headers are what are being targeted for the scrollspy links.




Werkzeug Security helpers for user information

https://werkzeug.palletsprojects.com/en/1.0.x/utils/#module-werkzeug.security

Flask cheat sheet and secondary password

https://prettyprinted.com

hashlib 

https://docs.python.org/3/library/hashlib.html

To learn how to sort data alphabetically

https://www.w3schools.com/python/python_mongodb_sort.asp

Cockney rhyming slang

https://happy2movelondon.co.uk/complete-dictionary-of-cockney-rhyming-slang/

For help with jinja templating

https://jinja.palletsprojects.com/en/master/templates/#for

Python datetime stamp

https://www.w3schools.com/python/python_datetime.asp

For converting Object into list

https://www.geeksforgeeks.org/how-to-create-a-list-of-object-in-python-class/

Selecting first letter in database items

https://stackoverflow.com/questions/44974291/ansible-loop-over-range-of-letters-in-template

PEP 8 compliance

https://www.python.org/dev/peps/pep-0008/

Font Awesome Icons

https://fontawesome.com/

Font

https://fonts.google.com/specimen/Delius?selection.family=Delius

IMAGES

Favicons

https://favicon.io/emoji-favicons/input-latin-letters

Brick wall background

https://images.unsplash.com/22/brick-wall.JPG?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb

Yellow wall background

https://unsplash.com/photos/9f3tCfHoGDE

Bug fixes

When user added slang term and definition to the site/database, upon page reloading, the slang term had been created successfully but the definition was showing as 'None'. Upon investigation, there were no errors but there was a mistake in the app.py file under the app.route declaration. Instead of request.form.get("slang_definition) I had written, request.form.get("slang_description"). Was difficult to spot but I discovered it eventually.