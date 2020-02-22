from sys import stdin

def get_result(data):
  N = data[0]
  # n円の場合、n+1円の場合
  dp = 0, 1
  for n in N:
      n = int(n)
      # N=123の1を考える
      # 100円を払うケース (1枚)
      # or 1000円払っていて + お釣り分の900円を払うケース (9枚)
      a = min(dp[0] + n, dp[1] + 10 - n)
      # 200円を払うケース (2枚) 
      # or 1000円払っていて + お釣り分の800円を払うケース (8枚, 下の桁によって減るケース)
      b = min(dp[0] + n + 1, dp[1] + 10 - (n + 1))
      dp = a, b
  return dp[0]

if __name__ == '__main__':
    data = list(map(str, stdin.readline().rstrip('\n').split(' ')))
    result = get_result(data)
    print(result)
