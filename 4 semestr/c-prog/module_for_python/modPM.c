#include <stdio.h>
#include <Python.h>
#include <math.h>
static PyObject* subtraction(PyObject *self, PyObject *args) {
  double x;
  double x1;
  double y;
  double y1;
  if (!PyArg_ParseTuple(args, "dddd", &x, &x1,&y,&y1)) {
      return NULL;
  }
    return Py_BuildValue("dd",x-y,x1-y1 );
}

static PyObject* sum(PyObject *self, PyObject *args) {
  double x;
  double x1;
  double y;
  double y1;
  if (!PyArg_ParseTuple(args, "dddd", &x, &x1,&y,&y1)) {
      return NULL;
  }
    return Py_BuildValue("dd",x+y,x1+y1 );
}

static PyObject* mult(PyObject *self, PyObject *args) {
  double x;
  double x1;
  double y;
  double y1;
  if (!PyArg_ParseTuple(args, "dddd", &x, &x1,&y,&y1)) {
      return NULL;
  }
    return Py_BuildValue("dd",x*y-x1*y1,x*y1+x1*y );
}

static PyObject* division(PyObject *self, PyObject *args) {
  double x;
  double x1;
  double y;
  double y1;
  if (!PyArg_ParseTuple(args, "dddd", &x, &x1,&y,&y1)) {
      return NULL;
  }
    return Py_BuildValue("dd",(x*y+x1*y1)/(y*y+y1*y1),(x1*y-x*y1)/(y*y+y1*y1));
}

static PyObject* vectors2d_sum(PyObject *self, PyObject *args) {
  double x1, x2;
  double y1, y2;
  if (!PyArg_ParseTuple(args, "dddd", &x1, &x2, &y1, &y2)) {
      return NULL;
  }
    return Py_BuildValue("dd", x1 + y1, x2 + y2);
}

static PyObject* vectors2d_sub(PyObject *self, PyObject *args) {
  double x1, x2;
  double y1, y2;
  if (!PyArg_ParseTuple(args, "dddd", &x1, &x2, &y1, &y2)) {
      return NULL;
  }
    return Py_BuildValue("dd", x1 - y1, x2 - y2);
}

static PyObject* vectors2d_scalar_prod(PyObject *self, PyObject *args) {
  double x1, x2;
  double y1, y2;
  if (!PyArg_ParseTuple(args, "dddd", &x1, &x2, &y1, &y2)) {
      return NULL;
  }
    return Py_BuildValue("d", x1*y1 + x2*y2);
}

static PyObject* vectors3d_sum(PyObject *self, PyObject *args) {
  double x1, x2, x3;
  double y1, y2, y3;
  if (!PyArg_ParseTuple(args, "dddddd", &x1, &x2, &x3, &y1, &y2, &y3)) {
      return NULL;
  }
    return Py_BuildValue("ddd", x1 + y1, x2 + y2, x3 + y3);
}

static PyObject* vectors3d_sub(PyObject *self, PyObject *args) {
  double x1, x2, x3;
  double y1, y2, y3;
  if (!PyArg_ParseTuple(args, "dddddd", &x1, &x2, &x3, &y1, &y2, &y3)) {
      return NULL;
  }
    return Py_BuildValue("ddd", x1 - y1, x2 - y2, x3 - y3);
}

static PyObject* vectors3d_scalar_prod(PyObject *self, PyObject *args) {
  double x1, x2, x3;
  double y1, y2, y3;
  if (!PyArg_ParseTuple(args, "dddddd", &x1, &x2, &x3, &y1, &y2, &y3)) {
      return NULL;
  }
    return Py_BuildValue("d", x1*y1 + x2*y2 + x3*y3);
}

