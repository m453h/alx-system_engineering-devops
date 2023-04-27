#include <stdio.h>
#include <unistd.h>

/**
* infinite_while - creates an infinite loop to make the program hang
* Return: always 0
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
* main - Creates 5 zombie processes
* Return: (int) always 0
*/
int main(void)
{
	int process_counter = 0;
	pid_t zombie_pid;

	while (process_counter < 5)
	{
		zombie_pid = fork();

		if (!zombie_pid)
			return (0);

		printf("Zombie process created, PID: %d\n", process_counter);
		process_counter++;
	}

	infinite_while();

	return (0);
}

