#include "lists.h"

/**
 * check_cycle - function checks a cycle in singly linked list
 * @list: pointer to the beginning of the linked list  node
 * Return: 0 if there is no cycle or 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *start_list, *check_next;

	start_list = list;

	if (start_list == NULL || start_list->next == NULL)
		return (0);
	/*start_list = list;*/
	check_next = start_list->next;

	while (start_list != NULL && check_next->next != NULL
			&& check_next->next->next != NULL)
	{
		if (start_list == check_next)
			return (1);
		start_list = start_list->next;
		check_next = check_next->next->next;
	}
	return (0);
}
