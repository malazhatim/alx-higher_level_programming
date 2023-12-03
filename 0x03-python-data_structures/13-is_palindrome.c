#include "lists.h"
/**
 * is_palindrome - checks for list is palindrome
 * @head: head of linked list
 * Return:  boolean
 */
int is_palindrome(listint_t **head)
{
	int l = 0, a= 0;
	listint_t *t;
	int N[10000];

	t = *head;
	if ((*head) == NULL)
		return (1);
	while (t != NULL)
	{
		l++;
		t = t->next;
	}
	if (l == 1)
		return (1);
	t = *head;
	while (t != NULL)
	{
		N[a] = t->n;
		t = t->next;
		a++;
	}
	for (a = 0; a <= l / 2; a++)
	{
		if (N[a] != N[l - a - 1])
		{
			return (0);
		}
	}
	return (1);
}
