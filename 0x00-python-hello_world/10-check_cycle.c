#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
/**
 *check_cycle-checks if linked list has cycle
 *@list:linked list checked
 *Return:0if no cycle 1 if cycle present
 **/
int check_cycle(listint_t *list)
{
	listint_t *p, *x;

	p = list;
	x = list;
	while (x && x->next)
	{
		p = p->next;
		x = x->next->next;
		if (x == p)
		{
			return (1);
		}
	}
	return (0);
}
