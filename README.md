<h1>ShutterShare</h1>
Shutter-Share is a project built for sharing and managing photos through posts while also providing a functionality to compare thr post's images through an intuitive voting method. This README will provide an overview of the project’s structure, its functionality, and how to get started.

<h2>Features</h2>

<b>User Authentication</b> : Secure user registration and login. Registration of user takes multiple details of the user like profile picture, bio, interests, etc.<br><br>
<b>Photo Sharing</b> : Upload and share photos by creating a post:- adding title, description, tags and privacy. Creating a post automatically creates a 'comparing' link which can be used to vote the post's images.<br><br>
<b>Profile Management</b> : Users can manage their profile and photo albums.<br><br>
<b>Search</b> : The website uses a Vector database (pinecone) to store and fetch vector embeddings for posts which is used to get related and recommended posts.<br><br>
<b>Multi-Tasking</b> : Celery and Redis is being used to run the upload post function in the background since it is time consuming, smoothens the flow.<br><br>
<b>Followers</b> : Users can use the following/followers button to follow each other and manage them in followers tab.<br><br>
<b>Notifications</b> : Recent notifications are visible on the home screen on the desktop version which is linked to the target post/user.<br><br>
<b>Responsive UI</b>: Mobile-friendly interface.<br><br>

<h2>Installation</h2>
Clone the repository : git clone https://github.com/Parth2k3/shutter-share.git<br>
Install the required dependencies : pip install -r requirements.txt<br>
Run database migrations : python manage.py migrate<br>
Start the development server : python manage.py runserver<br>
<h2>Structure</h2><br>
user_app/: Contains the core logic for user authentication and profile management.<br>
utils/: Helper functions and utilities used across the project.<br>
static/: Frontend assets such as CSS, JavaScript, and images.<br>
templates/: HTML templates for the web interface.<br>
Procfile: Defines commands for deployment, specifically on Heroku.<br>
railway.json: Deployment configuration for Railway.<br>

<h2>Deployment</h2><br>
To deploy this project, use platforms like Heroku or Railway. Configure the environment variables as required in Procfile or railway.json.<br>
