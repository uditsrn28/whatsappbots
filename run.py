__author__ = 'udit'

from yowsup.stacks import  YowStackBuilder
from layer import EchoLayer
from yowsup.layers.auth import AuthError
from yowsup.layers import YowLayerEvent
from yowsup.layers.network import YowNetworkLayer
from yowsup.env import YowsupEnv
from config import Config

credentials = (Config.CONFIG_PHONE, Config.CONFIG_PASSWORD) # replace with your phone and password
print credentials
if __name__==  "__main__":
    stackBuilder = YowStackBuilder()

    stack = stackBuilder \
        .pushDefaultLayers(True) \
        .push(EchoLayer) \
        .build()

    stack.setCredentials(credentials)
    stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))   #sending the connect signal
    stack.loop() #this is the program mainloop