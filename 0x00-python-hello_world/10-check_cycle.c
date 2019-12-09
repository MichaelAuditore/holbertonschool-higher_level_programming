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
	listint_t *tmp;

	if (head == NULL)
		return (0);

	while (head != NULL)
	{
	        tmp = head;
		head = head->next;
	        if(tmp <= head)
			return (1);
	}
	return (0);
}
