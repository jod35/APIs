from flask import Flask
from flask_restful import Api ,Resource

app=Flask(__name__)
api=Api(app)

class Sister(Resource):
    def get(self,name,age):
        return {"name":name,"age":age}


api.add_resource(Sister,'/sister/<string:name>/<int:age>')

app.run(debug=True)