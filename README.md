## Running Locally

Make sure you have Python 3.9 [installed locally](https://docs.python-guide.org/starting/installation/).

```sh
$ git clone https://github.com/Brepe/web-wedding-list.git
$ cd web-wedding-list

$ python3 -m venv env
$ pip install -r requirements.txt

$ createdb web-wedding-list

$ python manage.py migrate
$ python manage.py collectstatic


