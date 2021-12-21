# blackhole

A small HTTP server that accepts a request on any endpoint and returns info about that
request.

Supported verbs:

- POST
- PUT
- PATCH
- DELETE
- OPTIONS
- ... easy to add more!

## Usage

You can make life easy with Docker or bootstrap your own virtual environment using
`requirements.txt`.

A webserver is started that you can use the supported HTTP verbs against. Details of
the request are printed to stdout.

### Docker

This will listen for HTTP requests to http://localhost:4200

```shell
docker-compose up --build
```

### Python Virtualenv

You can use whatever virtual environment manager you want instead of the stdlib one.

```shell
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
./start_server.sh
```

## Examples

### GET

```shell
curl -X GET http://localhost:4200/foo/bar\?foo\=bar\&foo\=baz\&der\=p
```

```json
{
  "path": "foo/bar",
  "query": {
    "der": [
      "p"
    ],
    "foo": [
      "bar",
      "baz"
    ]
  },
  "headers": {
    "accept": "*/*",
    "host": "localhost:4200",
    "user-agent": "curl/7.64.1"
  },
  "data": null
}
```

## POST

```shell
curl -X POST http://localhost:4200/user/accout -d '{"username": "foobar", "org": "beez_neez"}'
```

```json
{
  "path": "user/account",
  "query": {},
  "headers": {
    "accept": "*/*",
    "content-length": "42",
    "content-type": "application/x-www-form-urlencoded",
    "host": "localhost:4200",
    "user-agent": "curl/7.64.1"
  },
  "data": {
    "username": "foobar",
    "org": "beez_neez"
  }
}
```
