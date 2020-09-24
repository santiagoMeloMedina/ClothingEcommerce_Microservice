
from configuration.blueprint import app
from flask import jsonify, Blueprint
import constant.connection as CONN

@app.route("/", methods=['GET'])
def root():
    return jsonify({"response": "Welcome from Product!"})


# if __name__ == "__main__":
#     app.run(debug=True, host=CONN.IP, port=int(CONN.PORT))