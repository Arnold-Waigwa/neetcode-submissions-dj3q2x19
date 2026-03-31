class TimeMap:
    # {"Alice": [(sad,1), (happy,2), (thrilled,11), (mellow,22)]}
    #timestamp.get("Alice",4)
    # [(sad,1), (happy,2), (thrilled,11), (mellow,22), (low,30)]
    # l = 0, r = 5
    # 4

    def __init__(self):
        self.storage = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        #check if the key exists
        array = self.storage.get(key)
        if not array: return ""
        l, r = 0, len(array) - 1
        while l <= r:
            mid = (l+r) // 2
            if array[mid][1] == timestamp:
                return array[mid][0]
            elif array[mid][1] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        return array[r][0] if r >= 0 else ""
        
