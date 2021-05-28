from os import mkdir
from pathlib import Path 


class Site:
    def __init__(self, **kwargs):
        self._source = Path(kwargs['source'])
        self._dest = Path(kwargs['dest'])

    def create_dir(self, path):
        path = Path(path)
        directory = f"{self._dest}/{path.relative_to(self._source)}"
        Path(directory).mkdir(parents=True, exist_ok=True)

    def build(self):
        Path(self._dest).mkdir(parents=True, exist_ok=True)
        for path in self._source.rglob("*"):
            if(path.is_dir()):
                self.create_dir(path)

    

    
        