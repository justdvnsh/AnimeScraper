from flask import Flask
from flask_restful import Resource, Api
from flask import request
from webargs.flaskparser import use_args
from webargs import fields
import utils


app = Flask(__name__)
api = Api(app)


def tryout(f):
    def decorator_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            return {"message": "error", "data": None}
    return decorator_function


class Providers(Resource):
    @tryout
    def get(self):
        return {"message": "ok", "data": utils.get_providers()}


class Search(Resource):
    @tryout
    @use_args({'provider': fields.Str(required=True)}, location="query")
    def get(self, args, query):
        search = utils.search_using_provider(query, args['provider'])
        return {'data': search, 'message': 'ok'}


class Episodes(Resource):
    @use_args({"link": fields.Str(required=True), 'provider': fields.Str(required=True)}, location="query")
    @tryout
    def get(self, args):
        episodes = utils.get_episodes_using_provider(
            args['link'], args['provider'])
        return episodes


class Episode(Resource):
    @tryout
    @use_args({"link": fields.Str(required=True), 'parent': fields.Str(required=True), 'provider': fields.Str(required=True)}, location="query")
    def get(self, args):
        return utils.get_episode(args['link'], args['provider'], args['parent'])


api.add_resource(Providers, '/get_providers')
api.add_resource(Search, '/search/<string:query>')
api.add_resource(Episodes, '/load_episodes')
api.add_resource(Episode, '/load_episode')

if __name__ == '__main__':
    app.run(debug=True)
