#include "lists.h"
/**
 * print_listint - Function that prints the linked lists
 *
 * @h: Pointer to the head
 *
 * Return: the number of element of the list
 */
size_t print_listint(const listint_t *h)
{
	int i;

	i = 0;
	while (h != NULL)
	{
		printf("%d\n", h->n);
		h = h->next;
		i++;
	}
	return (i);
}
