#include <Python.h>

/**
 * print_python_list - A C function that prints Python lists
 * @p: A PyObject list
 */
void print_python_list(PyObject *p)
{
	int i, size;

	if (PyList_Check(p))
	{
		size = (int)PyList_Size(p);
		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %d\n", size);
		printf("[*] Allocated = %d\n",
				(int)((PyListObject *)p)->allocated);
		for (i = 0; i < size; i++)
		{
			printf("Element %d: %s\n", i,Py_TYPE(PyList_GetItem(p, i))->tp_name);
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}

/**
 * print_python_bytes - A C function that prints Python bytes
 * @p: A PyObject list
 */
void print_python_bytes(PyObject *p)
{
	int i, size;

	if (PyBytes_Check(p))
	{
		size = (int)PyBytes_Size(p);
		printf("[.] bytes object info\n");
		printf("  size: %d\n", size);
		printf("  trying string: %s\n", PyBytes_AsString(p));
		printf("  first %d bytes: ", (size < 10) ? size : 10);
		for (i = 0; i < size && i < 10; i++)
		{
			printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);
		}
		printf("\n");
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}
