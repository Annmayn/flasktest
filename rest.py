from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


@app.route('/')
def indexPage():
	return "Front Page"

class ToDoSimple(Resource):
	def get(self, todo_id):
		return 'hello'

	def put(self, todo_id):
		pass

api.add_resource(ToDoSimple, '/<todo_id>')

if __name__ == '__main__':
	app.run(debug=True)