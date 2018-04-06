#include <iostream>
#include <sys/ioctl.h>
#include <stdio.h>
#include <unistd.h>

int main() {
	struct winsize w;
	ioctl(STDOUT_FILENO, TIOCGWINSZ, &w);

	int input = 0;

	for (int i = 0; i < w.ws_col; i++) {
		std::cout << "-";
	}
	for (int j = 1; j < w.ws_row-2; j++) {
		std::cout << "-";
		for (int i = 1; i < w.ws_col-1; i++) {
			std::cout << " ";
		}
		std::cout << "-";
		std::cout << std::endl;
	}
	for (int i = 0; i < w.ws_col; i++) {
		std::cout << "-";
	}
	// std::cout << "please w.ws_row enter a number: " << w.ws_row;
	// std::cin >> input;
	// std::cout << "hello world. Your input was: "
	//	<< input << std::endl;
}
