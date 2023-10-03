#include "lists.h"
/**
 * insert_node - A function in C that inserts a number into a
 * sorted singly linked list
 * @head: A head node
 * @number: A number
 * Return: Address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *old, *new, *latest;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	latest = *head;
	old = NULL;

	while (latest != NULL && latest->n < number)
	{
		old = latest;
		latest = latest->next;
	}
	old->next = new;
	new->next = latest;

	return (new);
}
