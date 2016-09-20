#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <time.h>
#include <windows.h>

using namespace std;

void getColumn();
void instruction();
void getRoll(int i);
void checkNum1(string &s);
void GetGrid(vector<char> v);
void checkNum(string &s, bool &save1);
void saveFile(vector<char> v, vector<int> step, vector<int> sleep, int pl, int len, int countAll, string s);
void loadFile(vector<char> &v, vector<int> &step, vector<int> &sleep, bool &win, int &N, int &pl, int &len, int &countAll, string yn);
bool ifYN(string &yn);
bool isDigits(const std::string &str);
bool checkLegal(vector<char> v, int a, int b);
bool CheckWin(vector<char> v, int a, int b, int len);
bool checkSquareUp(vector<char> v, int a, int b, int count, int len);
bool checkSquareLeft(vector<char> v, int a, int b, int count, int len);
bool checkSquareRight(vector<char> v, int a, int b, int count, int len);
bool checkSquareDown(vector<char> v, int a, int b, int count, int len);
int Ind(int x, int y);
int N;
string f;
bool win = false;

int main()
{
	clock_t t;
	int pl, x, y, len, countAll = 0, countDraw = 0, countForreplay = 0;
	bool draw = false, re = false, first = false, save = false, save1 = false;;
	string yn, a, b, players = "XOABCDEFGHIJKLMNPQRSTUVWYZ";
	vector<char>grid;
	vector<int>step;
	vector<int>sleep;
	instruction();
	cout << "Do you want to load game? (y / n)";
	cin >> yn;
	if (ifYN(yn))//if player choose to load file
	{
		cout << "Please enter the file name: ";
		cin >> yn;
		loadFile(grid, step, sleep, win, N, pl, len, countAll, yn);
		cout << "replay? (y / n)" << endl;
		cin >> yn;
		if (ifYN(yn))
		{
			re = true;
			yn = "n";
		}
		if (!re) //if player choose not to replay
		{
			GetGrid(grid);//if this game already had a winner, print it out
			if (win)	cout << "Congradulations! Player " << players[(countAll - 1) % pl] << " wins!" << endl;
		}
		else //if player choose to replay
		{
			for (int i = 0; i < N*N; i++)grid[i] = ' ';
			GetGrid(grid);
			if (countAll == N*N && !win) draw = true;//if it's a draw
		}
	}
	else//if player choose not load file
	{
		cout << "Please choose the size of the board: ";
		cin >> a;
		checkNum1(a);
		N = atoi(a.c_str());
		cout << "Please choose the winning sequence: ";
		cin >> a;
		checkNum1(a);
		len = atoi(a.c_str());
		while (len > N) 
		{
			cout << "The max sequence is " << N << "!" << endl;
			cin >> a;
			checkNum1(a);
			len = atoi(a.c_str());
		}
		cout << "How many players? (2-26) " << endl;
		cin >> a;
		checkNum1(a);
		pl = atoi(a.c_str());
		for (int i = 0; i < N*N; i++) grid.push_back(' ');//if no file loaded in, initialize the grid
		GetGrid(grid);
	}
	while (!win && countAll != N*N || draw || re)//step by step
	{
		if (draw)//if the game being replayed is draw
		{
			countDraw++;
			if (countDraw == N*N) draw = false;
		}
		string s;
		bool legal = false;
		while (!legal)//while the input is not legal, keep inputing
		{
			if (save == false)//if the player diden't save the game
			{
				if (!re) cout << endl << "Player " << players[countAll % pl] << " turn:";
				else cout << endl << "Player " << players[countForreplay / 2 % pl] << " turn:";
				if (!re)
				{
					t = clock();
					cout << endl << "Roll <<==== ";
					cin >> a;
					checkNum(a, save1);//to give player the convenience to save whenever he likes
					if (!save1) {
						x = atoi(a.c_str());
						cout << "Column <<== ";
						cin >> b;
						checkNum(b, save1);
						if (!save1) {
							y = atoi(b.c_str());
							t = clock() - t;
							sleep.push_back(t);
						}
						if (save1)save = true;//I know it's redundant, but I have to ....
					}
					if (save1)save = true;
				}
				else
				{
					cout << endl << "Replay step:  " << countForreplay / 2 + 1 << endl;
					x = step[countForreplay];
					y = step[countForreplay + 1];
					cout << "Player chose: roll ==>> " << x << "  " << "column ==>> " << y << endl;
					countForreplay += 2;
				}
			}
			if (save == true)
			{
				cout << "Please enter the file's name that you want to save in (no suffix): ";
				cin >> s;
				s = s + ".txt";
				saveFile(grid, step, sleep, pl, len, countAll, s);
				break;
			}
			legal = checkLegal(grid, x, y);
			if (!re && legal)
			{
				step.push_back(x);
				step.push_back(y);
				cout << endl;
			}
			if (re && countForreplay >= 2 * countAll)
			{
				cout << "Replay is over after next board" << endl;
				first = true;//the first step after repaly stops
				re = false;//it's very tricky here! 
			}//if replay step bigger than it should be, stop replay.
		}//end of an input
		if (save) break;
		if (re || first) grid[Ind(x, y)] = players[(countForreplay - 2) / 2 % pl];
		else grid[Ind(x, y)] = players[countAll % pl];
		win = CheckWin(grid, x, y, len);
		if (re || first)
		{
			cout << "Time consumed by player = " << sleep[countForreplay / 2 - 1] / 1000.0 << "s" << endl;
			Sleep(sleep[countForreplay / 2 - 1]);
		}
		GetGrid(grid);
		if (!re && !first && save1) save = true;
		if (!re && !first) countAll++;//not replay and not the first step after replay
		if (win == true)
		{
			cout << "Congradulations! Player " << players[(countAll - 1) % pl] << " wins!" << endl;
			if (!first)
			{
				cout << "Save this game? (y / n)";
				cin >> yn;
				while (yn != "y" && yn != "n") {
					cout << "Please choose y or n: ";
					cin >> yn;
				}
			}
			if (yn == "y")save = true;
			if (save)
			{
				cout << "Please enter the file's name that you want to save in (no suffix): ";
				cin >> s;
				s = s + ".txt";
				saveFile(grid, step, sleep, pl, len, countAll, s);
			}
			break;
		}
		if (first = true) first = false;
	}
	if (countAll == N*N && !win)
	{
		cout << "It ends in a draw!" << endl << "Save this game ? (y / n)";
		cin >> yn;
		if (ifYN(yn)) save = true;
		if (save)
		{
			string s;
			cout << "Please enter the file's name that you want to save in (no suffix): ";
			cin >> s;
			s = s + ".txt";
			saveFile(grid, step, sleep, pl, len, countAll, s);
		}
		win = true;
	}
}

