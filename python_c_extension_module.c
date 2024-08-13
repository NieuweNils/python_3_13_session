#include <Python.h>

static PyObject *method_fibonnaci(PyObject *self, PyObject *args) {
    int n = 0;

    /* Parse arguments */
    if (!PyArg_ParseTuple(args, "i", &n)) {
        return NULL;
    }

    // Check for negative input
    if (n < 0) {
        PyErr_SetString(PyExc_ValueError, "input number n must be greater than or equal to 0");
        return NULL;
    }

    int prev1 = 1;
    int prev2 = 0;
    int num;

    /* do the fibonnaci thing */
    for (int i = 0; i <= n; i++) {
        if (i == 0) {
            // for first term
            num = prev2;
        }
        else if (i == 1) {
            // for second term
            num = prev1;
        }
        else {
            // for subsequent terms
            num = prev1 + prev2;
            prev2 = prev1;
            prev1 = num;
        }

    }
    return PyLong_FromLong(num);

};

static PyMethodDef FibonnaciMethods[] = {
        {"fibonnaci", method_fibonnaci, METH_VARARGS, "Python interface for fibonnaci C library function"},
        {NULL,        NULL,             0,            NULL}
};


static struct PyModuleDef c_ext_module = {
        PyModuleDef_HEAD_INIT,
        "c_ext_module",
        "Python interface for the fibonnaci C library function, copy pasted from the internet by Nils",
        -1,
        FibonnaciMethods
};


PyMODINIT_FUNC PyInit_c_ext_module(void) {
    return PyModule_Create(&c_ext_module);
}
