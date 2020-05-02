#include <stdio.h>
#include <Python.h>
#include <math.h>
#define M_PI 3.14159265358979323846
// Module method definitions
static PyObject* subtraction(PyObject *self, PyObject *args) {
  double x;
  double x1;
  double y;
  double y1;
  if (!PyArg_ParseTuple(args, "dddd", &x, &x1,&y,&y1)) {
      return NULL;
  }
  printf("%lf real \n %lf im\n",x-y,x1-y1 );
    Py_RETURN_NONE;
}

static PyObject* sum(PyObject *self, PyObject *args) {
  double x;
  double x1;
  double y;
  double y1;
  if (!PyArg_ParseTuple(args, "dddd", &x, &x1,&y,&y1)) {
      return NULL;
  }
  printf("%lf real \n %lf im\n",x+y,x1+y1 );
    Py_RETURN_NONE;
}

static PyObject* mult(PyObject *self, PyObject *args) {
  double x;
  double x1;
  double y;
  double y1;
  if (!PyArg_ParseTuple(args, "dddd", &x, &x1,&y,&y1)) {
      return NULL;
  }
  printf("%lf real \n %lf im\n",x*y-x1*y1,x*y1+x1*y );
    Py_RETURN_NONE;
}

static PyObject* division(PyObject *self, PyObject *args) {
  double x;
  double x1;
  double y;
  double y1;
  if (!PyArg_ParseTuple(args, "dddd", &x, &x1,&y,&y1)) {
      return NULL;
  }
  printf("%lf real \n %lf im\n",(x*y+x1*y1)/(y*y+y1*y1),(x1*y-x*y1)/(y*y+y1*y1));
    Py_RETURN_NONE;
}
static PyObject* pow_complex(PyObject *self, PyObject *args) {
  double x;
  double y;
  double n;
  double alfa;
  double r;
  if (!PyArg_ParseTuple(args, "ddd", &x, &y,&n)) {
      return NULL;
  }
  r = sqrt(x*x+y*y);
  if(x < 0 && y<0){
        alfa = atan(y/x)-M_PI;
  }
  if(x<0 && y>=0){
        alfa = atan(y/x)+M_PI;
  }
  if(x>=0){
        alfa = atan(y/x);
  }
  printf("%lf real \n %lf im\n",r*cos(n*alfa),r*sin(n*alfa));
    Py_RETURN_NONE;
}


// Method definition object for this extension, these argumens mean:
// ml_name: The name of the method
// ml_meth: Function pointer to the method implementation
// ml_flags: Flags indicating special features of this method, such as
//          accepting arguments, accepting keyword arguments, being a
//          class method, or being a static method of a class.
// ml_doc:  Contents of this method's docstring
static PyMethodDef hello_methods[] = {
    {
        "subtraction", subtraction, METH_VARARGS,
        "Print 'hello world' from a method defined in a C extension."
    },
    {
        "sum", sum, METH_VARARGS,
        "Print 'hello xxx' from a method defined in a C extension."
    },
    {
        "mult", mult, METH_VARARGS,
        "Print 'hello xxx' from a method defined in a C extension."
    },
    {
        "division", division, METH_VARARGS,
        "Print 'hello xxx' from a method defined in a C extension."
    },
    {
        "pow_complex", pow_complex, METH_VARARGS,
        "Print 'hello xxx' from a method defined in a C extension."
    },
    {NULL, NULL, 0, NULL}
};

// Module definition
// The arguments of this structure tell Python what to call your extension,
// what it's methods are and where to look for it's method definitions
static struct PyModuleDef hello_definition = {
    PyModuleDef_HEAD_INIT,
    "hello",
    "A Python module that prints 'hello world' from C code.",
    -1,
    hello_methods
};

// Module initialization
// Python calls this function when importing your extension. It is important
// that this function is named PyInit_[[your_module_name]] exactly, and matches
// the name keyword argument in setup.py's setup() call.
PyMODINIT_FUNC PyInit_hello(void) {
    Py_Initialize();
    return PyModule_Create(&hello_definition);
}
