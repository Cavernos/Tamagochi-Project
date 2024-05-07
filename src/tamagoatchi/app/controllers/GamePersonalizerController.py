from tamagoatchi.app.models import Player
from tamagoatchi.lib.communication import Response, Request, ResponseType
from tamagoatchi.lib.view import View
from tamagoatchi.app.models import tamagotchis


class GamePersonalizerController:
    @staticmethod
    def show_personalization(request: Request) -> Response:
        view = View('personalization', {"player": Player(), "tamagotchis": tamagotchis, "tamagotchi_keys": tamagotchis[0].keys()}, request.json)
        return Response(ResponseType.valid, view)

    @staticmethod
    def new_player(request: Request) -> Response:
        playername = request.json['inputs']['playername']
        player = Player(name=playername)
        view = View('personalization', {'player': player}, request.json)
        return Response(ResponseType.valid, view)
    
    @staticmethod
    def new_tamagotchis(request: Request) -> Response:
        tamagotchis_name = ""
