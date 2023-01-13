#include "lists.h"
/**
 *insert_node - a function that adds a number to a linked list
 *@head: the head of the linked list
 *@number: the number to be added
 *
 *Return: return the address of the node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next != NULL && current->next->n < number)
			current = current->next;
		new->next = current->next;
		current->next = new;
	}

	return (new);
}
