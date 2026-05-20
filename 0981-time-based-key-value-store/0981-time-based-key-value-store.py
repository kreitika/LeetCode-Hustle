class TimeMap:

    def __init__(self):
        self.map = {} # key : string , value = list of lists(pairs : value, timestamp)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([value, timestamp])

        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map : return ""
        values = self.map.get(key,[])
        l,r = 0,len(values) - 1
        res = ""
        while l <= r:
            m = (l + r)//2
            if values[m][1] == timestamp:
                res = values[m][0]
                return res
            elif values[m][1] < timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res 


        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)