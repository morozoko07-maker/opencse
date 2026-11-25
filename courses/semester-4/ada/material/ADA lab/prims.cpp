#include <iostream>
#include <limits.h> // For INT_MAX

using namespace std;

int main()
{
  int n; // Number of vertices
  cout << "Enter the number of vertices:\n";
  cin >> n;

  int cost[10][10]; // Cost matrix
  cout << "Enter the adjacency matrix (use 999 for infinity):\n";
  for (int i = 1; i <= n; i++)
  {
    for (int j = 1; j <= n; j++)
    {
      cin >> cost[i][j];
      if (cost[i][j] == 0)
      {
        cost[i][j] = 999; // Representing infinity
      }
    }
  }

  int visited[10] = {0}; // Visited vertices
  visited[1] = 1;        // Start from vertex 1
  int ne = 1;            // Number of edges
  int mincost = 0;       // Minimum cost of the spanning tree

  cout << "The edges of the minimum spanning tree are:\n";
  while (ne < n)
  {
    int min = 999, a = -1, b = -1;
    for (int i = 1; i <= n; i++)
    {
      for (int j = 1; j <= n; j++)
      {
        if (cost[i][j] < min && visited[i] != 0)
        {
          min = cost[i][j];
          a = i;
          b = j;
        }
      }
    }
    if (visited[a] == 0 || visited[b] == 0)
    {
      cout << ne++ << " Edge (" << a << "," << b << ") = " << min << endl;
      mincost += min;
      visited[b] = 1;
    }
    cost[a][b] = cost[b][a] = 999; // Mark as visited
  }
  cout << "\nMinimum cost = " << mincost << endl;
  return 0;
}