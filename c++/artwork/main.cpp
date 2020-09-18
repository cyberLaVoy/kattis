#include <iostream>
#include <vector>

void displayCanvas(const std::vector<std::vector<bool>>& canvas) {
    for (int row = 0; row < (int)canvas.size(); row++) {
        for (int col = 0; col < (int)canvas[row].size(); col++) {
            std::cout << canvas[row][col];
        }
        std::cout << std::endl;
    }
    std::cout << std::endl;
}
void stroke(std::vector<std::vector<bool>>& canvas, int x1, int y1, int x2, int y2 ) {
    for (int row = y1; row <= y2; row++) {
        for (int col = x1; col <= x2; col++) {
            canvas[row][col] = true;
        }
    }
}
void fill(std::vector<std::vector<bool>>& canvas, int row, int col) {
    canvas[row][col] = true;
    if (col+1 < (int)canvas[row].size() && !canvas[row][col+1])
        fill(canvas, row, col+1);
    if (col-1 >= 0 && !canvas[row][col-1])
        fill(canvas, row, col-1);
    if (row+1 < (int)canvas.size() && !canvas[row+1][col])
        fill(canvas, row+1, col);
    if (row-1 >= 0 && !canvas[row-1][col])
        fill(canvas, row-1, col);
}
int dfs(std::vector<std::vector<bool>> canvas) { // recieve canvas, but make a copy to explore
    int sectionCount = 0;
     for (int row = 0; row < (int)canvas.size(); row++) {
        for (int col = 0; col < (int)canvas[row].size(); col++) {
            if (!canvas[row][col]) {
                sectionCount++;
                fill(canvas, row, col);
            }
        }
    }
    return sectionCount;
}


int main() {
    int cols, rows, q; 
    std::cin >> cols >> rows >> q;
    std::vector<std::vector<bool>> canvas(rows, std::vector<bool>(cols));
    int x1, y1, x2, y2;
    for (int i = 0; i < q; i++) {
        std::cin >> x1 >> y1 >> x2 >> y2; 
        x1--; y1--; x2--; y2--;
        stroke(canvas, x1, y1, x2, y2);
        std::cout << dfs(canvas) << std::endl;
    }
    return 0;
}