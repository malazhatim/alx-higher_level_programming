#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes information
 * @p: Python Object
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int s, a, lim;

	setbuf(stdout, NULL);

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		setbuf(stdout, NULL);
		return;
	}

	s = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", s);
	printf("  trying string: %s\n", str);

	if (s >= 10)
		lim = 10;
	else
		lim = s + 1;

	printf("  first %ld bytes:", lim);

	for (a = 0; a < lim; a++)
		if (str[a] >= 0)
			printf(" %02x", str[a]);
		else
			printf(" %02x", 256 + str[a]);

	printf("\n");
	setbuf(stdout, NULL);
}

/**
 * print_python_float - Prints float information
 * @p: Python Object
 * Return: no return
 */
void print_python_float(PyObject *p)
{
	double v;
	char *n;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		setbuf(stdout, NULL);
		return;
	}

	v = ((PyFloatObject *)(p))->ob_fval;
	n = PyOS_double_to_string(v, 'r', 0, Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);

	printf("  value: %s\n", n);
	setbuf(stdout, NULL);
}

/**
 * print_python_list - Prints list information
 * @p: Python Object
 * Return: no return
 */
void print_python_list(PyObject *p)
{
	long int s, a;
	PyListObject *l;
	PyObject *o;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		setbuf(stdout, NULL);
		return;
	}

	s = ((PyVarObject *)(p))->ob_size;
	l = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", s);
	printf("[*] Allocated = %ld\n", l->allocated);

	for (a = 0; a < s; a++)
	{
		o = l->ob_item[i];
		printf("Element %ld: %s\n", a, ((o)->ob_type)->tp_name);

		if (PyBytes_Check(o))
			print_python_bytes(o);
		if (PyFloat_Check(o))
			print_python_float(o);
	}
	setbuf(stdout, NULL);
}
