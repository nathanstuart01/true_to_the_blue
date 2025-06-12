#!/bin/bash

if [ -f .env ]; then
  set -a               
  source .env
  set +a
else
  echo ".env file not found, using default values or exiting..."
  exit 1
fi

if ! command -v docker &> /dev/null
then
    echo "Docker not found. Please install Docker first."
    exit 1
fi

if [ "$(docker ps -a -q -f name=${POSTGRES_CONTAINER_NAME})" ]; then
    echo "Container ${POSTGRES_CONTAINER_NAME} already exists. Starting it..."
    docker start ${POSTGRES_CONTAINER_NAME}
else
    echo "Running new Postgres container..."
    docker run -d \
      --name ${POSTGRES_CONTAINER_NAME} \
      -e POSTGRES_PASSWORD=${POSTGRES_PASSWORD} \
      -e POSTGRES_DB=${POSTGRES_DB} \
      -p ${POSTGRES_PORT}:5432 \
      ${POSTGRES_IMAGE}
fi

echo "Postgres is running on port ${POSTGRES_PORT}"