inline int Ind(int x, int y) // The function converts coordinate into index.-------------//motified to 9999*9999
{
	return (x-1)*N - 1 + y;
}

bool checkLegal(vector<char> v, int a, int b)
{
	if (a < 1 || b < 1 || a > N || b > N) // If the coordinate is out of range, tell player to input another coordinate.
	{
		cout << "Out of board! Please use another coordinate" << endl;
		return false;
	}
	else if (v[Ind(a, b)] != ' ') // If the grid is occupied by one of the player, tell player to input another coordinate.
	{
		cout << "This grid has already been occupied! Please use another coordinate" << endl;
		return false;
	}
	else return true;
}

bool CheckWin(vector<char> v, int a, int b, int len) {
	int ta = a, tb = b, count = 1;//------->>>>Left
	bool square = false;
	while (b - 1 > 0 && v[Ind(a, b - 1)] == v[Ind(a, b)] && v[Ind(a, b - 1)] != ' ')//move to left, until the same gird is over
	{
		b--;
		count++;
		if (b - 1 < 1) break;
	}
	if (count >= len) return true;
	count = 1;
	while (b + 1 <= N && v[Ind(a, b + 1)] == v[Ind(a, b)] && v[Ind(a, b + 1)] != ' ')//when left is over, move to right until it's over
	{
		b++;
		count++;
		if (b + 1 > N) break;
	}
	if (count >= len) return true;//if the length of the same line is over winning sequence, return ture
	if (count == len - 1) {
		if (checkSquareUp(v, a, b, count, len)) return true;
		if (checkSquareDown(v, a, b, count, len)) return true;
	}
	count = 1, a = ta, b = tb;//------->>>>Left up
	while (a - 1 > 0 && b - 1 > 0 && v[Ind(a - 1, b - 1)] == v[Ind(a, b)] && v[Ind(a - 1, b - 1)] != ' ')
	{
		a--;
		b--;
		count++;
		if (a - 1 < 1 || b - 1 < 1) break;
	}
	if (count >= len) return true;
	count = 1;
	while (a + 1 <= N && b + 1 <= N && v[Ind(a + 1, b + 1)] == v[Ind(a, b)] && v[Ind(a + 1, b + 1)] != ' ')
	{
		a++;
		b++;
		count++;
		if (a + 1 > N || b + 1 > N) break;
	}
	if (count >= len) return true;
	count = 1, a = ta, b = tb;//------->>>>Up
	while (a - 1 > 0 && v[Ind(a - 1, b)] == v[Ind(a, b)] && v[Ind(a - 1, b)] != ' ')
	{
		a--;
		count++;
		if (a - 1 < 1) break;
	}
	if (count >= len) return true;
	count = 1;
	while (a + 1 <= N && v[Ind(a + 1, b)] == v[Ind(a, b)] && v[Ind(a + 1, b)] != ' ')
	{
		a++;
		count++;
		if (a + 1 > N) break;
	}
	if (count >= len) return true;
	if (count == len - 1) {
		if (checkSquareLeft(v, a, b, count, len)) return true;
		if (checkSquareRight(v, a, b, count, len)) return true;
	}
	count = 1, a = ta, b = tb;//------->>>>Right up
	while (a - 1 > 0 && b + 1 <= N && v[Ind(a - 1, b + 1)] == v[Ind(a, b)] && v[Ind(a - 1, b + 1)] != ' ')
	{
		a--;
		b++;
		count++;
		if (a - 1 < 1 || b + 1 > N) break;
	}
	if (count >= len) return true;
	count = 1;
	while (a + 1 <= N && b - 1 > 0 && v[Ind(a + 1, b - 1)] == v[Ind(a, b)] && v[Ind(a + 1, b - 1)] != ' ')
	{
		a++;
		b--;
		count++;
		if (a + 1 > N || b - 1 < 1) break;
	}
	if (count >= len) return true;
	return false;
}

