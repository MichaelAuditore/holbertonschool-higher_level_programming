#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check if a linked list has a infinite loop
 * @head: Reference to the first node of list
 * Return: 0 if list has no cycle or 1 if has a cycle
 */
int check_cycle(listint_t *head)
{
	listint_t *tmp = head;
	int firstValue = head->n;
	int i = 0;

	if (head == NULL)
		return (0);
	while (tmp != NULL)
	{
		if (tmp->n == firstValue)
			i++;
		if (tmp->n == firstValue && i > 1)
			break;
		tmp = tmp->next;
	}
	if (i > 1)
		return (1);
	return (0);
}
