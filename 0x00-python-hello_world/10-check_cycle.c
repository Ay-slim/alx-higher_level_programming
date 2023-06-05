#include "lists.h"

/**
 * check_cycle - Function to check if a linked list has a cycle
 * @list: Linked list to check
 * Return: 1 if there is a cycle 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *holder;
	listint_t *variable = list;
	int i = 1;
	int j;

	if (variable->next)
		variable = variable->next;
	while (variable)
	{
		holder = list;
		j = 0;
		while (holder)
		{
			if (holder == variable && i != j)
			{
				return (1);
			}
			holder = holder->next;
			j++;
		}
		variable = variable->next;
		i++;
	}
	return (0);
}

