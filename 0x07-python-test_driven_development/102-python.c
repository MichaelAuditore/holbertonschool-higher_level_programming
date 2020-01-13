#include <stdio.h>
#include <string.h>
#include <Python.h>

/**
 * print_python_string - prints Python strings info.
 *
 * @p: Python String Unicode Object or ASCII string object
 * Return: no return
 */
void print_python_string(PyObject *p)
{

        PyObject *obj, *visual;

        (void)visual;
        printf("[.] string object info\n");

        if (strcmp(p->ob_type->tp_name, "str"))
        {
                printf("  [ERROR] Invalid String Object\n");
                return;
        }

        if (PyUnicode_IS_COMPACT_ASCII(p))
                printf("  type: compact ascii\n");
        else
                printf("  type: compact unicode object\n");

        visual = PyObject_Repr(p);
        obj = PyUnicode_AsEncodedString(p, "utf-8", "~E~");
        printf("  length: %ld\n", PyUnicode_GET_SIZE(p));
        printf("  value: %s\n", PyBytes_AsString(obj));
}


