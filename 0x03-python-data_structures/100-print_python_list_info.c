#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
/**
 * print_python_list_info - this function prints information about a python
 * object list
 * @pObject: Reference to the Python object
 */
void print_python_list_info(PyObject *pObject)
{
	unsigned int i;
	unsigned int length = Py_SIZE(pObject);
	PyObject *element;

	if (PyList_Check(pObject))
	{
		printf("[*] Size of the Python List = %ld\n", Py_SIZE(pObject));
		printf("[*] Allocated = %ld\n", ((PyListObject *)pObject)->allocated);
		for (i = 0; i < length; i++)
		{
			element = PyList_GetItem(pObject, i);
			printf("Element %d: %s\n", i, Py_TYPE(element)->tp_name);
		}
	}
}
