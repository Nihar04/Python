 # Testing Git folder





# Trying Classes and Objects
class Page:

    def __init__(self,length,type):
        self.length = length
        self.type = type


class Tab(class Page):

    def __init__(self,title, is_current, page, class_page):
        self.title = title
        self.is_current = is_current
        self.page = page
        self.length = class_page.length
        self.type = class_page.type

    def close():
        return "{} is currently {}".format(self.title, self.is_current)

    def reload():
        return "{} is currently reloading".format(self.page)
