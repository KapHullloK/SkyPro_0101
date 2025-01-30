## Исходный код для проекта урока 12

Склонируйте репозиторий себе, затем выполните задание.


------ Мин на отрезке --------

from collections import deque

n, k = map(int, input().split())
lst = list(map(int, input().split()))

l = r = 0

st = deque()

while r < n:
    while r - l < k:
        while st and st[-1][0] >= lst[r]:
            st.pop()
        st.append([lst[r], r])
        r += 1

    print(st[0][0])
    l += 1

    while st and st[0][1] < l:
        st.popleft()

------- треугольники ------

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define int long long

signed main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<int> lst(n);

    for (int i = 0; i < n; i++)
    {
        cin >> lst[i];
    }

    sort(lst.begin(), lst.end());

    int ans = 0;

    for (int i = 0; i < n - 2; i++)
    {
        for (int j = i + 1; j < n - 1; j++)
        {
            int ind = lower_bound(lst.begin(), lst.end(), lst[i] + lst[j]) - lst.begin();
            if (ind == n)
            {
                ind--;
            }

            if (lst[i] + lst[j] <= lst[ind])
            {
                ind--;
            }
            ans += ind - j;
        }
    }

    cout << ans << endl;
}

------ Пчелка ---------

n = int(input())
m = n + (n - 1)

dp = [[0] * m for i in range(n)]

for i in range(n):
    dp[i][0] = 1

for j in range(1, m):
    for i in range(n):
        if i == 0:
            dp[i][j] = dp[i][j - 1] + dp[i + 1][j - 1] * 2
        elif i == n - 1:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        else:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] + dp[i + 1][j - 1]

print(dp[0][m - 1])

--------- Удаление скобок --------

#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

bool check(char a, char b)
{
    map<char, char> alp;
    alp['('] = ')';
    alp['['] = ']';
    alp['{'] = '}';

    return alp[a] == b;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;

    int n = s.size();

    vector<vector<string>> dp(n, vector<string>(n));

    for (int len = 0; len < n; len++)
    {
        for (int r = len; r < n; r++)
        {
            int l = r - len;

            if (len == 0)
            {
                dp[l][r] = "";
            }
            else if (len == 1)
            {
                if (check(s[l], s[r]))
                {
                    string opt = "";
                    opt += s[l];
                    opt += s[r];
                    dp[l][r] = opt;
                }
                else
                {
                    dp[l][r] = "";
                }
            }
            else
            {
                dp[l][r] = dp[l][l] + dp[l + 1][r];

                for (int m = l + 1; m < r; m++)
                {
                    string opt = dp[l][m] + dp[m + 1][r];
                    if (opt.size() > dp[l][r].size())
                    {
                        dp[l][r] = opt;
                    }
                }

                if (check(s[l], s[r]))
                {
                    string opt = "";
                    opt += s[l];
                    opt += dp[l + 1][r - 1];
                    opt += s[r];

                    if (opt.size() > dp[l][r].size())
                    {
                        dp[l][r] = opt;
                    }
                }
                else
                {
                    string opt = dp[l + 1][r - 1];
                    if (opt.size() > dp[l][r].size())
                    {
                        dp[l][r] = opt;
                    }
                }
            }
        }
    }

    cout << dp[0][n - 1];
}

-------- НОВП --------

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

signed main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> lst(n);

    for (int i = 0; i < n; i++)
    {
        cin >> lst[i];
    }

    vector<int> dp(n + 1, 1e7);
    vector<int> road(n + 1, -1);
    vector<int> was(n);

    dp[0] = 0;

    int len = 0;

    for (int i = 0; i < n; i++)
    {
        int ind = lower_bound(dp.begin(), dp.end(), lst[i]) - dp.begin();
        dp[ind] = lst[i];
        road[ind] = i;
        was[i] = road[ind - 1];

        len = max(len, ind);
    }

    cout << len << endl;

    vector<int> ans;

    len = road[len];

    while (len != -1)
    {
        ans.emplace_back(lst[len]);
        len = was[len];
    }

    for (int i = ans.size() - 1; i >= 0; i--)
    {
        cout << ans[i] << " ";
    }
}

---------- Матрица ---------

def bin_pow(x: list, n: int, m: int):
    if n == 0:
        return [[1 if i == j else 0 for j in range(len(x))] for i in range(len(x))]
    if n % 2:
        return mult_mat(x, bin_pow(x, n - 1, m), m)
    else:
        z = bin_pow(x, n // 2, m)
        return mult_mat(z, z, m)


def mult_mat(lst1: list, lst2: list, m: int):
    new_lst = [[0] * len(lst1) for _ in range(len(lst1))]

    for i in range(len(lst1)):
        for j in range(len(lst2)):
            tmp = 0
            for k in range(len(lst1)):
                tmp += (lst1[i][k] * lst2[k][j]) % m

            new_lst[i][j] = tmp % m

    return new_lst


n, s, m = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(n)]

res = bin_pow(lst, s, m)

for i in res:
    print(*i)

