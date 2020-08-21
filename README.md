## Flask Deploy
*IDEA:* Canonically good Flask application with the performant and functional base required for scalable production.

N.B. As of the initial version, the docker-compose.yml is set to do a database init.

TODO: Develop a second compose without database init.

## System requirements

Expect 4 cores 2 GB Free RAM

## Get this repo installed

```
git clone https://github.com/dixon1e/flask-deploy-1.git
cd flask-deploy-1
```

## Build and Run
This is a Docker Compose project. The two different steps are to build docker images for the services, and then run.

To prove the build works before runing compose, run this command:

```
docker build -t mytestimage .
```

To run the Docker Compose ensemble, choose an environment and assign it to the environment variable APP_ENV:
```
APP_ENV=Production docker-compose up --build
```

APP_ENV Options:
* Dev
* Test
* Production
