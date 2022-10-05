import functions_framework
import pymongo
import datetime


@functions_framework.http
def hello_http(request):
    request_json = request.get_json(silent=True)
    # request_args = request.args
    client = pymongo.MongoClient(
        "mongodb+srv://mongo-user1:IctNC0513@cluster0.t1yi6.mongodb.net/?retryWrites=true&w=majority")
    db = client['workouts']
    work_collection = db['workouts']
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
