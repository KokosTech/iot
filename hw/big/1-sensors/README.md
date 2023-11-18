# Homework 1

## How to run

```bash
docker build -t iot-sensors-client-01 client
docker build -t iot-sensors-server-01 server/src
docker compose up # docker compose up -d if you want to run in background
```

*Btw we don't use the built-in build option in docker compose because we believe that you could just download the image from dockerhub*

## Optional

If you want to run the client with different number of sensors (threads), you can add a `.env` file:

```bash
mkdir .env
echo "THERM_NUM=<NUM>" > .env
```
