import json
from typing import Optional


class Decoder(json.JSONDecoder):
    __slots__ = ('array_hook',)

    def __init__(self, array_hook: Optional[callable] = None, **kwargs):
        super().__init__(**kwargs)
        self._array_hook = array_hook
        if self._array_hook is not None:
            self.parse_array = self._json_array
            self.scan_once = json.scanner.py_make_scanner(self)

    def _json_array(self, s_and_end, scan_once, **kwargs):
        values, end = json.decoder.JSONArray(s_and_end, scan_once, **kwargs)
        return self._array_hook(values), end
