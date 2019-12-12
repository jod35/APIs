from flask import Flask,jsonify,request

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
@app.route('/store',methods=['POST'])
def create_store():
    request_data =request.get_json()
    new_store={
        'name':request_data['name'],
        'items':[]
    }
    stores.append(new_store)

    return jsonify({'store':new_store})

#GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    #iterate over stores 
    #if the store name matches, return it
    #if the store doesnot exist,return an error

    for store in stores:
        if store['name']==name:
            return jsonify(store)
    return jsonify({"message":"store not found"})

#GET /store
@app.route('/store')
def get_stores():
    return jsonify({"stores":stores})


#POST /store/<string:name>/item
@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store(name):
    request_data=request.get_json()
    for store in stores:
        if store['name']==name:
            new_item={
                'name':request_data['name'],
                'price':request_data['price']
            }
            store['items'].append(new_item)
            return jsonify({'item':new_item})
    return jsonify({'message':"Store not found"})

#GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] ==name:
            return jsonify({'items':stores['items']})
app.run(port=3000)