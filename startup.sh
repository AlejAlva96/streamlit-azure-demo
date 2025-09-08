#!/usr/bin/env bash
set -e
PORT=${PORT:-8501}
exec python -m streamlit run app.py --server.address=0.0.0.0 --server.port=$PORT