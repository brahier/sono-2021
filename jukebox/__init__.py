import requests


class Jukebox:
    def __init__(self) -> None:
        self.url = url = "http://localhost:6680/mopidy/rpc"

    def _send_command(self, method: str, params = []):
        payload = {
            "method": method,
            "params": params,
            "jsonrpc": "2.0",
            "id": 0,
        }
        response = requests.post(self.url, json=payload).json()
        return response

    def setVolume(self, vol: int) -> None:
        self._send_command("core.mixer.set_volume", [vol])

    def stop(self) -> None:
        self._send_command("core.playback.stop")

    def playUri(self, uri: str) -> None:
        self._send_command("core.tracklist.clear")
        res = self._send_command("core.tracklist.add", {"uris": [uri]})
        tlid = res["result"][0]["tlid"]
        self._send_command("core.playback.play", {"tlid": tlid})
