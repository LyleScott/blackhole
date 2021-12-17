from json import JSONDecodeError
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse


router = APIRouter()


def _parse_query(request: Request) -> Dict[str, List[str]]:
    query = {}
    for k, v in sorted(request.query_params.multi_items()):
        query.setdefault(k, []).append(v)

    return query


def _parse_headers(request: Request) -> Dict[str, str]:
    return {k: str(request.headers[k]) for k in sorted(request.headers)}


async def _parse_data(request: Request) -> Optional[Dict[str, Any]]:
    try:
        return await request.json()
    except JSONDecodeError:
        return None


async def _response(path: str, request: Request) -> JSONResponse:
    return JSONResponse({
        "path": path,
        "query": _parse_query(request),
        "headers": _parse_headers(request),
        "data": await _parse_data(request),
    })


@router.get("/{path:path}", status_code=status.HTTP_200_OK)
async def index(path: str, request: Request) -> JSONResponse:
    return await _response(path, request)


@router.post("/{path:path}", status_code=status.HTTP_201_CREATED)
async def index(path: str, request: Request) -> JSONResponse:
    return await _response(path, request)


@router.put("/{path:path}", status_code=status.HTTP_200_OK)
async def index(path: str, request: Request) -> JSONResponse:
    return await _response(path, request)


@router.patch("/{path:path}", status_code=status.HTTP_200_OK)
async def index(path: str, request: Request) -> JSONResponse:
    return await _response(path, request)


@router.options("/{path:path}", status_code=status.HTTP_200_OK)
async def index(path: str, request: Request) -> JSONResponse:
    return await _response(path, request)
