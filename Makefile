deploy:
	gcloud functions deploy create-workout-mongo-python \
		--gen2 --trigger-http --runtime=python310 \
		--region=us-central1 --source=. \
		--entry-point=create_workout --allow-unauthenticated --memory=256MB