from flask import Flask,request,jsonify

app= Flask(__name__)



stores=[
    
    {
        
        "name":"MyStore",
        "items":[
            {
                "name":"My Item",
                "price":15.99
            }
        ]
    }
]


@app.get("/stores")
def get_stores():
    return {"stores":stores}


@app.post("/stores")
def create_store():
    data=request.get_json()
    new_store={
        "name":data["name"],
        "items":[]
    }
    stores.append(new_store)
    return jsonify(new_store),201
    
    
@app.post("/stores/<string:name>/item")
def create_item_in_store(name):
    data=request.get_json()
    for store in stores:
        if(store["name"]==name):
            new_item={
                "name":data["name"],
                "price":data["price"]
            }
            store["items"].append(new_item)
            return jsonify(new_item),201
        
    return jsonify({"message":"store not found"}),404

@app.get("/stores/<string:name>")
def get_store(name):
    for store in stores:
        if(store["name"]==name):
            return jsonify(store)
    return jsonify({"message":"store not found"}),404

'''sdsdsdss'''