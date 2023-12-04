#include <Python.h>
/**
 *print_python_list_info-prints info about python lists
 *@p:python object
  **/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t listSize = PyList_Size(p);
	return (listSize);
}
