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
	listint_t *curr = NULL;
	listint_t *check = NULL;

	curr = *head;
	after = *head;
	check = *head;

	while (after->next != NULL)
	{
		after = after->next;
	}

	curr = curr->next;

	while (check->next->next != NULL)
	{
		check = check->next;
	}

	if (after->n == (*head)->next->n && curr->n == check->n)
	{
		return (0);
	}

	return (1);
}
