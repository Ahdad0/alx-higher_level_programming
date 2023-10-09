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
	int store_f[10], store_l[10], i = 0, u = 0, o = 0;

	curr = *head;
	after = *head;

	after = after->next;

	while (after->n != curr->n)
	{
		store_f[i] = curr->n;
		after = after->next;
		curr = curr->next;
		i++;
	}

	store_f[i] = curr->n;
	while (after->next != NULL)
	{
		store_l[u] = after->n;
		after = after->next;
		u++;
	}

	store_l[u] = after->n;

	while (u >= 0 && i >= o)
	{
		if (store_f[o] != store_l[u])
		{
			return (0);
		}
		o++;
		u--;
	}

	return (1);
}
