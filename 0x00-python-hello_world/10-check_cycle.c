#include "lists.h"

/**
 * check_cycle - checks a SLL for cycle
 * @list: list input
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	slow = list;
	fast = list->next;
	while (list != NULL && slow != NULL && fast != NULL && fast->next != NULL)
	{
		if (fast == slow)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
