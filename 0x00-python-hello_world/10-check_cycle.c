#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 *
 * @list: head of node
 *
 * Return: 0 in success otherwize 1
 */
int check_cycle(listint_t *list)
{
	listint_t *check = NULL;

	if (list == NULL)
	{
		return (NULL);
	}

	check = list;

	while (check != NULL)
	{
		if (check->next == list)
		{
			return (1);
		}
		check = check->next;
	}
	return (0);
}
