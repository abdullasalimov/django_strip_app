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
4. Go to https://stripe.com/ and register to get stripe keys.

5. Create a .env file at the same level as this README, and input stripe keys. This will be used by Docker.
    
    ```
    STRIPE_PUBLIC_KEY=pk_test_...........
    STRIPE_SECRET_KEY=sk_test_...........
    ```

6. On the command line, within this directory, do this to build the image and start the container:

        docker build --tag django-stripe-app .

7. If that's successful you can then start it up. This will start up the database and web server, and display the Django runserver logs:

        docker run --publish 8000:8000 django-stripe-app

8. Open http://localhost:8000/item/ in your browser.

9. To create admin use below command:

        docker exec -it container_id python manage.py createsuperuser

## App is live on Heroku server

1. To test app go below site:

    https://django-stripe-app.herokuapp.com/item/

2. To go to admin panel:

    https://django-stripe-app.herokuapp.com/admin/

        login:admin
        password:123

