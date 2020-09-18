#include <iostream>
#include <vector>


class Graph {
    private:
    std::vector<std::vector<int>> E; // a list of edges for each vertex
    std::vector<int> ccnum; // tells us which connected component a vertex belongs to
    int sizeV;

    public:
    Graph(int numV) {
        sizeV = numV;
        for (int i = 0; i < numV; i++) {
            std::vector<int> edges;
            E.push_back(edges);
        }
        for (int i = 0; i < numV; i++) {
            ccnum.push_back(-1);
        }
    }
    void addUndirectedEdge(int u, int v) {
        E[u].push_back(v);
        E[v].push_back(u);
    }
    std::vector<int> getEdges(int vertex) {
        return E[vertex];
    }
    void updateCC(int vertex, int connectedComponent) {
        ccnum[vertex] = connectedComponent;
    }
    int getCC(int vertex) {
        return ccnum[vertex];
    }
    int getSizeV() {
        return sizeV;
    }
};

void previsit(int vertex, int ccnum, Graph& G) {
   G.updateCC(vertex, ccnum); 
}
void explore(int vertex, bool* visited, Graph& G, int ccnum) {
     visited[vertex] = true;
     std::vector<int> edges = G.getEdges(vertex);
     int numEdges = edges.size();
     previsit(vertex, ccnum, G);
     for (int i = 0; i < numEdges; i++) {
         int u = edges[i];
         if (!visited[u]) {
             explore(u, visited, G, ccnum);
         }
     }
}
void dfs(Graph& G) {
    int sizeV = G.getSizeV();
    bool visited[sizeV] = { 0 };
    int ccnum = 0;
    for (int v = 0; v < sizeV; v++) {
        if (!visited[v]) {
             explore(v, visited, G, ccnum);
             ccnum++;
        }
    }

}
int main() {
    int numHouses;
    int numCables;
    std::cin >> numHouses;
    std::cin >> numCables;
    int houseA;
    int houseB;
    Graph G(numHouses);
    for (int i = 0; i < numCables; i++) {
        std::cin >> houseA;
        std::cin >> houseB;
        G.addUndirectedEdge(houseA-1, houseB-1);
    }
    dfs(G);
    bool notConnected = false;
    for (int v = 0; v < numHouses; v++) {
        int ccnum = G.getCC(v);
            if (ccnum != 0) {
                notConnected = true;
                std::cout << v+1 << '\n';
            }
    }
    if (!notConnected) {
        std::cout << "Connected" << '\n';
    }
    return 0;
}