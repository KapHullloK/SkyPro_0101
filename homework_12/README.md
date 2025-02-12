## Исходный код для проекта урока 12

Склонируйте репозиторий себе, затем выполните задание.


-------- Разница между макс -------
#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

struct seg_tree
{
    int size = 1;
    vector<pair<int, int>> tree;

    void inint(int n)
    {
        while (size < n)
        {
            size *= 2;
        }
        tree.resize(size * 2 - 1);
    }

    void add(int cur, int l, int r, int ind, int x)
    {
        if (r - l == 0)
        {
            tree[cur].first = x;
            tree[cur].second = x;
            return;
        }

        int m = (r + l) / 2;

        if (l <= ind and ind <= m)
        {
            add(cur * 2 + 1, l, m, ind, x);
        }
        else
        {
            add(cur * 2 + 2, m + 1, r, ind, x);
        }

        tree[cur].first = max(tree[cur * 2 + 1].first, tree[cur * 2 + 2].first);
        tree[cur].second = min(tree[cur * 2 + 1].second, tree[cur * 2 + 2].second);
    }

    pair<int, int> get(int cur, int l, int r, int l_f, int r_f)
    {

        if (l_f <= l and r <= r_f)
        {
            return {tree[cur].first, tree[cur].second};
        }

        if (r < l_f or l > r_f)
        {
            return {(int)-1e9 - 7, (int)1e9 + 7};
        }

        int m = (r + l) / 2;
        auto opt1 = get(cur * 2 + 1, l, m, l_f, r_f);
        auto opt2 = get(cur * 2 + 2, m + 1, r, l_f, r_f);

        return {max(opt1.first, opt2.first), min(opt1.second, opt2.second)};
    }
};

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    seg_tree lst;
    lst.inint(n);

    for (int i = 0; i < m; i++)
    {
        int com;
        cin >> com;

        if (com == 1)
        {
            int l, r;
            cin >> l >> r;
            l--;
            r--;

            auto res = lst.get(0, 0, lst.size - 1, l, r);
            cout << res.first - res.second << endl;
        }
        else
        {
            int ind, x;
            cin >> ind >> x;
            ind--;

            lst.add(0, 0, lst.size - 1, ind, x);
        }
    }
}

------- Задача о рюкзаке -------

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

signed main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<vector<int>> dp(n + 1, vector<int>(m + 1, -1));

    dp[0][0] = 0;

    vector<int> lstW(n);
    vector<int> lstC(n);

    for (int i = 0; i < n; i++)
    {
        cin >> lstW[i];
    }

    for (int i = 0; i < n; i++)
    {
        cin >> lstC[i];
    }

    for (int j = 0; j < n; j++)
    {
        for (int i = 0; i <= m; i++)
        {
            if (dp[j][i] != -1 and i + lstW[j] <= m)
            {
                dp[j + 1][i + lstW[j]] = max(dp[j + 1][i + lstW[j]], dp[j][i] + lstC[j]);
            }
            dp[j + 1][i] = max(dp[j + 1][i], dp[j][i]);
        }
    }

    int ans = 0;

    for (int i = 0; i <= m; i++)
    {
        if (dp[n][i] > dp[n][ans])
        {
            ans = i;
        }
    }

    vector<int> res;

    for (int i = n - 1; i >= 0; i--)
    {
        if (ans - lstW[i] >= 0 and dp[i + 1][ans] - lstC[i] == dp[i][ans - lstW[i]])
        {
            res.push_back(i + 1);
            ans -= lstW[i];
        }
    }

    cout << res.size() << endl;

    for (int i = res.size() - 1; i >= 0; i--)
    {
        cout << res[i] << " ";
    }
}

------- Проверка на двудольность ----------

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> used;

void solve(int cur, int prev, int ind, vector<vector<int>> &lst)
{
    if (used[cur])
    {
        return;
    }

    if (cur == prev)
    {
        return;
    }

    used[cur] = ind;

    for (int to : lst[cur])
    {
        if (used[to] == used[cur])
        {
            cout << "No";
            exit(0);
        }
        solve(to, cur, 3 - ind, lst);
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<vector<int>> lst(n);
    used.resize(n);

    for (int i = 0; i < m; i++)
    {
        int a, b;
        cin >> a >> b;
        a--;
        b--;
        lst[a].push_back(b);
        lst[b].push_back(a);
    }

    for (int i = 0; i < n; i++)
    {
        if (!used[i])
        {
            solve(i, -1, 1, lst);
        }
    }

    cout << "Yes";
}

------------- Эйлеров путь -------------
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <iomanip>

using namespace std;

vector<set<int>> lst;
map<pair<int, int>, int> edgs;

void eler_way(int cur)
{
    while (lst[cur].size())
    {
        int to = *lst[cur].begin();
        lst[cur].erase(to);
        lst[to].erase(cur);

        eler_way(to);

        cout << edgs[{cur, to}] << " ";
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    lst.resize(n);

    for (int i = 0; i < m; i++)
    {
        int a, b;
        cin >> a >> b;
        a--;
        b--;

        lst[a].insert(b);
        lst[b].insert(a);
        edgs[{a, b}] = i + 1;
        edgs[{b, a}] = i + 1;
    }

    int start = 0;

    for (int i = 0; i < n; i++)
    {
        if (lst[i].size() % 2)
        {
            start = i;
            break;
        }
    }

    eler_way(start);
}

------------ Алгоритм Дейкстры -------------
#include <iostream>
#include <vector>
#include <set>
#include <iomanip>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, s, f;
    cin >> n >> s >> f;

    int inf = 1e9;

    vector<vector<int>> lst(n, vector<int>(n));
    vector<int> ttl(n, inf);
    vector<int> was(n);

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> lst[i][j];
        }
    }

    ttl[s - 1] = 0;
    set<pair<int, int>> way;
    way.insert({ttl[s - 1], s - 1});

    while (way.size())
    {
        auto cur = *way.begin();
        way.erase(cur);
        was[cur.second] = 1;

        for (int i = 0; i < n; i++)
        {
            if (lst[cur.second][i] != -1 and !was[i])
            {
                ttl[i] = min(ttl[i], cur.first + lst[cur.second][i]);
                way.insert({ttl[i], i});
            }
        }
    }

    if (ttl[f - 1] == inf)
    {
        cout << -1;
    }
    else
    {
        cout << ttl[f - 1];
    }
}

--------- Минимальный каркас ---------

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct el3
{
    int a, b, w;
};

bool cmp(el3 a, el3 b)
{
    return a.w < b.w;
}

vector<int> links;
int root = -1;

int get(int a)
{
    if (links[a] != a)
    {
        links[a] = get(links[a]);
    }
    return links[a];
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    for (int i = 0; i < n; i++)
    {
        links.push_back(i);
    }

    vector<el3> lst;

    for (int i = 0; i < m; i++)
    {
        int a, b, w;
        cin >> a >> b >> w;
        a--;
        b--;

        lst.push_back({a, b, w});
    }

    sort(lst.begin(), lst.end(), cmp);

    int ans = 0;

    for (el3 val : lst)
    {
        if (get(val.a) != get(val.b))
        {
            ans += val.w;

            links[get(val.a)] = get(val.b);
        }
    }

    cout << ans;
}
