#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome - catch if a linked list is palindrome or not
 * @head: Pointer to the first node
 * Return: 1 is palindrome or 0 is not
 */
int is_palindrome(listint_t **head)
{
	int length = 0, elements[9999], j;
	listint_t *header = NULL;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	header = *head;
	for (; header; length++, header = header->next)
		elements[length] = header->n;
	for (j = 0; j < length; j++, length--)
	{
		if (elements[j] != elements[length - 1])
			return (0);
	}
	return (1);
}
