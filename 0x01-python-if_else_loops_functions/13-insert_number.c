#include "lists.h"
#include <stdio.h>
#include <stddef.h>

/**
 * insert_node - insert node at last small nnumber in the node
 *
 * @head: head of node
 * @number: number
 *
 * Return: return the node
 */
listint_t *insert_node(listint_t **head, int number)
{
	int i = 0;
	listint_t *behind = *head;
	listint_t *after = *head;
	listint_t *cur = NULL;
	listint_t *h = *head;

	cur = malloc(sizeof(listint_t));

	if (!cur || !*head)
	{
		return (NULL);
	}
	while (h)
	{
		if (h->n > number)
		{
			break;
		}
		i++;
		h = h->next;
	}

	while (i > 0)
	{
		after = after->next;
		if (i - 1 == 0)
		{
			break;
		}
		behind = behind->next;
		i--;
	}

	cur->n = number;
	behind->next = cur;
	cur->next = after;

	return (*head);
}
