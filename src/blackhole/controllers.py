import json
from datetime import datetime
from json import JSONDecodeError
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse

router = APIRouter()


def _parse_query(request: Request) -> Dict[str, List[str]]:
    """JSONify Request query parameters."""
    query = {}
    for k, v in sorted(request.query_params.multi_items()):
        query.setdefault(k, []).append(v)

    return query


def _parse_headers(request: Request) -> Dict[str, str]:
    """JSONify Request headers."""
    return {k: str(request.headers[k]) for k in sorted(request.headers)}


async def _parse_data(request: Request) -> Optional[Dict[str, Any]]:
    """Helper for attempting to parse the request body as JSON."""
    try:
        return await request.json()
    except JSONDecodeError:
        return None


async def _response(path: str, request: Request) -> JSONResponse:
    """A helper for returning particulars in a response."""
    data = {
        "method": request.method,
        "headers": _parse_headers(request),
        "query": _parse_query(request),
        "path": path,
    }

    # Only show this field with "write HTTP methods".
    if request.method in ("POST", "PUT", "PATCH"):
        data["data"] = await _parse_data(request)

    # Print output.
    print(f"/ --- {datetime.now().isoformat()} " + "-" * 40)
    print(json.dumps(data, indent=2))
    print("\\ " + "-" * 70)

    # Also return output to HTTP client.
    return JSONResponse(data)


@router.get("{path:path}", status_code=status.HTTP_200_OK)
async def http_get(path: str, request: Request) -> JSONResponse:
    return await _response(path, request)


@router.post("{path:path}", status_code=status.HTTP_201_CREATED)
async def http_post(path: str, request: Request) -> JSONResponse:
    return await _response(path, request)


@router.put("{path:path}", status_code=status.HTTP_200_OK)
async def http_put(path: str, request: Request) -> JSONResponse:
    return await _response(path, request)


@router.patch("{path:path}", status_code=status.HTTP_200_OK)
async def http_patch(path: str, request: Request) -> JSONResponse:
    return await _response(path, request)


@router.delete("{path:path}", status_code=status.HTTP_200_OK)
async def http_delete(path: str, request: Request) -> JSONResponse:
    return await _response(path, request)


@router.options("{path:path}", status_code=status.HTTP_200_OK)
async def http_options(path: str, request: Request) -> JSONResponse:
    return await _response(path, request)
