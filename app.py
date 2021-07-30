from flask import Flask, Response, request, json, render_template
import pymongo

app = Flask(__name__)

# establishing webhook_db connection to create a new db
try:
    mongo = pymongo.MongoClient(
        host="localhost",
        port=27017,
        serverSelectionTimeoutMS=1000
    )
    db = mongo.webhook_db
    mongo.server_info()
except:
    print("ERROR -Cannot connect to db")


# home page
@app.route('/')
def index():
    return "HELLO"


# webhook page
@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        if request.headers['Content-Type'] == 'application/json':
            wh_table = request.get_json()
            dbResponse = db.wh_table.insert_one(wh_table)

            return Response(
                response=json.dumps({
                    "message": "data successfully added to the collection",
                    "id": f"{dbResponse.inserted_id}"
                }),
                status=200,
                mimetype="application/json"
            )
    except Exception as ex:
        return Response(
            response=json.dumps({
                "message": "some error occured",
                "error": f"{ex}"
            }),
            status=500,
            mimetype="application/json"
        )


# reads the data from the DB and showing the whole data on "data_display.html"
@app.route('/read', methods=['GET'])
def message():
    try:
        data = list(db.wh_table.find())
        for user in data:
            user["_id"] = str(user["_id"])
        return render_template("data_display.html", data=data)
    except Exception as ex:
        return Response(
            response=json.dumps({
                "message": "cannot read users",
                "error": f"{ex}"
            }),
            status=500,
            mimetype="application/json"
        )


if __name__ == "__main__":
    app.run(port=5000, debug=True)
