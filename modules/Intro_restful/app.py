"""
Initial test of a RESTful API
Dipankar Nath
"""
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []


class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {"Item": None}, 404

    def post(self, name):
        data = request.get_json()
        price = data['price']
        item = {'name': name, 'price': price}
        items.append(item)
        return item, 201

    # def put(self, name):
    #     raw_data = request.json()
    #     price = raw_data['price']
    #     for item in items:
    #         if item['name'] == name:
    #             item['price'] = price
    #         else:
    #             items.append


class Itemlist(Resource):
    def get(self):
        return {'items': items}, 201


api.add_resource(Itemlist, '/items')
api.add_resource(Item, '/item/<string:name>')

if __name__ == "__main__":
    app.run(port=5000, debug=True)
