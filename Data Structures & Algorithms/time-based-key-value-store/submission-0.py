from sortedcontainers import SortedDict
class TimeMap:

    def __init__(self):
       self.maps=defaultdict(SortedDict) 

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.maps[key][timestamp]=value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.maps:
            return ""
        timestamps=self.maps[key]
        idx=timestamps.bisect_right(timestamp)-1
        if idx>=0:
            closest=timestamps.iloc[idx]
            return timestamps[closest]
        return ""