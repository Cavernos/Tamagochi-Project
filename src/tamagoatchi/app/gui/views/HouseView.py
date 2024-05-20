import pygame
import pyscroll
from pygame import Surface, SurfaceType
import pytmx

from tamagoatchi.app.definitions import MAP_SIZE
from tamagoatchi.lib.event import EventManager
from tamagoatchi.lib.handlers import ResourceHandler
from tamagoatchi.lib.view import GUIView
from tamagoatchi.lib.widgets import Button


class HouseView(GUIView):
    def __init__(self, screen: Surface | SurfaceType, ext_dict: dict):
        super().__init__(screen, ext_dict)
        map = pytmx.util_pygame.load_pygame(self.view_location)
        zoom = screen.get_size()[0] / MAP_SIZE[0]
        map_data = pyscroll.TiledMapData(map)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(map_data, pygame.display.get_window_size())
        self.map_layer.zoom = zoom
        self.buttons.append(Button(self, self.view_tamagotchi_red, zoom*48, zoom*48, zoom*16, zoom*16))
        self.event_managers["Key Manager"] = EventManager.from_id("Key Manager")
        self.event_managers["Key Manager"].register(pygame.KEYDOWN, self.on_key_pressed)

    def on_key_pressed(self, event):
        if event.key == pygame.K_ESCAPE:
            self.redirect('')
        return

    def view_tamagotchi_red(self, event):
        self.redirect('game.red_tamagotchi')
        return

    def deregister_events(self):
        super().deregister_events()
        for key, value in self.event_managers.items():
            if key == "Key Manager":
                value.deregister(pygame.KEYDOWN, self.on_key_pressed)
