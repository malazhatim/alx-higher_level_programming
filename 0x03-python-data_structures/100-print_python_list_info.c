#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int s = PyList_Size(p);
	int a;
	PyListObject *o = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", s);
	printf("[*] Allocated = %li\n", o->allocated);
	for (a = 0; a < s; a++)
		printf("Element %i: %s\n", a, Py_TYPE(o->ob_item[a])->tp_name);
}
