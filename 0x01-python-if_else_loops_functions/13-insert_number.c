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
	listint_t *node;
	listint_t *h;
	listint_t *h_prv;

	h = *head;
	node = malloc(sizeof(listint_t));

	if (node == NULL)
		return (NULL);

	while (h != NULL)
	{
		if (h->n > number)
			break;
		h_prv = h;
		h = h->next;
	}

	node->n = number;

	if (*head == NULL)
	{
		node->next = NULL;
		*head = node;
	}
	else
	{
		node->next = h;
		if (h == *head)
			*head = node;
		else
			h_prv->next = node;
	}

	return (node);
}
