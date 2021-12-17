#!/usr/bin/env bash

set -ex

api_host="${API_HOST:-localhost}"
api_port="${API_PORT:-4200}"
log_level="${UVICORN_LOG_LEVEL:-warning}"

current_directory=$(pwd)
export PYTHONPATH=${current_directory}/src:${PYTHONPATH}
export PYTHONTRACEMALLOC=128

cmd=$(
    cat <<-EOF
        uvicorn \
            --host "${api_host}" --port ${api_port} \
            --reload --reload-dir=src \
            --log-level ${log_level} \
            --interface asgi3 \
            --http httptools \
            --ws none \
            blackhole.main:app
EOF
)

echo "STARTSERVER Starting uvicorn server @ ${api_host}:${api_port}"
eval $cmd
