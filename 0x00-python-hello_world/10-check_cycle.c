#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - function that checks if a singly linked list has a cycle in it
 * @list: pointer to the head node
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *old, *new;

	old= new = list;
	while (old && new && new->next)
	{
		old = old->next;
		new = new->next->next;
		if (old == new)
			return (1);
	}
	return (0);
}
