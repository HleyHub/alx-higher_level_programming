#include <Python.h>
/**
 * print_python_list_info - A C function that prints some basic
 * info about Python lists
 * @p: A PyObject list
 */
void print_python_list_info(PyObject *p)
{
	size_t size;
	PyObject *object;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %zu\n", size);
	printf("[*] Allocated = %zu\n", ((PyListObject *)p)->allocated);
	while (a < size)
	{
		object = PyList_GET_ITEM(p, a);
		printf("Element %zu: %s\n", a, Py_TYPE(objet)->tp_name);
		a++;
	}
}
