import webbrowser
import sys
import logging


sys.path.insert(0, "GUI CLI\scripts\beorn_collector.py")
from . import beorn_collector


logging.basicConfig(
    filename="./logs/Zeus.log",
    level=logging.DEBUG,
    format="%(module)s : %(levelname)s:  %(message)s - : %(asctime)s",
)


# def mdso_button(self):
#     webbrowser.open_new(r"https://austx-mdso-vip.chtrse.com/blueplanet-app-bar-ui/")


# def smart_button(self):
#     webbrowser.open_new(r"http://47.43.111.73/")


def beorn_button(self, full_link):
    logging.info(f"Our full link is {full_link}")
    webbrowser.open_new(full_link)


def leftside_beorn_butt(self):
    webbrowser.open_new(r"https://sense.chtrse.com/beorn/v3/topologies?cid=")
def leftside_MDSO_butt(self):
    webbrowser.open_new(r"https://austx-mdso-vip.chtrse.com/blueplanet-app-bar-ui/")


def snippit_button(self):
    webbrowser.open_new(r"http://austx-esp-provisioning.chtrse.com/snippet/")


# def hydra_button(self):
#     webbrowser.open_new(
#         r"https://hydra-vip.chtrse.com/server/app_int/dv_mdso_model_v20220413_1/views/dv_mdso_model_v20220413_1?api_key=yo7BOD04OqhfNesl6Z6PwksUimlvY8DeL7eKr0XQ&cid="
#     )
