#include <Python.h>
#include <object.h>
#include <unicodeobject.h>

/**
 * print_python_string - A function that prints Python strings
 * @p: arguments
 */
void print_python_string(PyObject *p)
{
	const char *type = NULL;
	Py_ssize_t lgth = 0;
	wchar_t *stg = NULL;

	printf("[.] string object info\n");
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	if (PyUnicode_IS_COMPACT_ASCII(p))
		type = "compact ascii";
	else
		type = "compact unicode object";

	stg = PyUnicode_AsWideCharString(p, &lgth);

	printf("  type: %s\n", type);
	printf("  length: %ld\n", lgth);
	printf("  value: %ls\n", stg);
}
