# TNA Interview Coding Challenge: Archive Cache

This repository holds the code for an interview coding challenge for The National Archive: essentially a method for retrieving archive items from an API and storing them in a local cache. Implemented as a django app, the app provide a simple management command, `cacheitem`, to retrieve an item by its `id` and store it locally (this simple version uses the default database provider, `sqlite`, storing the database in the project folder). It then displays a short description of the item, choosing in priority its `title`, `scopeContent.description`, or `citableReference`. If the item exists but none of those fields has content, the message "not sufficient information" is displayed instead. If the `id` provided does not match an item in the API, the message "no record found" is shown.

The records are retrieved from [The National Archive Discovery API](https://www.nationalarchives.gov.uk/help/discovery-for-developers-about-the-application-programming-interface-api/)

## Installation & Build

This repository contains all the file necessary to run a django project that contains the app, and should be installed and built as per a standard django project: first clone this respoitory, then in the root folder create a python virtual envronment, activate it, and install the requirements.  Then change to the `archive` directory that contains the `manage.py` file, and set up migrations.

**[If you require detailed instruction on these steps please read INSTALLATION.md](./INSTALLATION.md).**

## Running the app

The app creates and installs a management command that retrieves an item from the Discovery api, adds it to the database, then uses the view function to retrieve the text description of the item retrieved.

You can use the app from the terminal, ensuring that your working directory is the `archive` directory containing the `manage.py` file. Invoke the `cacheitem` command, passing the ID of the item you want to retrieve. It is good practice to quote the item id, as certain characters will break the argument-parsing process. e.g.:

```
> ./manage.py cacheitem "<item-id-here>"
```

## Running the tests

The app was built with a set of unit and integration tests to confirm that the expected results were emitted from the code. The tests are built on django's default testing framework, and as such they can be run as a suite using the built in `test` management command:

```
> ./manage.py test
```

## Further information

The behaviour of the app when an item that has already been stored is requested was not given in the brief. I have made the assumption that the intention was not to retrieve an item every time it was requested (as this would make storing it locally pointless) so have implemented a local db check as part of the management command: when an item is requested the local db is checked first, and if it exists it is retrieved from there first and the user is shown the message "Item exists locally: using cached version" before the item detail is shown.
