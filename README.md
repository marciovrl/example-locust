# example-locust

Simple implementation of non-functional tests with Locust.

For example, let's use a fake API [JSONPlaceholder](https://jsonplaceholder.typicode.com/) to run the tests.

## Preconditions

- python installed

## Clone the project

```
git clone https://github.com/marciovrl/example-locust.git
```

## Available Scripts

In the project directory, you can run:

### `pip install -q -r requirements.txt`

Installs project dependencies. <br>

### `locust -f locustfile.py`

Runs the `locustfile.py` file that contains the Locust scrip. <br>
Open [http://127.0.0.1:8089/](http://127.0.0.1:8089/) in the browser to run the tests in visual mode. <br>

### `locust -f locustfile.py --no-web -c 2 -r 2`

Run the `locustfile.py` which contains the Locust script in non graphical interface mode. <br>

Where the `-c` parameter is the number of concurrent users and `-r` is the number of users that will be added to the test per second. <br>

## Open [Locust documentation](https://locust.io/).
