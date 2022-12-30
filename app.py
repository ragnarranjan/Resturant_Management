from flask import Flask,request


app = Flask(__name__)

items=[
    {
        "name":"Ashish Ranjan",
        "sal":25
    }
    ,
    {
        "name":"Ranjan",
        "sal":27
    }
]

@app.get('/get-items')   
def get_items():
    return {"items":items}


# @app.get('/get-item/<string:name>')   
# def get_item(name):
#     print(name)
#     for item in items:
#         if name==item['name']:
#             return {"msg":"we got the result"},201
#     return 'hey this doesnt exist',404

@app.get('/get-item')   
def get_item():
    name=request.args.get('name')
    print(name)
    for item in items:
        if name==item['name']:
            return {"msg":"we got the result"},201
    return 'hey this doesnt exist',404

@app.delete('/delete-item')   
def delete_item():
    name=request.args.get('name')
    print(name)
    for item in items:
        if name==item['name']:
            items.remove(item)
            return {"msg":"item removed"},201
    return 'hey this doesnt exist'

@app.put('/update-item')   
def update_item():
    data = request.get_json()
    print(data)
    for item in items:
        if data['name']==item['name']:
            item['sal']=data['sal']
            return {"msg":"update successfully"},200
    return {"msg":"didnt get"}


@app.post("/add-item")
def add_item():
    request_item = request.get_json()
    print(request_item)
    items.append(request_item)
    return {"msg":"item added succesfully"}