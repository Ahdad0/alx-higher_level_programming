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

	curr = malloc(sizeof(listint_t));
	if (curr == NULL)
	{
		return (NULL);
	}

	after = malloc(sizeof(listint_t));
	if (after == NULL)
	{
		return (NULL);
	}

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
		free(curr);
		free(after);
		return (0);
	}

	free(curr);
	free(after);
	return (1);
}
