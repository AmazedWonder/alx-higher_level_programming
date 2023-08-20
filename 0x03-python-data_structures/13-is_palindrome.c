#include "lists.h"

/**
 * reverse_listint - function is used to reverses a linked list
 * @head: pointer to first node in list
 *
 * Return: pointer to the first node in the new list
 */
void reverse_listint(listint_t **head)
{
	/* Declare pointers for previous, current, and next nodes */
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	/* Reverse the linked list */
	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	/* Update the head pointer to the new head of the reversed list */
	*head = prev;
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
	/* Declare pointers for slow, fast, temporary, and duplicated nodes */
	listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;

	/* Check for base cases */
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	/* Find the middle of the linked list */
	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dup = slow->next;
			break;
		}
		if (!fast->next)
		{
			dup = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	/* Reverse the second half of the linked list */
	reverse_listint(&dup);

	/* Compare original list and reversed list node by node */
	while (dup && temp)
	{
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	/* If the loop completes without differences, it is a palindrome */
	if (!dup)
		return (1);

	return (0);
}