void saveFile(vector<char> v, vector<int> step, vector<int> sleep, int pl, int len, int countAll, string s)
{
	ofstream outfile(s);
	outfile << N << ' ' << pl << ' ' << len << ' ' << countAll;
	for (int i = 0; i < N*N; i++) outfile << v[i];
	outfile << '*';
	for (int i = 0; i < 2 * countAll; i++) outfile << step[i] << ' ';
	for (int i = 0; i < countAll; i++) outfile << sleep[i] << ' ';
	outfile << win;//if the game already has a winner, i need to know the loading file is a win situation
	outfile.close();
	win = true;
	cout << "******File saved successfully!******" << endl << endl;
}

void loadFile(vector<char> &v, vector<int> &step, vector<int> &sleep, bool &win, int &N, int &pl, int &len, int &countAll, string yn)
{
	char symbol;
	int sp;
	bool file;
	yn = yn + ".txt";
	string truefile = yn;
	ifstream infile(yn);
	file = infile.fail();
	while (file)
	{
		cout << "Input file opening failed, please input another file name: ";
		cin >> yn;
		ifstream infile(yn);
		file = infile.fail();
		truefile = yn;
	}
	ifstream infileTrue(truefile);
	infileTrue >> N >> pl >> len >> countAll;
	cout << endl << endl;
	cout << "The size of board = " << N << endl << endl;
	cout << "The winning sequence = " << len << endl << endl;
	cout << "Number of players = " << pl << endl << endl;
	cout << "Number of all steps = " << countAll << endl << endl; cout << endl;
	while (true)
	{
		infileTrue.get(symbol);
		if (symbol == '*') break;
		v.push_back(symbol);
	}
	for (int i = 0; i < 2 * countAll; i++)
	{
		infileTrue >> sp;
		step.push_back(sp);
	}
	for (int i = 0; i < countAll; i++)
	{
		infileTrue >> sp;
		sleep.push_back(sp);
	}
	infileTrue >> sp;
	win = (sp == 1);
	infile.close();
	infileTrue.close();
}

bool isDigits(const string &str)
{
	return str.find_first_not_of("0123456789") == string::npos;
}

void checkNum(string &s, bool &save1)
{
	while (!isDigits(s))
	{
		if (s == "Exit")
		{
			save1 = true;
			break;
		}
		cout << "Please input an integer!(or \" Exit \" to save)" << endl;
		cin >> s;
	}
}

void checkNum1(string &s)
{
	int num = atoi(s.c_str());
	while (!isDigits(s) || num <= 0)
	{
		if (!isDigits(s)) 
		{
			cout << "Please input an integer!" << endl;
			cin >> s;
		}
		else if(num=atoi(s.c_str())<=0)
		{
			cout << "Please input a number bigger than 0!" << endl;
			cin >> s;
		}
		num = atoi(s.c_str());
	}
}

bool checkSquareUp(vector<char> v, int a, int b, int count, int len)
{
	int sa = a, sb = b, rsa = a;
	count = 0;
	while (sa - len + 2 > 0 && sb - len + 2 > 0 && v[Ind(a, sb)] == v[Ind(sa - len + 2, b)] && v[Ind(rsa - len + 2, sb - len + 2)] == v[Ind(sa - len + 2, b)])//if the grid in each corner is all the same
	{
		a--;
		b--;
		rsa++;
		count++;
		if (rsa - len + 2 >= sa) break;
	}
	if (count == len - 2) return true;
	else return false;
}

