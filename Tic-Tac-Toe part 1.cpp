#include <iostream>
#include <vector>
using namespace std;
void getGrid(); // Declare the functions that used in this project
bool checkLegal(int a, int b);
void win();
void whowins();
void InputStep(int &a, int &b);
int toIndex(int x, int y);
bool wins = true; // Define global variable
int roundNum = 1;
vector<char> grid(9);

int main()
{
	int a, b; // Put default ' ' into grid(9)
	for (int i = 0; i < 9; i++) {
		grid[i] = ' ';
	}
	getGrid(); // Give players the original board
	while (wins) // This loop stops when someone wins or when the board is running out
	{
		cout << " " << endl;
		cout << "Player X turn: ";
		InputStep(a,b);//input X
		grid[toIndex(a, b)] = 'X'; // Put player's choice into the board
		roundNum++;
		cout << " " << endl;
		getGrid();
		win(); // Test if anybody wins in this round.
		if (roundNum == 10) // Check if the board is running out
		{
			wins = false;
			cout << "It ends in a draw!" << endl;
		}
		if (wins == true) // If there is no winner, go to the next round
		{
			cout << "Player O turn: ";
			InputStep(a,b);//input O
			grid[toIndex(a, b)] = 'O';
			roundNum++;
			cout << " " << endl;
			getGrid();
			win();
		}
	}
	cout << "Game Over!" << endl;
	return 0;
}

void getGrid() // This function gives the board of this game.
{
	cout << "   " << 1 << "   " << 2 << "   " << 3 << endl;
	cout << " " << 1 << " " << grid[0] << " " << "|" << " " << grid[1] << " " << "|" << " " << grid[2] << endl;
	cout << "  " << "---+---+---" << endl;
	cout << " " << 2 << " " << grid[3] << " " << "|" << " " << grid[4] << " " << "|" << " " << grid[5] << endl;
	cout << "  " << "---+---+---" << endl;
	cout << " " << 3 << " " << grid[6] << " " << "|" << " " << grid[7] << " " << "|" << " " << grid[8] << endl;
}

int toIndex(int x, int y) // The function converts coordinate into index.
{
	return (x - 1) * 3 + y - 1;
}

void win() // Because it's a very small board, so I just have all the situation listed and chack if one of them is satified.
{
	if (grid[0] == grid[1] && grid[1] == grid[2] && grid[0] != ' ') whowins();
	if (grid[3] == grid[4] && grid[4] == grid[5] && grid[3] != ' ') whowins();
	if (grid[6] == grid[7] && grid[7] == grid[8] && grid[6] != ' ') whowins();
	if (grid[0] == grid[3] && grid[3] == grid[6] && grid[0] != ' ') whowins();
	if (grid[1] == grid[4] && grid[4] == grid[7] && grid[1] != ' ') whowins();
	if (grid[2] == grid[5] && grid[5] == grid[8] && grid[2] != ' ') whowins();
	if (grid[0] == grid[4] && grid[4] == grid[8] && grid[0] != ' ') whowins();
	if (grid[2] == grid[4] && grid[4] == grid[6] && grid[2] != ' ') whowins();
}

bool checkLegal(int a, int b)
{
	if (a < 1 || b < 1 || a > 3 || b > 3) // If the coordinate is out of range, tell player to input another coordinate.
	{
		cout << "Illegal input! Please use another coordinate" << endl;
		return true;
	}
	else if (grid[toIndex(a, b)] == 'X' || grid[toIndex(a, b)] == 'O') // If the grid is occupied by one of the player, tell player to input another coordinate.
	{
		cout << "This grid has already been occupied! Please use another coordinate" << endl;
		return true;
	}
	else
	{
		return false;
	}
}

void InputStep(int &a,int &b) 
{
	bool v = true;
	while (v) // Test if the input is legal and if the grid has already been occupied
	{
		cout << "Round number: " << roundNum;
		cout << " " << endl;
		cout << "Enter the roll number: ";
		cin >> a;
		cout << "Enter the column number: ";
		cin >> b;
		cout << " " << endl;
		v = checkLegal(a,b);
	}
}

void whowins() 
{
	if(roundNum%2==1) cout << "Player O wins!" << endl;
	else cout << "Player X wins!" << endl;
	wins = false;
}