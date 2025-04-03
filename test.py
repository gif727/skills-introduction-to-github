def main():
    nums = [2, 4, 2, 2, 3, 6, 1]
    print(hares(nums))

def hares(nums):
    hare = nums[0]
    tortoise = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            tortoise = nums[0]
            while True:
                tortoise = nums[tortoise]
                hare = nums[hare]
                if tortoise == hare:
                    return hare

if __name__ == "__main__":
    main()