bool checkSquareDown(vector<char> v, int a, int b, int count, int len)///////////////////////
{
	int sa = a, sb = b, rsa = a;
	count = 0;
	while (sa + len - 2 < N && sb - len + 2 > 0 && v[Ind(a, sb)] == v[Ind(sa + len - 2, b)] && v[Ind(rsa + len - 2, sb - len + 2)] == v[Ind(sa + len - 2, b)])//if the grid in each corner is all the same
	{
		a++;
		b--;
		rsa--;
		count++;
		if (rsa + len - 2 <= sa) break;
	}
	if (count == len - 2) return true;
	else return false;
}

bool checkSquareLeft(vector<char> v, int a, int b, int count, int len)
{
	int sa = a, sb = b, rsb = b;
	count = 0;
	while (sa - len + 2 > 0 && sb - len + 2 > 0 && v[Ind(sa, b)] == v[Ind(a, sb - len + 2)] && v[Ind(sa - len + 2, rsb - len + 2)] == v[Ind(a, sb - len + 2)])//if the grid in each corner is all the same
	{
		a--;
		b--;
		rsb++;
		count++;
		if (rsb - len + 2 >= sb) break;
	}
	if (count == len - 2) return true;
	else return false;
}

bool checkSquareRight(vector<char> v, int a, int b, int count, int len)
{
	int sb = b, sa = a, rsb = b;
	count = 0;
	while (sa - len + 2 > 0 && sb + len - 2 < N && v[Ind(sa, b)] == v[Ind(a, sb + len - 2)] && v[Ind(sa - len + 2, rsb + len - 2)] == v[Ind(a, sb + len - 2)])//if the grid in each corner is all the same
	{
		a--;
		b++;
		rsb--;
		count++;
		if (rsb + len - 2 <= sb) break;
	}
	if (count == len - 2) return true;
	else return false;
}

void instruction()
{
	cout << endl << endl << "***************************************INSTRCTIONS*******************************************" << endl << endl;
	cout << "[1]  The maximum number of players is 26." << endl;
	cout << "[2]  The maximum board size is 99, theoretically (no more than 38 normally)." << endl;
	cout << "[3]  If the winning sequence is bigger than size of the board, you will be required to use another sequence." << endl;
	cout << "[4]  You can choose to \"save and exit\" whenever you like, just input \"Exit\" during the game. i.e. Roll: Exit" << endl << "     (You can even save the game when the game is over, in case you want to replay the game)" << endl;
	cout << "[5]  You can choose to load game at the beginning, and replay (or not) the game after loading." << endl;
	cout << "[6]  Every step replayed on the screen will take exactly the same time that it was originally played." << endl;
	cout << "[7]  Every illegal input requires a correction, i.e. wrong file name or wrong roll number." << endl << endl;
	cout << "Winning by sqare(which side = winning sequence - 1) is allowed(hollow),for example:" << endl << endl;
	cout << "                                                                           X  X  X  X" << endl;
	cout << "When N=5, player \" X \" will win the game in this situation:                X        X" << endl;
	cout << "(A single step will NOT be counted as a square)                            X        X" << endl;
	cout << "                                                                           X  X  X  X" << endl;
}

void GetGrid(vector<char> v) //motified to 9999*9999
{
	string Nf = to_string(N);
	string shape, blank;
	f = to_string(N);
	for (size_t p = 0; p < f.length() + 1; p++) blank += " ";
	for (int o = 1; o < N; o++) shape += "---+";
	shape = blank + shape + "---";
	for (size_t p = 0; p < f.length(); p++) cout << " ";
	cout << " ";
	getColumn();
	cout << endl;//output the column number
	for (int i = 1; i < 2 * N; i++) 
	{
		if (i % 2 != 0) 
		{
			getRoll(i);
			for (int j = 1; j < N; j++) cout << " " << v[((i / 2 + 1) - 1)*N - 1 + j]<< " |";
			cout << " " << v[((i / 2 + 1) - 1)*N - 1 + N] <<endl;
		}
		else cout << shape << endl;
	}
}

void getColumn() 
{
	string Nf = to_string(N);
	for (int c = 1; c <= N; c++) 
	{
		f = to_string(c);
		if(c<10) cout << " " << c << "  ";
		else 
		{
			if (f.length() < 3) for (size_t j = 0; j < 3 - f.length(); j++) cout << " ";
			for (size_t i = 0; i < f.length(); i++) cout << f[i];
			if (f.length() <= 3) cout << " ";
		}
	}
}

void getRoll(int i) 
{
	string Nf = to_string(N);
	f = to_string(i / 2 + 1);
	if (f.length() < Nf.length()) for (size_t j = 0; j < Nf.length() - f.length(); j++) cout << " ";
	for (size_t i = 0; i < f.length(); i++) cout << f[i];
	cout << " ";
}

bool ifYN(string &yn) 
{
	while (yn != "y" && yn != "n")
	{
		cout << "Please choose y or n: ";
		cin >> yn;
	}
	return yn == "y";
}