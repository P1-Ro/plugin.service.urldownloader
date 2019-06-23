#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs
import os
import re
import sys

import requests
import xbmcaddon
import xbmcgui


def vtt_to_srt(content):
    content = re.sub(r'([\d]+)\.([\d]+)', r'\1,\2', content)
    content = re.sub(r'WEBVTT(\n|\r)*', '', content)
    content = re.sub(r'^\d+\n', '', content)
    content = re.sub(r'\n\d+\n', '\n', content)

    return content


def download_url(url):
    addon = xbmcaddon.Addon()
    folder = addon.getSetting("subsFolder")

    if len(str(folder)) == 0:
        title = addon.getAddonInfo('name')
        xbmcgui.Dialog().ok(title, "Please set folder for subtitles in addon settings")
        return

    filename = url.split("/")[-1].split("?")[0]
    path = os.path.join(folder, filename)

    r = requests.get(url)
    content = r.content.decode("utf-8")

    if ".vtt" in filename:
        path = path.replace(".vtt", ".srt")
        content = vtt_to_srt(content)

    with codecs.open(path, "w", "utf-8-sig") as f:
        f.write(content)


if len(sys.argv) == 2:
    url = str(sys.argv[1]).split("=")[1]
    download_url(url)
