#include <iostream>
#include <unistd.h>
#include <math.h>
#ifdef __linux__
#include <sys/ioctl.h>
#include <string.h>
#include <sstream>
#include <fstream>
#define BUF_SIZE 4096

#elif _WIN32
#include <windows.h>
#endif
int a[] = { 0b000000000000000000000000000000,
	    0b111111111100001111111111110000,
	    0b111111111100001111111111110000,
	    0b000001111100001111000011110000,
	    0b111111111100001111000011110000,
	    0b111111111100001111000011110000,
	    0b111111111100001111000011110000,
	    0b000001111100001111000011110000,
	    0b000001111100001111000011110000,
	    0b000001111100001111000011110000,
	    0b000001111100001111000011110000,
	    0b000001111100001111111111110000,
	    0b000001111100001111111111110000,
	    0b000001111100001111111111110000,
	    0b000000000000000000000000000000 };

int check(int x, int y, int x_max, int y_max) {
  if (x == 0 || y == 0 ||
      x == x_max-1 || y == y_max-1) {
    return 1;
  } else if (y < 15 && a[y] & int(powf(2,x)) ) {
    return 1;
  } else {
    return 0;
  }
}

int main() {
#ifdef __linux__
  struct winsize w;
  ioctl(STDOUT_FILENO, TIOCGWINSZ, &w);
  const int width = w.ws_col;
  const int height = w.ws_row-1;
  
#elif _WIN32
  CONSOLE_SCREEN_BUFFER_INFO csbi;
  GetConsoleScreenBufferInfo(GetStdHandle(STD_OUTPUT_HANDLE), &csbi);
  int width = csbi.srWindow.Right - csbi.srWindow.Left + 1;
  int height = csbi.srWindow.Bottom - csbi.srWindow.Top;
#endif
  for (int j = 0; j < height; j++) {
    for (int i = 0; i < width; i++) {
      if (check(i, j, width, height)) {
	std::cout << "-";
      } else {
	std::cout << " ";
      }
    }
    std::cout << std::endl;
  }
  std::string input = "";
  std::string line;
  // std::cin >> input;
  if (input == "What is the name of my city?") {
    std::cout << input;
  }
  std::ifstream infile( "cities" );
  int number = 0;
  do {
    std::cout << "How many letters is your city? _";
    std::cin >> number;
  } while (number < 2 || number > 49);
  
  char inchar = ' ';
  
  do {
    std::cout << "What is the first letter (capitalized)? _";
    std::cin >> inchar;
  } while (inchar < 'A' || inchar > 'Z');
  
  while (std::getline(infile, line)) {
    if (line.length() == number && line[0] == inchar) {
      std::cout << line << std::endl;
    }
  }

  // std::cout << "please w.ws_row enter a number: " << w.ws_row;
  // std::cin >> input;
  // std::cout << "hello world. Your input was: "
  //	<< input << std::endl;
}
