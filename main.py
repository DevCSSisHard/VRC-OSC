import spotilib
import pythonosc
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
from pythonosc.udp_client import SimpleUDPClient
from typing import List, Any
import spotimeta

def info(client, server):
    my_list = []
    #Test/Debug stuff
    print(spotilib.song_info())
    print(spotilib.song())
    print(spotilib.artist())
    #Shove every character into a list
    for item in (spotilib.song_info()):
        my_list.append(item)

    #more debugging then sending each character as an address to OSC.
    print(my_list)
    for a in my_list:
        client.send_message("/" + a, 1)



def set_filter(address: str, *args: List[Any]) -> None:
    # We expect two float arguments
    if not len(args) == 2 or type(args[0]) is not float or type(args[1]) is not float:
        return

    # Check that address starts with filter
    if not address[:-1] == "/filter":  # Cut off the last character
        return

    value1 = args[0]
    value2 = args[1]
    filterno = address[-1]
    print(f"Setting filter {filterno} values: {value1}, {value2}")

def main():
    dispatcher = Dispatcher()
    dispatcher.map("/filter*", set_filter)
    server = BlockingOSCUDPServer(("127.0.0.1" , 1337), dispatcher)
    client = SimpleUDPClient("127.0.0.1", 8000)
    #haha funny forever loop for updates. Info doesnt need server but passed it for later work just incase.
    while True:
        info(client, server)


if __name__ == '__main__':
    main()