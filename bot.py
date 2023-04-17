#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import nonebot
import sys
import json
import os
from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11Adapter
try:
    os.mkdir("./src/data")
except FileExistsError:
    print("检测到`data`文件夹已创建。")

try:
    os.mkdir("./src/cache")
except FileExistsError:
    print("检测到`cache`文件夹已创建。")

try:
    os.mkdir("./src/sign")

except FileExistsError:
    print("检测到`sign`文件夹已创建。")

try:
    os.mkdir("./src/assets")
    os.mkdir("./src/assets/arcaea")
    os.mkdir("./src/assets/arcaea/char")
    os.mkdir("./src/assets/arcaea/icon")
    os.mkdir("./src/assets/arcaea/song")
    os.mkdir("./src/assets/jx3")
    os.mkdir("./src/assets/jx3/skills")
    os.mkdir("./src/assets/jx3/icons")
    os.mkdir("./src/assets/jx3/achievement")
    os.mkdir("./src/assets/jx3/talents")
    os.mkdir("./src/assets/jx3/adventure")
except FileExistsError:
    print("检测到`assets`文件夹已创建，已自动补全所有需要的文件夹。")
plugins = os.listdir("./src/plugins")
for i in plugins:
    if not os.path.exists("./src/plugins/" + i + "/info.json"):
        raise FileNotFoundError(
            f"Plugin `{i}` required a `info.json` but not found. Please check and try again.")
        sys.exit(1)

tools_path = os.path.dirname(__file__)
nonebot.init(tools_path=os.path.join(tools_path, 'src\\tools'))
app = nonebot.get_asgi()
driver = nonebot.get_driver()
driver.register_adapter(ONEBOT_V11Adapter)
nonebot.load_from_toml("pyproject.toml")
if __name__ == "__main__":
    nonebot.logger.warning(
        "Always use `nb run` to start the bot instead of manually running!")
    nonebot.run(app="__mp_main__:app")