static PyObject *intersection(PyObject *self, PyObject *args) {
    PyObject *pylist1, *pylist2;
    double  double_item1, double_item2, len1, len2;
    double result = 0;
    double* list1;
    double* list2;
    double* inter;
    int i,i1,i3;
    int i2 = 0;
    int check = 1;

    if (!PyArg_ParseTuple(args,"OO",&pylist1, &pylist2)) {
        return NULL;
    }

    len1 = PySequence_Fast_GET_SIZE(pylist1);
    len2 = PySequence_Fast_GET_SIZE(pylist2);

    list1 = (double*)malloc(len1 * sizeof(double));
    list2 = (double*)malloc(len2 * sizeof(double));// тут юзаем динамическую память, потому что дефолтная не катит
    if(len1<len2){
      inter = (double*)malloc(len1 * sizeof(double));
    }else{
      inter = (double*)malloc(len2 * sizeof(double));
    }
    for(i=0; i<len1; i++) {
        PyObject *item1 = PySequence_Fast_GET_ITEM(pylist1,i);
        double_item1 = PyFloat_AsDouble(item1);
        list1[i] = double_item1;
    }
    for(i=0; i<len2; i++) {
        PyObject *item2 = PySequence_Fast_GET_ITEM(pylist2,i);
        double_item2 = PyFloat_AsDouble(item2);
        list2[i] = double_item2;
    }
    for(i = 0; i<len1;i++){
      for(i1 = 0; i1<len2;i1++){
        if(list1[i] == list2[i1]){
            for(i3 = 0; i3<i2; i3++){
              if(inter[i3] == list2[i1]){
                check = 0;
                break;
              }
            }
            if(check==0){
            }else{
            inter[i2] = list1[i];
            i2++;
          }
          check = 1;
      }
    }
  }

    PyObject *tup = PyTuple_New(i2);
    for(i = 0; i<i2;i++){
      PyTuple_SET_ITEM(tup, i, PyLong_FromDouble(inter[i]));
    }

    return Py_BuildValue("O", tup);
}
static PyMethodDef modPM_methods[] = {
    {
        "subtraction", subtraction, METH_VARARGS,
        "Subtraction of two complex numbers\nthe first two arguments of the function are the real and imaginary parts of the first number, the second two are the real and imaginary parts of the second number"
    },
    {
        "sum", sum, METH_VARARGS,
        "Sum of two complex numbers\nthe first two arguments of the function are the real and imaginary parts of the first number, the second two are the real and imaginary parts of the second number"
    },
    {
        "mult", mult, METH_VARARGS,
        "Multiplication of two complex numbers\nthe first two arguments of the function are the real and imaginary parts of the first number, the second two are the real and imaginary parts of the second number"
    },
    {
        "division", division, METH_VARARGS,
        "Division of two complex numbers\nthe first two arguments of the function are the real and imaginary parts of the first number, the second two are the real and imaginary parts of the second number"
    },

    {
        "intersection", intersection, METH_VARARGS,
        "Intersection of two lists"
    },
    {
        "vectors2d_sum", vectors2d_sum, METH_VARARGS,
        "Subtraction of 2-dimension vectors."
    },
    {
        "vectors2d_sub", vectors2d_sub, METH_VARARGS,
        "Sum of 2-dimension vectors."
    },
    {
        "vectors2d_scalar_prod", vectors2d_scalar_prod, METH_VARARGS,
        "Scalar product of 2-dimension vectors."
    },
    {
        "vectors3d_sum", vectors3d_sum, METH_VARARGS,
        "Sum of 3-dimension vectors."
    },
    {
        "vectors3d_sub", vectors3d_sub, METH_VARARGS,
        "Subtraction of 3-dimension vectors."
    },
    {
        "vectors3d_scalar_prod", vectors3d_scalar_prod, METH_VARARGS,
        "Scalar product of 3-dimension vectors."
    },
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef modPM_definition = {
    PyModuleDef_HEAD_INIT,
    "modPM",
    "Module for count complex numbers and vectors.",
    -1,
    modPM_methods
};

PyMODINIT_FUNC PyInit_modPM(void) {
    Py_Initialize();
    return PyModule_Create(&modPM_definition);
}