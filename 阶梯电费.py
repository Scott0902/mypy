class Solution:
    def __init__(self) -> None:
        pass
    
    def solution(self, amount):
        result = None
        if amount<0 or amount>10000:
            print('Input error.')
            return result
        elif amount<=150:
            result=amount*0.4463
        elif amount>150 and amount<=400:
            result=150*0.4463+(amount-150)*0.4663
        elif amount>400:
            result=150*0.4463+250*0.4663+(amount-150-250)*0.5663
        result=float(f'{result:.1f}')
        return result

if __name__ == "__main__":

    print('月用电量在150千瓦时及以下部分按每千瓦时0.4463元执行，\n'\
          '月用电量在151~400千瓦时的部分按每千瓦时0.4663元执行，\n'\
          '月用电量在401千瓦时及以上部分按每千瓦时0.5663元执行。\n'\
          '\n请输入一个用电量整数，计算结果将保留一位小数。')
    amount = int(float(input().strip()))
    
    s = Solution()
    result = s.solution(amount)

    print(result)
