#!/usr/bin/python
# -*- coding: utf-8 -*-
import xbmc, xbmcgui, xbmcaddon
import os
import time
import downloader


def download_url(url):
    dp = xbmcgui.DialogProgress()
    dp.create("URL Downloader", "Downloading", "", "Please Wait")
    dp.update(0, "Downloading ", "", "Please Wait")
    folder = xbmcaddon.Addon('plugin.video.urldownloader').getSetting("subsFolder")
    filename = url.split("/")[-1].split("?")[0]

    path = os.path.join(folder, filename)
    downloader.download(url, path, dp)


defaulturl = "http://google.com"
download_url(defaulturl)
