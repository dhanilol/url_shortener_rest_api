# URL Shortener with Django Rest Framework


```bash
$ git clone https://github.com/dhanilol/url_shortener_rest_api
```

## Installation

After cloning the repository and with Python installed in your local machine. 

Set up the .env file based on the .env.sample file located on the project root folder.
 * Add the Django Secure Key to its attribute: SECRET_KEY
 * Optional: Set the database connection if you're using it (or use the projects default)

Create a Virtual Environment

```bash
$ python -m venv ./venv
```

Activate your virtual environment (MAC e Linux)

```bash
$ source venv/bin/activate
```

In case you are using Windows, use the command:

```bash
venv\Scripts\activate.bat
```

use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
$ pip install -r requirements.txt
```

This project has a default database that was used during development.
If you rather use an external one, connect its credentials on the .env file and run the following commands:

```bash
$ python manage.py makemigrations
```
```bash
$ python manage.py migrate
```


###Start the server

```bash
$ python manage.py runserver
```

## Usage

With the server running you can access [http://127.0.0.1:8000/module_url_shortener/](http://127.0.0.1:8000/module_url_shortener/) to access the Django REST Framework Api Root

If you rather use a service like [Postman](https://www.postman.com/downloads/). You can make your requests with the following:

* **URL**

  <_http://127.0.0.1:8000/module_url_shortener/short_url/_>

* **Method:**
  
  <_The request type_>

  `GET` | `POST`

```python
{
    "original_url": "URL", #required
    "custom_url": "string", #optional
    "expiration": "Date" #optional (default 7 days)
}
```
You should only enter the final piece of your custom URL when sendind with ```"custom_url"``` 
Example:
```python
{
    "original_url":"http://crunchyroll.com/pt-br/attack-on-titan/",
    "custom_url": "tatakae"
}
```

* **Success Response:**
  
  * **Code:** 200 

  * **Content:** 
  ```
  {
    "original_url":"http://crunchyroll.com/pt-br/attack-on-titan/",
    "custom_url": "http://127.0.0.1:8000/u/tatakae",
    "expiration": "2022-01-17 00:16:44"
  }
  ```



## License
[MIT](https://choosealicense.com/licenses/mit/)