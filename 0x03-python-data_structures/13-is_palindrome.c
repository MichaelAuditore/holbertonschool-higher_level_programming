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
	listint_t *prevtail;
	listint_t *tail;
	int length = 0;
	int pos;

	if (*head == NULL)
		return (1);
	if (head == NULL)
		return (0);
	header = *head;
	tail = *head;
	while (tail->next != NULL)
	{
		tail = tail->next;
		length++;
	}
	while (header != NULL)
	{
		if (header->n == tail->n && length == 0)
			return (1);
		if (header->n == tail->n)
		{
			header = header->next;
			prevtail = *head;
			pos = 1;
			while (pos < length)
			{
				prevtail = prevtail->next;
				pos++;
			}
			length--;
			tail = prevtail;
		}
		else
			break;
	}
	return (0);
}
