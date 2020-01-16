"""
Initial test of a RESTful API
Dipankar Nath
"""
from flask import Flask
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
        item = {'name': name, 'price': 12.00}
        items.append(item)
        return item, 201


class Itemlist(Resourse):
    def get(self):
        return {'items': items}


api.add_resource(Itemlist, '/items')
api.add_resource(Item, '/item/<string:name>')

if __name__ == "__main__":
    app.run(port=5000, debug=True)
