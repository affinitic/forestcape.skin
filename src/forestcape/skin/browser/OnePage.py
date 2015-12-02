# -*- coding: UTF-8 -*-

from Products.Five import BrowserView


class OnePageView(BrowserView):

    def getPage(self, pageId):
        page = getattr(self.context, pageId, None)
        if page is None:
            return None
        try:
            translatedObject = page.getTranslation()
        except AttributeError:
            pass
        if translatedObject:
            return translatedObject
        return None

    def getPageText(self, pageId):
        page = self.getPage(pageId)
        if page:
            return page.getText()
