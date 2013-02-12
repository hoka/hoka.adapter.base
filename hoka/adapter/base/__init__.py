from zope.interface import Interface

class BaseAdapter:

    def __init__(self, context):
        self.context = context