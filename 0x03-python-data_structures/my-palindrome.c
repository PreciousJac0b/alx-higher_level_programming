#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - linked list palindrome
 *
 * @head: pointer to head of linkedlist
 *
 * Return: 1 on success, 0 on fail
 */

int is_palindrome(listint_t **head)
{
	listint_t *new, *move;
	int *p;
	unsigned int i = 0, j = 0, k = 0, l = 0;

	new = *head;
	move = *head;

	while (new)
	{
		new = new->next;
		i++;
	}
	p = malloc(sizeof(int) * i);
	if (p == NULL)
		return (0);

	while (move)
	{
		*(p + j) = move->n;
		move =  move->next;
		j++;
	}

	l = i - 1;

	while (k < l)
	{
		if (*(p + k) != *(p + l))
		{
			free(p);
			return (0);
		}
		k++;
		l--;
	}

	free(p);
	return (1);
}
