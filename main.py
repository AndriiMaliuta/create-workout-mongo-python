import os

import functions_framework
import pymongo
import datetime


@functions_framework.http
def create_workout(request):
    if request.method == "POST":
        request_json = request.get_json(silent=True)
        if request_json:
            print(request_json)
        # request_args = request.args
        client = pymongo.MongoClient(os.getenv("DB_URL"))
        db = client['workouts']
        work_collection = db['workouts']
        today = datetime.datetime.now()
        if request_json:
            workout = {
                "record": round(datetime.datetime.now().timestamp()),
                "sets": request_json["sets"],
                "comments": request_json["comments"],
                "workout_date": request_json["workout_date"],
                "workout_type": request_json["workout_type"],
                "creation_date": today,
                "day": today.strftime("%A"),
                "week": week_number_of_month(today),
                "user_id": request_json["user_id"],
                "month": today.strftime("%B")
            }
            id = work_collection.insert_one(workout).inserted_id
            return 'created workout {}!'.format(id)
    return "TEST"


def week_number_of_month(date_value):
    return (date_value.isocalendar()[1] - date_value.replace(day=1).isocalendar()[1] + 1)
