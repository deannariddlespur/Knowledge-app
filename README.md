# Instructional Assessment
##### Social Login with  Github, Google and Bitbucket

1. Clone the repo.
2. Set up your virtual enviroment using either Virtualenv or Virtual Wrapper.
3. Install requirements:

    ```bash
    $ pip install -r requirements.txt
    ```

4. Run migrations.
5. Load the fixtures in this order will create admin user (username: admin, password: admin):

    ```bash
    $ python manage.py loaddata auth.json
    $ python manage.py loaddata socialaccount.json
    $ python manage.py loaddata instructional_assessment.json
    ```
    - Local database - sqlite3
    - Production database - postgress


6. Run Server

    ```bash
    $ python manage.py runserver
    ```
7. Login as admin http://localhost:8000/admin/
8.   Login with your social account  http://localhost:8000/
9. To create apps for your own project social login:
    * Get Client Id and Client Secret from the following sites.
        * https://bitbucket.org/account/user/YOURUSERNAME/api
        * https://console.developers.google.com/project/YOURPROJECTNAME
        * https://github.com/settings/applications/
    * You must create an account and an application.
    * Change Authorization callback URL.
    * Change SocialNetwork to 'github', 'bitbucket' or 'google'.
    * http://localhost:8000/accounts/SocialNetwork/login/callback/
