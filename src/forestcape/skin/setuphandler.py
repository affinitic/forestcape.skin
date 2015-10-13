# -*- coding: utf-8 -*-


def setupSite(context):
    if context.readDataFile('forestcape.skin_various.txt') is None:
        return
