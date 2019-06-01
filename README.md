DataScience Stack
=================

This can be deployed using docker stack and the python Flask will launch on port 5010 by default while Jupyter Notebook will be accessible on port 5011. Adminer will connect to PostgreSQL as specified in a docker-compose.yml.

## Folder structure:

* docker-compose.yml - Docker compose file to build the stack
* app-code - python code directory
* db-pgsql - persistence database data
* db-archive - databases export and import sql scripts & db dumps
* jupyter-notebook-conf - a password protected jupyter authentication and authorization file (comment out if preference is on jupyter access token)

## Deployment Steps:

* Fetch Code : `git clone git@github.com:ds-group-kawhi/datascience-stack.git`
* To lint Docker Compose file : `docker-compose config` or `docker-compose -f docker-compose config`
* To launch a local development : `docker-compose --compatibility up -d` (depends on if image is pulled or built)
* To launch a local development using Docker Swarm : `cd datascience-stack && sudo docker stack deploy -c docker-compose.yml kawhi`
* *NOTE:* Make sure all the folder requirements have been met before launching DataScience Stack

## References: 
- [DockerHub](https://hub.docker.com)
- [Jupyter Docker Stack](https://jupyter-docker-stacks.readthedocs.io/en/latest/)
