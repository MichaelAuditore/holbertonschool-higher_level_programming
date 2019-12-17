#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome - catch if a linked list is palindrome or not
 * @head: Pointer to the first node
 * Return: 1 is palindrome or 0 is not
 */
int is_palindrome(listint_t **head)
{
	listint_t *header;
	listint_t *tail;
	int length = 0;
	int pos[1024], npos = 0, j;

	if (*head == NULL)
		return (1);
	if (head == NULL)
		return (0);
	header = *head;
	tail = *head;
	while (header->next != NULL)
	{
		header = header->next;
		length++;
	}
	for (npos = 0; npos <= length; npos++, tail = tail->next)
		pos[npos] = tail->n;
	for (j = 0; j < length; j++, length--)
	{
		if (pos[j] != pos[length])
			return (0);
	}
	return (1);
}
