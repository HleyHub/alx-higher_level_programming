#include <Python.h>
#include <listobject.h>
#include <object.h>
#include <bytesobject.h>

/**
 * print_python_bytes - A C function that prints Python lists
 * @p: A PyObject list
 */
void print_python_bytes(PyObject *p)
{
	long int bytes_size, idx;

	printf("[.] bytes object info\n");
	if (PyBytes_CheckExact(p))
	{
		bytes_size = PyBytes_Size(p);
		printf("  size: %ld\n", bytes_size);
		printf("  trying string: %s\n", PyBytes_AsString(p));
		if (bytes_size >= 10)
			bytes_size = 10;
		else
			bytes_size++;
		printf("  first %ld bytes:", bytes_size);
		for (idx = 0; idx < bytes_size; idx++)
			printf(" %02x", (int) PyBytes_AsString(p)[idx] & 0xff);
		printf("\n");
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}

/**
 * print_python_list - A C function that prints Python bytes
 * @p: A PyObject list
 */
void print_python_list(PyObject *p)
{
	long int size_list = PyList_GET_SIZE(p), index_list;
	PyObject *test;
	PyListObject *object_list = (PyListObject *) p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size_list);
	printf("[*] Allocated = %ld\n", object_list->allocated);

	for (index_list = 0; index_list < size_list; index_list++)
	{
		test = PyList_GET_ITEM(p, index_list);
		printf("Element %ld: %s\n", index_list,
				test->ob_type->tp_name);
		if (PyBytes_CheckExact(test))
			print_python_bytes(test);
	}
}
