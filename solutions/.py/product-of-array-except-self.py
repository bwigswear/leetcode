class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = 0
        for i in nums: 
            if i == 0: 
                zeros += 1
            else:
                product *= i

        products = []
        if zeros == 0:
            for i in nums:
                products.append(product // i)
        elif zeros == 1:
            for i in nums:
                if i == 0:
                    products.append(product)
                else:
                    products.append(0)
        else:
            products = [0] * len(nums)

        return products