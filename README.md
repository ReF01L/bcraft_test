# BCraft test task
## First start with docker:
 - docker-compose build
 - docker-compose up database -d
 - docker-compose run app alembic upgrade head
 - docker-compose up
## The other times
 - docker-compose up

# Be careful. PSQL stores its state in the parent folder/data