# polyknoly 
-Core concept: help citizens make more educated votes
    Using a web application to view a database of potential local government candidates and their approach towards certain issues/questions
    Search via name, precinct, or map?
-Software Stack:
    postgreSQL database, python, and Django web framework (probably some javascript, CSS, HTML later)
-3 step guide to Make Migrations for Models to DB
	1) make changes to models (in models.py)
	2) py manage.py makemigrations <app_name>
	3) py manage.py migrate
-Run local Server(from project directory)
	py manage.py runserver

TODOs:
	-Forms needed to insert/update data
	-organize/sort data relationally
	-query/search options, trending questions, like buttons
	-login/authentication

Current Branch: fbView

09-17-2020
- checking code runs before push to github
- insert date into db not implemented, but code was last tested to make sure:
		-form data is being handed off properly
		-needs to now organize data and save() / push to db
- need to clean pc, so I am backing up all work before "migration"

07-28-2020
- added a candidate entry page
- tested code to insert data/objects into database

07-01-2020
-mostly research as I try to add some depth to this project
-learned that there are alot of elected officials

06-30-2020
-added views to my records application
-added more fields to my tables in db
-
06-23-2020
-had some security issues with old repo, needed to redue project and naming

06-19-2020
-Added some environental variable stuff to project for development and security before I added to git
-familiarization w/ git and django framework

06-12-2020
-started polyknowly app
-created relational database for candidates and questions

