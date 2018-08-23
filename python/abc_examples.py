"""This module is a simple abstract base class example."""

import abc


class Api(abc.ABC):
    """Api base abstract class"""

    @abc.abstractmethod
    def get_api(self, key: str):
        """Api abstract method get_api"""
        pass

    @property
    @abc.abstractmethod
    def apis(self):
        """Api abstract property apis getter"""
        pass

    @apis.setter
    @abc.abstractmethod
    def apis(self, key: str, value: object):
        """Api abstract property apis setter"""
        pass

    @classmethod
    @abc.abstractmethod
    def is_valid_key(cls, key: str):
        """Api abstract class method is_valid_key"""
        pass

    @staticmethod
    @abc.abstractmethod
    def get_version():
        """Api abstract static method get_version"""
        pass


class AppApi(Api):
    """AppApi is an Api subclass which behaves as an App"""

    def __init__(self, apis: dict):
        # super().__init__(self, apis)
        if not isinstance(apis, dict):
            apis = {}
        self._apis = apis

    @property
    def apis(self):
        return self._apis

    @apis.setter
    def apis(self, apis: dict):
        if not isinstance(apis, dict):
            apis = {}
        self._apis = apis

    def get_api(self, key: str):
        """AppApi method to get an api value from key"""
        if self.is_valid_key(key):
            return self._apis.get(key)
        raise TypeError(f"Expected string type, got {type(key)}")

    def set_api(self, key: str, value: object):
        """AppApi method to set an api key-value pair"""
        if not self.is_valid_key(key):
            raise TypeError(f"Expected string type, got {type(key)}")
        self._apis[key] = value

    @classmethod
    def is_valid_key(cls, key: str):
        if isinstance(key, str):
            return True
        return False

    @staticmethod
    def get_version():
        import time
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
