#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 *
 * @head: head of node
 *
 * Return: 0 if palindrome
 * 1 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *curr = NULL;
	listint_t *after = NULL;

	curr = *head;
	after = *head;

	after = after->next;

	while (curr->n != after->n)
	{
		curr = curr->next;
		after = after->next;
	}

	after = after->next;

	if ((*head)->n == after->n)
	{
		return (0);
	}

	return (1);
}
