#include "lists.h"
#include <stdio.h>
void reverse(listint_t **head);
/**
 * is_palindrome - Checks if a singly linked is a palindrome
 * @head: Pointer to pointer of the first node in listint_t list.
 * Return: 0 if not a palindrome, 1 if it is a palindrome
 *
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr;
	listint_t *fast_ptr;
	listint_t *first_half_head;
	listint_t *second_half_head;

	slow_ptr = *head;
	fast_ptr = *head;
	// if the list is empty, it is a palindrome
	if (head == NULL || *head == NULL)
		return (1);
	while (fast_ptr->next != NULL && fast_ptr->next->next != NULL)
	{
		fast_ptr = fast_ptr->next->next;
		slow_ptr = slow_ptr->next;
	}
	// Reverse the second half using the slow_ptr
	second_half_head = slow_ptr;
	reverse(&second_half_head);
	first_half_head = *head;
	// Compare the two halves
	while (second_half_head != NULL && first_half_head != NULL)
	{
		if (first_half_head->n != second_half_head->n)
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
 * reverse - Function that reverses the linked lists
 *
 * @head: pointer to pointer to the head node
 *
 *
 */
void reverse(listint_t **head)
{
	listint_t *temp = *head;
	listint_t *next;
	listint_t *prev = NULL;

	while (temp != NULL)
	{
		next = temp->next;
		temp->next = prev;
		prev = temp;
		temp = next;
	}
	*head = prev;
}
