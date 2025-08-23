class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) > 1:
            if flowerbed[1] == 0 and flowerbed[0] == 0:
                flowerbed[0] = 1
                n -= 1

            if flowerbed[len(flowerbed)-2] == 0 and flowerbed[-1] == 0:
                flowerbed[-1] = 1
                n -= 1
        else:
            if flowerbed[0] == 0 and n > 0:
                flowerbed[0] = 1
                n -= 1
            elif flowerbed[0] == 0 and n == 0:
                return True

        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] == 0 and flowerbed[i+1] != 1 and flowerbed[i-1] != 1:
                flowerbed[i] = 1
                n -= 1

        if n > 0:
            return False
        else:
            return True