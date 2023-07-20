from dataclasses import dataclass
from typing import IO, Union

from django.core.files.storage import Storage


@dataclass(frozen=True)
class InMemoryFile:
    data: Union[str, bytes]

    def read(self) -> Union[str, bytes]:
        return self.data


class InMemoryStorage(Storage):  # noqa (disable requirement of implementation of all abstract methods)
    def __init__(self, *args, **kwargs) -> None:
        super(InMemoryStorage, self).__init__(*args, **kwargs)
        self._data = {}

    def _save(self, name: str, content: IO) -> str:
        self._data[name] = content.read()
        return name

    def _open(self, name: str, mode='rb') -> InMemoryFile:
        return InMemoryFile(self._data[name])

    def delete(self, name: str):
        if self.exists(name):
            del self._data[name]

    def exists(self, name) -> bool:
        return name in self._data

    def size(self, name: str) -> int:
        return len(self._data[name])

    def url(self, name) -> str:
        # Implementation is required not to raise NotImplementedError
        # Since InMemoryStorage is used for testing purposes, real url is not needed
        return '/fake/url'
