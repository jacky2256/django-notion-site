#  Django Notion Site Project
### 1. Clone the Repository
```shell
git clone https://github.com/jacky2256/django-notion-site.git
cd django-notion-site
```
### 2. Create the .env file
```shell
# Debug mode
DEBUG=True

# Secret Key
SECRET_KEY=django-insecure-c)4oysy=b_4mmgy_(r=ha6#$jw!%1cv^%*=b(af$jl73ns7$5_

# Database
POSTGRES_DB=notion_site_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=1234
DB_HOST=postgres
DB_PORT=5432

# RabbitMQ
RABBITMQ_USER=guest
RABBITMQ_PASS=guest
RABBITMQ_HOST=rabbitmq
RABBITMQ_PORT=5672

# Allowed Hosts
ALLOWED_HOSTS=localhost,0.0.0.0
```
### 3. Start the Docker Containers
```shell
docker compose up -d
```
### 4. Apply Database Migrations
```shell
docker exec -it django_notion_site bash
```
```shell
python manage.py makemigrations
python manage.py migrate
```
### 5. Restart the Django Container
```shell
docker compose restart django_notion_site
```
### 6. Access the Swagger API Documentation
Open your browser and navigate to: http://0.0.0.0:8000/api/swagger/
<br> From there:

1. Locate the POST /example/ endpoint.
2. Send a POST request with the following payload:
```json
{
  "name": "Test Example"
}
```
### 7. Verify the Request Processing
7.1. Check Logs in the Django Container
<br> Enter the django_notion_site container:
```shell
docker logs -f django_notion_site
```
7.2. Check Celery Workers
<br> Repeat the process for celery_service_1 and celery_service_2:
```shell
docker logs -f celery_service_1
docker logs -f celery_service_2
```
### Expected Result
in django_notion_site:
```shell
2024-12-21 10:50:18,427 basehttp.py [213] INFO: "GET /api/swagger/ HTTP/1.1" 200 4640
2024-12-21T10:50:18.509364088Z 2024-12-21 10:50:18,509 basehttp.py [213] INFO: "GET /api/schema/ HTTP/1.1" 200 8543
2024-12-21T10:50:27.801116341Z Pre-save signal received for instance: Test Example
2024-12-21T10:50:27.868899497Z Post-save signal received for instance: Test Example
2024-12-21T10:50:27.873637855Z 2024-12-21 10:50:27,872 basehttp.py [213] INFO: "POST /example/ HTTP/1.1" 201 24
```
in celery_service_1:
```shell
[2024-12-21 10:47:54,572: INFO/MainProcess] worker1@celery_service_1 ready.
2024-12-21T10:50:27.845759656Z 2024-12-21 10:50:27,845 task.py [9] INFO: [Celery Task] Signal: pre_save_multicast, Sender: ExampleModel, Instance ID: None
2024-12-21T10:50:27.875049680Z 2024-12-21 10:50:27,874 task.py [9] INFO: [Celery Task] Signal: post_save_multicast, Sender: ExampleModel, Instance ID: 1
```
in celery_service_2:
```shell
[2024-12-21 10:47:54,561: INFO/MainProcess] worker1@celery_service_2 ready.
2024-12-21T10:50:27.845677681Z 2024-12-21 10:50:27,845 task.py [9] INFO: [Celery Task] Signal: pre_save_multicast, Sender: ExampleModel, Instance ID: None
2024-12-21T10:50:27.876152263Z 2024-12-21 10:50:27,875 task.py [9] INFO: [Celery Task] Signal: post_save_multicast, Sender: ExampleModel, Instance ID: 1
```