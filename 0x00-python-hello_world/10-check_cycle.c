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
		return (0);
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

	if (check->next == NULL)
	{
		return (0);
	}

	return (1);
}
