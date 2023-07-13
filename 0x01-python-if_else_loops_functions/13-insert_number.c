#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * insert_node - function used to Insert a number
 * into a sorted singly-linked list
 * @head: A pointer the head of the linked list
 * @number: The number to be inserted
 *
 * Return: NULL, if the function fails
 * Otherwise - a pointer to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_node = *head;
	/* Allocate memory for new node */
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
	{ /* Check if mem allocation was successful */
		return (NULL);
	}

	new_node->n = number; /* Assign value to new node */
	new_node->next = NULL; /* Set next pointer to NULL */
	if (*head == NULL || number < (*head)->n)
	{ /* If list is empty or new node inserted at the beginn */
		/*set the next pointer of the new node to current head of list*/
		new_node->next = *head;
		*head = new_node;/*update the head to point new node*/
		return (new_node);
	}

	/*listint_t *current_node = *head;*/
	/* current node is not NULL, and the value of the n*/
	/*field of the next node is less than the input value*/
	while (current_node->next != NULL && current_node->next->n < number)
	{ /* Traverse list until the correct position is found */
		current_node = current_node->next;
	}
	new_node->next = current_node->next; /* Insert new node */
	/*append it to the end of the list by setting the next*/
	/*pointer of the last node to point to the new node*/
	current_node->next = new_node;
	return (new_node);
}
