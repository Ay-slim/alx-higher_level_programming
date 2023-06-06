#include "lists.h"

/**
 * create_node - Creates a node for a linkedlist
 * @n: Number to include
 * @next_val: Next node
 * Return: Returns a pointer to the created node
 */
listint_t *create_node(int n, listint_t *next_val)
{
	listint_t *new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);
	new->n = n;
	new->next = next_val;
	return (new);
}

/**
 * insert_node - Inserts a node into a sorted linked list
 * @head: Pointer to pointer to linked list head node
 * @number: Number to insert
 * Return: Pointer to created node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new;
	listint_t *next_chk;

	if (!current || number <= current->n)
	{
		new = create_node(number, current);
		if (new == NULL)
			return (NULL);
		**head = *new;
		return (new);
	}
	current = current->next;
	while (current)
	{
		if (number >= current->n)
		{
			next_chk = current->next;
			if (!next_chk || number <= next_chk->n)
			{
				new = create_node(number, current->next);
				if (new == NULL)
					return (NULL);
				current->next = new;
				return (new);
			}
		}
		current = current->next;
	}
	return (NULL);
}
