# hackathon_API
This project is a Django REST Framework project that allows users to create and register for hackathons. Only admins can create a hackathon, and all users can register and create submissions for hackathons they've registered for.

Installation and Setup
#Clone the repository.
#Create a virtual environment for the project and activate it.
#Install the requirements by running pip install -r requirements.txt.
#Create a superuser by running python manage.py createsuperuser and following the prompts. You will use this user to login as an admin.
#Run the migrations by running python manage.py migrate.
#Start the development server by running python manage.py runserver.
  API Endpoints
->POST /hackathon/: Creates a new hackathon. Only admins can perform this action.
->GET /hackathon/list/: Retrieves a list of all the hackathons.
->GET /registration/all/: Retrieves a list of all the registrations.
->POST /register/: Registers a user for a hackathon.
->GET /user/hackathon/<str:username>/: Retrieves a list of hackathons registered by a user.
->POST /user/createsubmission/<str:username>/<str:hackathon>/: Creates a submission for a user and a hackathon.
->GET /user/submission/<str:username>/: Retrieves a list of submissions made by a user.

