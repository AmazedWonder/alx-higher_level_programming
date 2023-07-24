#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

/**
 * print_python_bytes - function prints information about a Python bytes object
 * @p: pointer to the Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	/* declare variables */
	long int size;
	int i;
	char *str_bytes_data = NULL;

	/* print header */
	printf("[.] bytes object info\n");

	/* check if input is a bytes object */
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	/* extract the bytes data and its size */
	PyBytes_AsStringAndSize(p, &str_bytes_data, &size);

	/* print size and bytes data */
	printf("  size: %li\n", size);
	printf("  trying string: %s\n", str_bytes_data);

	/* print the first 10 bytes as hexadecimal values */
	if (size < 10)
		printf("  first %li bytes:", size + 1);
	else
		printf("  first 10 bytes:");
	for (i = 0; i <= size && i < 10; i++)
		printf(" %02hhx", str_bytes_data[i]);
	printf("\n");
}

/**
 * print_python_list - function prints information about a Python list object
 * @p: pointer to the Python list object
 */
void print_python_list(PyObject *p)
{
	/* declare variables */
	long int size = PyList_Size(p);
	int i;
	PyListObject *list = (PyListObject *)p;
	const char *type;

	/* print header */
	printf("[*] Python list info\n");

	/* print size and memory allocation */
	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", list->allocated);

	/* print information about each element in the list */
	for (i = 0; i < size; i++)
	{
		type = (list->ob_item[i])->ob_type->tp_name;
		printf("Element %i: %s\n", i, type);
		if (!strcmp(type, "bytes"))
			print_python_bytes(list->ob_item[i]);
	}
}
