#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - Inserts a number into a sorted linked list.
 * @head: Pointer to the pointer of the first node of listint_t list.
 * @number: Integar to be included into the new node.
 * Return: Upon success the address of the new node. Otherwise NULL.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *link;
	listint_t *new_node;

	if (head == NULL)
		return (NULL);
	link = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	/*adding values to the new node*/
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL)
	{
		return (new_node);
	}
	/*Handling special case for first node insertion*/
	if (link->n > number)
	{
		*head = new_node;
		new_node->next = link;
		return (new_node);
	}
	/*Traversing the linked list to find the right location for the node*/
	while (link->next != NULL)
	{
		if (link->next->n > number)
		{
			new_node->next = link->next;
			link->next = new_node;
			return (new_node);
		}
		link = link->next;
	}
	link->next = new_node;
	return (new_node);
}
