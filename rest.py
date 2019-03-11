from flask import Flask, request, send_file
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


@app.route('/')
def indexPage():
	return None

#handle site.com/<id>
class ToDoSimple(Resource):
	def get(self, todo_id):
		return 'hello'

	def post(self, todo_id):
		data = request.get_json()
		return data['val']

#handle site.com/image/id
class ImageHandler(Resource):
	def get(self, imageId):
		return send_file("images/img.jpg", mimetype='image/gif')

api.add_resource(ToDoSimple, '/<todo_id>')
api.add_resource(ImageHandler, '/image/<imageId>')

if __name__ == '__main__':
	app.run(debug=True)