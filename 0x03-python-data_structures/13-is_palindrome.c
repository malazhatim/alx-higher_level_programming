#include "lists.h"

/**
 * is_palindrome - function that check for palindrom
 * @head:list
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	const listint_t *cur;
	int l;
	int a, b;
	int arr[10000];

	if (*head == NULL)
		return (1);
	current = *head;
	l = 0;
	while (cur != NULL)
	{
		cur = cur->next;
		l++;
	}
	if (l == 1)
		return (1);

	cur = *head;
	a = 0;
	while (cur != NULL)
	{
		arr[a] = current->n;
		a++;
		cur = cur->next;
	}
	b = 0;
	a--;
	l--;
	while (a >= (l / 2))
	{
		if (arr[a] != arr[b])
			return (0);
		a--;
		b++;
	}
	return (1);
}
