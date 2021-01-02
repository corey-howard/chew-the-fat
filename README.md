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

Bug fixes

When user added slang term and definition to the site/database, upon page reloading, the slang term had been created successfully but the definition was showing as 'None'. Upon investigation, there were no errors but there was a mistake in the app.py file under the app.route declaration. Instead of request.form.get("slang_definition) I had written, request.form.get("slang_description"). Was difficult to spot but I discovered it eventually.