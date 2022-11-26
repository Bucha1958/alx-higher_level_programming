#include "lists.h"
#include <stdio.h>
void reverse(listint_t **head);
/**
 *
 *
 *
 *
 *
 *
 *
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr = *head;
	listint_t *fast_ptr = *head;
	listint_t *second_half_head;
	listint_t *first_half_head;

	if (head == NULL && *head == NULL)
		return (1);
	while (fast_ptr->next != NULL && fast_ptr->next->next != NULL)
	{
		fast_ptr = fast_ptr->next->next;
		slow_ptr = slow_ptr->next;
	}
	// Get the middle and reverse the second_half of the linked list
	second_half_head = slow_ptr;
	first_half_head = *head;
	reverse(&second_half_head);
	// compare the first_half_head and second_half_head
	while (second_half_head != NULL && first_half_head != NULL)
	{
		if (second_half_head->n != first_half_head->n)
			return (0);
		else
		{
			second_half_head = second_half_head->next;
			first_half_head = first_half_head->next;
		}
	}
	return (1);
}

/**
 *
 *
 *
 *
 *
 */
void reverse(listint_t **head)
{
	listint_t *next;
	listint_t *current;
	listint_t *prev = NULL;

	current = *head;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}

