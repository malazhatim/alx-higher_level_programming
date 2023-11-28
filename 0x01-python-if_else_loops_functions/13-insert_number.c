#include "lists.h"
/**
 * insert_node - insert into list
 * @head: head of list
 * @number:number to insert
 * Return: adresse of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *a, *t;

	a = malloc(sizeof(listint_t));
	if (a == NULL)
		return (NULL);
	t = *head;
	if (*head == NULL)
	{
		a = add_nodeint_end(head, number);
		return (a);
	}
	if (t->n > number)
	{
		a->next = t;
		a->n = number;
		*head = a;
		return (a);
	}
	while (t->next)
	{
		if (number < t->next->n)
		{
			a->next = t->next;
			t->next = a;
			a->n = number;
			return (a);
		}
		t = t->next;
	}
	a = add_nodeint_end(head, number);
	return (a);
}
