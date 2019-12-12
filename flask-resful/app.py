from flask import Flask
from flask_restful import Api ,Resource

app=Flask(__name__)
api=Api(app)

items=[]

class Item(Resource):
    def get(self,name):
        for item in items:
            if item['name'] == name:
                return item

    def post(self,name):
        item={'name':name,'price':12.00}
        items.append(items)
        return item

api.add_resource(Item,'/item/<string:name>')

app.run(debug=True)