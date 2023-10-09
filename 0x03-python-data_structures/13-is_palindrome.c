#include "lists.h"

/**
 * is_palindrom - A function in C that checks if a singly linked
 * list is a palindrome
 * head: Double pointer
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *old = NULL;
	listint_t *temp;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;

		temp = slow->next;
		slow->next = old;
		old = slow;
		slow = temp;
	}
	if (fast != NULL)
		slow = slow->next;
	while (slow != NULL)
	{
		if (slow->n != old->n)
		{
			return (0);
		}
		slow = slow->next;
		old = old->next;
	}
	return (1);
}
