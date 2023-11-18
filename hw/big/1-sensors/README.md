# Homework 1

## How to run

```bash
docker build -t iot-sensors-client-01 client
docker build -t iot-sensors-server-01 server/src
docker compose up
```

*Btw we don't use the built-in build option in docker compose because we believe that you could just download the image from dockerhub*
