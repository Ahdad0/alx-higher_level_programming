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
	listint_t *after = NULL;

	after = *head;

	while (after->next != NULL)
	{
		after = after->next;
	}

	if (after->n == (*head)->next->n)
	{
		return (0);
	}

	return (1);
}
