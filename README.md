# blackhole

A small HTTP server that accepts a request on any endpoint and returns info about that
request.

Supported verbs:

- POST
- PUT
- PATCH
- DELETE
- OPTIONS

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
