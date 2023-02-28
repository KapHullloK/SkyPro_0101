from flask import jsonify, request, abort
from flask_restx import Namespace, Resource

from dao.model.user import UserSchema
from decorators import admin_required
from implemented import user_service

user_ns = Namespace('users')
auth_ns = Namespace('auth')
user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class User_view(Resource):
    @admin_required
    def get(self):
        all_users = user_service.get_all()
        return users_schema.dump(all_users), 200

    def post(self):
        data = request.json
        user_service.add(data)
        return 'OK', 201


@auth_ns.route('/')
class Auth_view(Resource):
    def post(self):
        data = request.json
        if data is None:
            abort(401)
        tokens = user_service.post_tokens(data)
        return jsonify(tokens)

    def put(self):
        data = request.json
        if data is None:
            abort(401)
        tokens = user_service.put_tokens(data)
        return jsonify(tokens)
