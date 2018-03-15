import platform

class Bookmark:
    def __init__(self):
        self.__set_bookmarks_path()
    def __set_bookmarks_path(self):
        system_name = platform.system()
        if system_name == "Linux":
            self.bookmarks_path = "~/.config/google-chrome/Default/Bookmarks"
        elif system_name == "Darwin":
            self.bookmarks_path = '~/Library/Application Support/Google/Chrome/Default/Bookmarks'
        else:
            pass
    def __get_bookmarks(self):
        pass
    
    
            
