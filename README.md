Werkzeug Security helpers for user information

https://werkzeug.palletsprojects.com/en/1.0.x/utils/#module-werkzeug.security

Flask cheat sheet and secondary password

https://prettyprinted.com

hashlib - 

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

IMAGES

Brick wall background

https://images.unsplash.com/22/brick-wall.JPG?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb

Yellow wall background

https://unsplash.com/photos/9f3tCfHoGDE

Bug fixes

When user added slang term and definition to the site/database, upon page reloading, the slang term had been created successfully but the definition was showing as 'None'. Upon investigation, there were no errors but there was a mistake in the app.py file under the app.route declaration. Instead of request.form.get("slang_definition) I had written, request.form.get("slang_description"). Was difficult to spot but I discovered it eventually.