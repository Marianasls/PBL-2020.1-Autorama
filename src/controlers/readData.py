from flask import Flask
from flask_restplus import Api, Resource 
from src.server.instance import server

app, api = server.app, server.api

from autorama import Autorama

autorama = Autorama()

@api.route('/api')

class readData(Resource):
    def get(self, ):
        return autorama.dados

    def post(self, ):
        response = api.payload
        autorama.dados = append(response)
        return response, 200

autorama.save()