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
	listint_t *curr = *head;
	listint_t *count = *head;
	int store_f[10], store_l[10], i = 0, u = 0, o = 0, c = 0;

	if (!(*head) && !(*head)->next)
		return (1);
	while (count != NULL)
	{
		count = count->next;
		c++;
	}
	if (c == 1)
		return (0);
	while (i != (c / 2) - 1 && curr)
	{
		store_f[i] = curr->n;
		curr = curr->next;
		i++;
	}
	store_f[i] = curr->n;
	if (c % 2 == 0)
		curr = curr->next;
	else
		curr = curr->next->next;

	while (curr->next)
	{
		store_l[u] = curr->n;
		curr = curr->next;
		u++;
	}
	store_l[u] = curr->n;
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
