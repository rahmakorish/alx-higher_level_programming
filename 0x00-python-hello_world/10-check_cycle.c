#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
int check_cycle(listint_t *list)
{

	listint_t *p;
	p = list;
	while(p->next)
	{
	if(p->next != NULL)
	{
	printf("inside has cycle\n");
	p = p->next;
	}
	if(p->next == NULL)
	{
		printf("no cycle");
		break;
		return (1);

	}
	}

	return(0);
}
