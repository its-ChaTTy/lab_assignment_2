#include <stdio.h>
#include <stdlib.h>

// Function to validate user input
int getNumber(const char *prompt) {
    char buffer[256];
    char *end;
    long number;

    // Prompt the user for input
    printf("%s", prompt);

    // Read the user's input
    if (!fgets(buffer, sizeof(buffer), stdin)) {
        // If fgets fails, exit the program
        fprintf(stderr, "Error: Unable to read user input\n");
        exit(EXIT_FAILURE);
    }

    // Convert the user's input to a number
    number = strtol(buffer, &end, 10);

    // Check if the user's input was a valid number
    if (end == buffer || *end != '\n') {
        fprintf(stderr, "Error: Invalid input\n");
        exit(EXIT_FAILURE);
    }

    // Return the number
    return (int)number;
}

int main() {
    int num1, num2, sum;

    // Get the first number from the user
    num1 = getNumber("Enter the first number: ");

    // Get the second number from the user
    num2 = getNumber("Enter the second number: ");

    // Calculate the sum of the two numbers
    sum = num1 + num2;

    // Print the result
    printf("The sum of %d and %d is %d\n", num1, num2, sum);

    return 0;
}