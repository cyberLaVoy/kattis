#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <map>

void gatherLayout(int rows, int cols, std::vector<std::vector<int>>& layout) {
    std::string line;
    for (int i = 0; i < rows; i++) {
        std::cin >> line;
        std::vector<int> row;
        for (int j = 0; j < cols; j++) {
            if (line[j] == '1') { 
                row.push_back(1);
            }
            else {
                row.push_back(0);
            }
        }
        layout.push_back(row);
    }
}
void gatherMoves(std::vector<std::map<std::string, std::pair<int, int>>>& moves) {
    int numMoves;
    std::cin >> numMoves;
    for (int i = 0; i < numMoves; i++) {
        int x1, y1, x2, y2;
        std::cin >> x1;
        std::cin >> y1;
        std::cin >> x2;
        std::cin >> y2;
        std::pair<int, int> start ( x1-1, y1-1 );
        std::pair<int, int> end ( x2-1, y2-1 );
        std::map<std::string, std::pair<int, int>> move;
        move["from"] = start;
        move["to"] = end;
        moves.push_back(move);
    }
}

void fillR(std::vector<std::vector<int>>& layout, int i, int j, bool searchValue, std::vector<std::pair<int, int>>& coordinates) {
    std::pair<int, int> coordinate (i, j); 
    coordinates.push_back(coordinate);
    layout[i][j] = 2;
    if ( i+1 < (int)layout.size() && layout[i+1][j] == searchValue )
        fillR(layout, i+1, j, searchValue, coordinates);
    if ( i-1 >= 0 && layout[i-1][j] == searchValue )
        fillR(layout, i-1, j, searchValue, coordinates);
    if ( j+1 < (int)layout[i].size() && layout[i][j+1] == searchValue )
        fillR(layout, i, j+1, searchValue, coordinates);
    if ( j-1 >= 0 && layout[i][j-1] == searchValue )
        fillR(layout, i, j-1, searchValue, coordinates);
}
std::vector<std::pair<int, int>> fill(std::vector<std::vector<int>>& layout, int i, int j, bool searchValue) {
    std::vector<std::pair<int, int>> coordinates;
    fillR(layout, i, j, searchValue, coordinates);
    return coordinates;
}


//  returns a dict of connected components
void findCoordinates(std::vector<std::vector<int>> layout, int rows, int cols, bool searchValue,std::map<int, std::vector<std::pair<int, int>>>& coordinates ) {
    int ccNum = 0;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (layout[i][j] == searchValue) {
                
                coordinates[ccNum] = fill(layout, i, j, searchValue); 
                ccNum += 1;
            }
        }
    }
}

void describeCoordinates(std::map<int, std::vector<std::pair<int, int>>> zeroCoordinates, std::map<int, std::vector<std::pair<int, int>>> oneCoordinates,std::map<std::pair<int, int>, std::map<std::string, int>>& descriptions ) {
    std::map<int, std::vector<std::pair<int, int>>>::iterator it;
    for (it = zeroCoordinates.begin(); it != zeroCoordinates.end(); it++) {
        int cc = it->first;
        std::vector<std::pair<int, int>> coordinates = it->second;
        for (int i = 0; i < (int)coordinates.size(); i++) {
            std::map<std::string, int> description;
            description["region"] = 0;
            description["cc"] = cc;
            descriptions[coordinates[i]] = description;
        }
    }
    for (it = oneCoordinates.begin(); it != oneCoordinates.end(); it++) {
        int cc = it->first;
        std::vector<std::pair<int, int>> coordinates = it->second;
        for (int i = 0; i < (int)coordinates.size(); i++) {
            std::map<std::string, int> description;
            description["region"] = 1;
            description["cc"] = cc;
            descriptions[coordinates[i]] = description;
        }
    }
}

int main() {
    int rows, cols;
    std::cin >> rows;
    std::cin >> cols;
    std::vector<std::vector<int>> layout;
    gatherLayout(rows, cols, layout);
    std::vector<std::map<std::string, std::pair<int, int>>> moves;
    gatherMoves(moves);
    std::map<int, std::vector<std::pair<int, int>>> zeroCoordinates, oneCoordinates;
    findCoordinates(layout ,rows, cols, 0, zeroCoordinates); 
    findCoordinates(layout ,rows, cols, 1, oneCoordinates); 
    std::map<std::pair<int, int>, std::map<std::string, int>> coordinates;
    describeCoordinates(zeroCoordinates, oneCoordinates, coordinates);

    for (int i = 0; i < (int)moves.size(); i++) {
        int startRegion = coordinates[moves[i]["from"]]["region"];
        int startCC = coordinates[moves[i]["from"]]["cc"];
        int endRegion = coordinates[moves[i]["to"]]["region"];
        int endCC = coordinates[moves[i]["to"]]["cc"];
        if (startRegion == endRegion && startCC == endCC) {
            if (startRegion == 0) {
                std::cout << "binary" << std::endl;
            }
            else {
                std::cout << "decimal" << std::endl;
            }
        }
        else {
            std::cout << "neither" << std::endl;
        }
    }
    return 0;
}
