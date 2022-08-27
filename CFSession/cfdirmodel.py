import os
DEFAULT = os.path.join(os.getcwd(),".browser")
class cfDirectory:
    """cfDirectory object
    Handles directories where session tokens, headers, and cookie 
    dumps on CFSession.cfcookie.cfCookieHandler
    """
    def __init__(self, path: str = DEFAULT, cache_path: str = DEFAULT) -> None:
        self.path = path
        self.cache = cache_path

    def cookie_path(self, name: str = "sitesession.json") -> str:
        if self.path == DEFAULT:
            path = os.path.join(self.path, name)
        else:
            path = os.path.join(self.path, name)
        return path

    def session_path(self, name: str = "session.json") -> str:
        if self.path == DEFAULT:
            path = os.path.join(self.path, name)
        else:
            path = os.path.join(self.path, name)
        return path
    
    def cache_path(self) -> str:
        if self.cache == DEFAULT:
            path = os.path.join(self.path)
        elif set:
            path = self.cache
        return path
