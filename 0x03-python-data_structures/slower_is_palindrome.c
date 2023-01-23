#include "lists.h"
/**
 *is_palindrome - a function that checks if a linked list is palindrome
 *@head: the pointer to address of the head of the linked list
 *
 *Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *b_end, *end;

	if ((*head) == NULL)
		return (1);
	while ((*head) && (*head)->next)
	{
		if ((*head)->next == NULL)
			return (1);
		b_end = (*head)->next;
		end = b_end->next;

		if (end == NULL)
		{
			if ((*head)->n != b_end->n)
				return (0);
			return (1);
		}
		while (end->next)
		{
			b_end = end;
			end = end->next;
		}
		if ((*head)->n != end->n)
			return (0);
		b_end->next = NULL;
		(*head) = (*head)->next;
	}
	return (1);
}
