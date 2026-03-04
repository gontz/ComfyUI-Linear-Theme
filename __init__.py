import json
import os
from aiohttp import web
from server import PromptServer

WEB_DIRECTORY = "./js"
NODE_CLASS_MAPPINGS = {}

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")

@PromptServer.instance.routes.get("/linear-theme/config")
async def get_config(request):
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as f:
            return web.json_response(json.load(f))
    return web.json_response({})

@PromptServer.instance.routes.post("/linear-theme/config")
async def save_config(request):
    data = await request.json()
    with open(CONFIG_PATH, "w") as f:
        json.dump(data, f, indent=2)
    return web.json_response({"status": "ok"})
