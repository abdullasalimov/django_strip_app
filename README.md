# Django-Stripe Payment APP

## Build and run the container

1. Install Docker

2. Download this repository
    ```
    git clone https://github.com/abdullasalimov/django_stripe_app.git
    ```
3. Go to directory
    ```
    cd django_stripe_app
    ```

4. Create a .env file at the same level as this README, containing the following. This will be used by Docker.
    ```
    # Environment settings for local development.

    STRIPE_PUBLIC_KEY=pk_test_........... #Input your stripe public key
    STRIPE_SECRET_KEY=sk_test_........... #Input your stripe secret key
    DOMAIN=http://localhost:8000
    ```

5. On the command line, within this directory, do this to build the image and start the container:

        docker build --tag django-stripe-app .

6. If that's successful you can then start it up. This will start up the database and web server, and display the Django runserver logs:

        docker run --publish 8000:8000 django-stripe-app

7. Open http://localhost:8000 in your browser.

8. To create admin use below command:

        docker exec -it container_id python manage.py createsuperuser

## App is live on Heroku server

1. To test app go below site:

        https://django-stripe-app.herokuapp.com/

2. To go to admin panel:

        https://django-stripe-app.herokuapp.com/admin/

        login:admin
        password:123

3. Test stripe api with below card numbers:

        Success: 4242 4242 4242 4242
        Authentication: 4000 0000 0000 3220
        Decline: 4000 0000 0000 0002
