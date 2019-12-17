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
	int *pos = NULL, npos = 0, j = 0;

	if (*head == NULL)
		return (1);
	if (head == NULL)
		return (0);
	header = *head;
	for (npos = 0; npos++; header = header->next)
		;
	pos = malloc(sizeof(int) * npos + 1);
	for (npos = 0; npos++; header = header->next)
		pos[npos] = header->n;
	for (j = 0; j < npos; j++, npos--)
	{
		if (pos[j] != pos[npos])
			return (0);
	}
	for (j = 0; j < npos; j++)
		free((pos + j));
	free(pos);
	return (1);
}
