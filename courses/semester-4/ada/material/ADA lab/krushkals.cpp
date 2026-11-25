#include <iostream>
#include <limits.h> // For INT_MAX

using namespace std;

int main()
{
  int parent[10], mincost = 0, cost[10][10];
  int n;

  cout << "Enter the no. of vertices:\n";
  cin >> n;

  cout << "Enter the graph data:\n";
  for (int i = 1; i <= n; i++)
  {
    for (int j = 1; j <= n; j++)
    {
      cin >> cost[i][j];
      if (cost[i][j] == 0)
        cost[i][j] = INT_MAX; // Using INT_MAX to represent infinity
    }
  }

  for (int i = 0; i < 10; i++)
    parent[i] = 0;

  int ne = 1;
  while (ne < n)
  {
    int min = INT_MAX, a = -1, b = -1;
    for (int i = 1; i <= n; i++)
    {
      for (int j = 1; j <= n; j++)
      {
        if (cost[i][j] < min && cost[i][j] != INT_MAX)
        {
          min = cost[i][j];
          a = i;
          b = j;
        }
      }
    }

    int u = a, v = b;
    while (parent[u])
      u = parent[u];
    while (parent[v])
      v = parent[v];

    if (u != v)
    {
      cout << "\n"
           << ne++ << " edge (" << a << "," << b << ") = " << min << "\n";
      mincost += min;
      parent[v] = u;
    }

    cost[a][b] = cost[b][a] = INT_MAX; // Mark this edge as visited
  }

  cout << "\nMinimum cost = " << mincost << "\n";
  return 0;
}