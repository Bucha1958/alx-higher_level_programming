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
	
	if (list == NULL)
		return (0);
	while (tmp && first)
	{
		if (first->next == NULL)
			return (false);
		tmp = tmp->next;
		first = first->next->next;
		if (tmp == first)
			return (1);
	}
	return (0);
}
