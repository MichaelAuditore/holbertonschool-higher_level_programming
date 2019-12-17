#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome - catch if a linked list is palindrome or not
 * @head: Pointer to the first node
 * Return: 1 is palindrome or 0 is not
 */
int is_palindrome(listint_t **head)
{
	int count = 0, nel[9999], j;
	listint_t *header = NULL;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	for (; header; count++, header = header->next)
		nel[count] = header->n;
	for (j = 0; j < count; j++, count--)
	{
		if (nel[j] != nel[count - 1])
			return (0);
	}
	return (1);
}
