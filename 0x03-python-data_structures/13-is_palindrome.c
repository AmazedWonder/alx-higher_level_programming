#include "lists.h"

/**
 * reverse_listint - function is used to reverses a linked list
 * @head: pointer to first node in list
 *
 * Return: pointer to the first node in the new list
 */
void reverse_listint(listint_t **head)
{
	listint_t *previous = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		previous = current;
		current = next;
		next = current->next;
		current->next = previous;
	}

	*head = previous;
}

/**
 * is_palindrome -function checks if singl linked list is
 * a palindrome or not
 * @head: double pointer to the linked list
 *
 * Return: 1 if a palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptrslow = *head, *ptrfast = *head, *traverse = *head, *rev = NULL;

	/*checks if the input list is empty or contains only one element*/
	/* to be considered palindrome*/
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	/* If the list has at least two elements*/
	/*use two pointers slow and fast to find the middle of the list*/
	while (1)
	{
		ptrfast = ptrfast->next->next;
		if (!ptrfast)
		{
			rev = ptrslow->next;
			break;
		}
		if (!ptrfast->next)
		{
			rev = ptrslow->next->next;
			break;
		}
		ptrslow = ptrslow->next;
	}

	reverse_listint(&rev);

	while (traverse && rev)
	{
		if (traverse->n == rev->n)
			rev = rev->next;
			traverse = traverse->next;
		else
			return (0);
	}

	if (!rev)
		return (1);

	return (0);
}
