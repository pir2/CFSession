from ..CFSession.cfdefaults import cfConstant as cfConstant
from _typeshed import Incomplete
from typing_extensions import Literal, Tuple
import undetected_chromedriver as uc
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

DEFAULT: str
DEFAULT_NAME: Tuple[Literal["Cookie Name"], Literal["User-Agent Name"]]

class cfDirectory:
    cache: str
    cookie_name: str
    agent_name: str
    chromedriver: str
    def __init__(self, cache_path: str = ..., session_name: Tuple[Literal["Cookie Name"], Literal["User-Agent Name"]]=DEFAULT_NAME, chromedriver_path: str = ...) -> None: ...
    def cookie_path(self) -> str: ...
    def session_path(self) -> str: ...
    def cache_path(self) -> str: ...
    def chromedriver_path(self) -> str: ...

class Options:
    proxy: dict
    headless: bool
    ignore_defaults: bool
    chrome_options: uc.ChromeOptions
    desired_capabilities: DesiredCapabilities
    def __init__(self, proxy: list = ..., headless: bool = ..., chrome_options: uc.ChromeOptions = ..., desired_capabilities: DesiredCapabilities = ...) -> None: ...
    def reset_dcp(self, defaults: bool = True) -> None: ...
    def reset_chromeoptions(self, defaults: bool = True) -> None: ...
    def get_default_dcp(self) -> DesiredCapabilities: ...
    def get_default_chromeoptions(self) -> uc.ChromeOptions: ...
