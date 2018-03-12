import platform

class Bookmark:
    def __init__(self):
        pass
    
    def __get_bookmark_path(self):
        system_name = platform.system()
        print (system_name)
        if system_name == "Linux":
            self.bookmark_path = '~/.config/google-chrome/Default/Bookmarks'
        elif system_name == "Darwin":
            self.bookmark_path = '~/Library/Application Support/Google/Chrome/Default/Bookmarks'
        else:
            pass
        
    
    
            
