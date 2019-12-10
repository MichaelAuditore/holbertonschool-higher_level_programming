#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * insert_node - insert node in a sorted linked list
 * @head: reference to the first node of list
 * @number: Number to add
 * Return: Pointer with the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;

	if (number < current->n)
	{
		new->next = *head;
		*head = new;
		return (*head);
	}
	while (current->next != NULL)
	{
		if (current->n < number && current->next->n >= number)
			break;
		current = current->next;
	}
	if (current->next == NULL)
		new->next = NULL;
	else
		new->next = current->next;
	current->next = new;
	return (current);
}
