import os

import functions_framework
import pymongo
import datetime


@functions_framework.http
def create_workout(request):
    if request.method == "POST":
        request_json = request.get_json(silent=True)
        # request_args = request.args
        client = pymongo.MongoClient(os.getenv("DB_URL"))
        db = client['workouts']
        work_collection = db['workouts']
        if "comments" in request_json \
                and "workout_date" in request_json \
                and "workout_type" in request_json \
                and "creation_date" in request_json:
            workout = {
                "record": datetime.datetime.utcnow().timestamp(),
                "sets": 0,
                "comments": request_json["comments"],
                "workout_date": request_json["workout_date"],
                "workout_type": request_json["workout_type"],
                "creation_date": request_json["creation_date"],
                "day": request_json["day"],
                "week": request_json["week"],
                "user_id": 1,
                "month": request_json["month"]
            }
            id = work_collection.insert_one(workout).inserted_id
            return 'created workout {}!'.format(id)
    return "TEST"
