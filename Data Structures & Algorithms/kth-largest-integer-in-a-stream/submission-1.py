class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)

    def add(self, val: int) -> int:
        if val >= self.max:
            self.nums.append(val)
        elif val <= self.min:
            self.nums.insert(0, val)
        else:
            for i in range(1, self.length):
                if self.nums[i] <= val:
                    continue
                self.nums.insert(i, val)
                break
        return self.nums[-self.k]
    
    @property
    def length(self) -> int:
        return len(self.nums)
    
    @property
    def min(self) -> int:
        if self.length == 0: return 9999
        return min(self.nums)
    
    @property
    def max(self) -> int:
        if self.length == 0: return -9999
        return max(self.nums)
