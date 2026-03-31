class TimeMap:

    def __init__(self):
        self.table = defaultdict(list)  #we'll store the keys, values here
        #keys to be [("happy",1)]
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[(key)].append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        value_list = self.table.get(key)
        #at this point we have a list of tuple. timestamp = 11
        #[("happy", 3), ("sad", 10), ("bored", 12), ("okay", 20)]
        if not value_list: return ""
        l, r = 0, len(value_list) - 1
        while l <= r:
            mid = (l+r) // 2
            if value_list[mid][1] == timestamp:
                return value_list[mid][0]
            
            elif value_list[mid][1] > timestamp:
                r = mid - 1

            else:
                l = mid + 1

        return value_list[r][0] if r >= 0 else ""
            
        


