Deploy

```
~/google-cloud-sdk/bin/gcloud functions deploy go_gcp_cfunc_mongo_workouts --trigger-http --runtime=go116 --entry-point=GetWorkouts --allow-unauthenticated --memory=256MB
```
```
# example
gcloud functions deploy python-http-function \
--gen2 \
--runtime=python310 \
--region=REGION \
--source=. \
--entry-point=hello_get \
--trigger-http \
--allow-unauthenticated
```
LOGS

```
gcloud functions logs read
gcloud functions logs read FUNCTION_NAME --execution-id EXECUTION_ID
```
Mongo Install Mongo Tools

mongodb+srv://<credentials>@cluster0.t1yi6.mongodb.net/myFirstDatabase?appName=mongosh+1.6.0
## import
```
mongoimport --db=workouts --collection=workouts --type=csv --headerline --file=/home/malandr/Downloads/'workouts-Grid view.csv'
mongosh "mongodb+srv://cluster0.t1yi6.mongodb.net/myFirstDatabase" --apiVersion 1 --username <usern
```