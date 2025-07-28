class Solution:
    def getAngle(self, s: str) -> float:
        hour, minute = map(int, s.split(":"))
        
        hour %= 12
        
        hour_angle = 30 * hour + 0.5 * minute
        minute_angle = 6 * minute
        
        angle = abs(hour_angle - minute_angle)
        angle = min(angle, 360 - angle)
        
        return f"{angle:.4f}"


s = Solution()
print(s.getAngle("06:00"))
print(s.getAngle("03:15"))
print(s.getAngle("03:32"))