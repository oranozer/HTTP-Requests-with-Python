# HTTP-Requests-with-Python

a simple HTTP client using Python and talk with
the provided server written with Flask. The server runs a simple D’Hondt-style election
simulator with region and seat information for an example-country election. It has 3 APIs,
one for adding/deleting parties another for adding/deleting regions for the election, and
third one for running the D’Hondt simulation with party votes provided by the client.

To use the provided server, you need to install Flask, which is a Python library that handles
HTTP requests. 

## After extracting the given server code, head into the folder and run:

```bash
flask --app election init-db
```
## Starting the server

```bash
flask --app election run
```


