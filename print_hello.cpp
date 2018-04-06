#include <iostream>
#include <sys/ioctl.h>
#include <stdio.h>
#include <unistd.h>
int check(int x, int y) {
	if (x%4 == 0 && y%4 == 0 || )
	   )
}

int main() {
	#ifdef __linux__
	struct winsize w;
	ioctl(STDOUT_FILENO, TIOCGWINSZ, &w);

	int input = 0;
	
	for (int i = 0; i < w.ws_col; i++) {
		for (int j = 0; j < w.ws_row; j++) {
		}
	}
	#endif
	// std::cout << "please w.ws_row enter a number: " << w.ws_row;
	// std::cin >> input;
	// std::cout << "hello world. Your input was: "
	//	<< input << std::endl;
}
