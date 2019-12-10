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
	int number2;

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
		number2 = current->n;
		if (number2 <= number && current->next->n > number)
			break;
		current = current->next;
	}
	if (number2 <= number)
		new->next = current->next;
	else
		new->next = NULL;
	current->next = new;
	return (current);
}
