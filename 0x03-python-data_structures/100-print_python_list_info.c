#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Print info about python lists
 * @p: Python object
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *py_list;
	PyObject *py_item;
	long int py_size;
	long int i = 0;

	py_size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", py_size);
	py_list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", py_list->allocated);

	while (i < py_size)
	{
		py_item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
