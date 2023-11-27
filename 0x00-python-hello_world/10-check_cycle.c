#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
int check_cycle(listint_t *list)
{

	listint_t *p, *x;
	p = list;
	x = list;
	
	while(x->next != NULL && x != NULL)
	{
		p = p->next;
		x = x->next->next;
		if (x == p)
		{
			return (1);
		}
	}
	return(0);
}
