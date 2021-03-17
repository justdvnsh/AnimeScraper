from flask import Flask
from flask_restful import Resource, Api
from flask import request
from webargs.flaskparser import use_args
from webargs import fields
import utils


app = Flask(__name__)
api = Api(app)


class Search(Resource):
    def get(self, query):
        search = Twist.search(query)
        return {'data': [utils.SearchResult_to_json(x) for x in search]}


class Episodes(Resource):
    @use_args({"link": fields.Str(required=True), 'provider': fields.Str(required=True)}, location="query")
    def get(self, args):
        episodes = utils.get_episodes_using_provider(args['link'], args['provider'])
        return episodes


class Episode(Resource):
    @use_args({"link": fields.Str(required=True), 'parent': fields.Str(required=True), 'provider': fields.Str(required=True)}, location="query")
    def get(self, args):
        return utils.get_episode(args['link'], args['provider'], args['parent'])


api.add_resource(Search, '/search/<string:query>')
api.add_resource(Episodes, '/load_episodes')
api.add_resource(Episode, '/load_episode')

if __name__ == '__main__':
    app.run(debug=True)
