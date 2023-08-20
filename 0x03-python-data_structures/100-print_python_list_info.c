#include <Python.h>

/**
 * print_python_list_info - function prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyObject *obj;

	/* Get the size and allocation of the list */
	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	/* Iterate over the list and print information about each element */
	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		/* Get the i-th element of the list */
		obj = PyList_GetItem(p, i);

		/* Print the type name of the element */
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
