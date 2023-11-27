#include "lists.h"
/**
 * check_cycle - checks for cycles in loop
 * @list: list to take in
 * Return: integer value
 */
int check_cycle(listint_t *list)
{
	listint_t *a = list;
	listint_t *b = list;

	if (!list)
	{
		return (0);
	}

	while (a != NULL && b != NULL)
	{
		a = a->next;
		if (b->next)
			b = b->next->next;

		if (a == b)
			return (1);
	}
	return (0);
}
