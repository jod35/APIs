from flask import Flask

app=Flask(__name__)

stores=[
    {
        'name':"My wonderful store",
        'items':[
            {
                "name":"My item",
                 "price":15.77
            }
        ]
    }
]
app.debug=True
app.secret_key='verysecret'


#POST /store :data
@app.route('/store')
def create_store():
    pass

#GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    pass

#GET /store
@app.route('/store')
def get_stores():
    pass


#POST /store/<string:name>/item
@app.route('/store/<string:name>/item')
def create_item_in_store(name):
    pass

#GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    pass 
app.run(port=3000)