#include <python/Python.h>
#include <stdio.h>
#include <stdint.h>

static char module_docstring[] =
        "This module provides swap in 4 and swap in 2 functions";

static char endianSwap32_docstring[] =
        "Flip bytes in a 32 bit integers";

static char endianSwap16_docstring[] =
        "Flip bytes in a 16 bit integers";


static PyObject* endianSwap16(PyObject* self, PyObject* args)
{
    short a;
    if (!PyArg_ParseTuple(args, "i", &a)) {
        return NULL;
    } else {
        short b = (int16_t) ((a << 8) | (a >> 8));
        return Py_BuildValue("i", b);
    }
}

static PyObject* endianSwap32(PyObject* self, PyObject* args)
{
    int a;
    if (!PyArg_ParseTuple(args, "i", &a)) {
        return NULL;
    } else {
        int b = (int32_t) (((a << 24) & 0xff000000) |
                                       ((a << 8) & 0x00ff0000) |
                                       ((a >> 8) & 0x0000ff00) |
                                       ((a >> 24) & 0x000000ff));
        return Py_BuildValue("i", b);
    }
}

/* describe a module containing the interfaces,
 * function pointer and a  doc string, some explaination
 * about the function (document)
 * */
static PyMethodDef module_methods[] = {
    {"endianSwap16", endianSwap16, METH_VARARGS, endianSwap16_docstring},
    {"endianSwap32", endianSwap32, METH_VARARGS, endianSwap32_docstring}
    };



PyMODINIT_FUNC initlibsimplemodule(void)
{
    (void) Py_InitModule("libsimplemodule", module_methods);
}


int main(int argc, char** argv)
{
    Py_SetProgramName(argv[0]);
    Py_Initialize();
    initlibsimplemodule();
    return 0;
}
