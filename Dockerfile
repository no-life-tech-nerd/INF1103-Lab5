FROM docker.io/library/python:3.14-slim

WORKDIR /app

COPY inventory_manager.py .

ENV DATA_PATH=/data
VOLUME ["/data"]
CMD ["python", "inventory_manager.py"]
