# Twistlock testing assignment

The general testing strategy was to divide the tests according to their types: authentication, data validation, parameter validation, etc. 

I've also added some minimal CRUD tests and performance tests since I wan't sure if I was asked to include them.

I've found several bugs:

1. You can login with only 'admin' as username no matter which password you type (prio: high)
2. You can login with only 'admin' as password no matter which username you type (prio: high)
3. Many requests return 418 (since I guess they're not implemented for this simple API)
4. Some players are missing names (prio: medium-high???)
5. There are missing IDs between pages. In each page there are 49 players but there is a gap between pages. For example, the last player on the first page has an id of 48 and the first player on the second page has an id of 50. This indicates a loss of data (prio: high)
6. This API doesn't support a lot of concurrency requests. In the test I've put the value of 3 to the concurrent requests variable, but if I change to, let's say, 10, then the web server crashes and I need to restart it. I think it's an important high priority bug...

## How to run tests

Make sure you have docker installed.
Then, pull the project, navigate to its root folder and build docker image like so:

```
docker build -t twistlock .
```

The python to run the server and the tests is already configured (main.py) in dockerfile so simple run:

```
docker run twistlock
```
