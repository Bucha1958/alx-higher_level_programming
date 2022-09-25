#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: list to be checked
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *tmp = list;
	
	while (tmp != NULL && first->next != NULL && first->next->next != NULL)
	{
		first = first->next->next;
		tmp = tmp->next;

		if (first == tmp)
			return (1);
	}
	return (0);
}
