#include "lists.h"
/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Head node of linkedlist
 * Return: 1 if palindrome 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *head_ptr = *head;
	listint_t *tail_ptr = *head;
	listint_t *floater;
	int l = 0;
	int i = 0;

	if (head_ptr == NULL || head_ptr->next == NULL)
		return (1);
	do {
		l++;
		tail_ptr = tail_ptr->next;
	} while (tail_ptr->next);
	while (i < l / 2)
	{
		if (head_ptr->n == tail_ptr->n)
		{
			if (i == ((l / 2) - 1))
				return (1);
			head_ptr = head_ptr->next;
			floater = head_ptr;
			while (floater)
			{
				if (floater->next->n == tail_ptr->n)
				{
					tail_ptr = floater;
					break;
				}
				floater = floater->next;
			}
		}
		else
		{
			return (0);
		}
		i++;
	}
	return (0);
}
