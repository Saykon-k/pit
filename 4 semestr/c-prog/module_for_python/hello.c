#include <stdio.h>
#include <Python.h>
#include <math.h>
#define M_PI 3.14159265358979323846
static PyObject* subtraction(PyObject *self, PyObject *args) {
  double x;
  double x1;
  double y;
  double y1;
  if (!PyArg_ParseTuple(args, "dddd", &x, &x1,&y,&y1)) {
      return NULL;
  }
  printf("%lf real \n %lf im\n",x-y,x1-y1 );
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
  printf("%lf real \n %lf im\n",x+y,x1+y1 );
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
  printf("%lf real \n %lf im\n",x*y-x1*y1,x*y1+x1*y );
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
  printf("%lf real \n %lf im\n",(x*y+x1*y1)/(y*y+y1*y1),(x1*y-x*y1)/(y*y+y1*y1));
  return Py_BuildValue("dd",(x*y+x1*y1)/(y*y+y1*y1),(x1*y-x*y1)/(y*y+y1*y1));
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
        alfa = atan(y/x);
  }
  if(x<0 && y>=0){
        alfa = atan(y/x);
  }
  if(x>=0){
        alfa = atan(y/x);
  }
  printf("%lf - x \n %lf - y\n", x , y  );
  printf("%lf  - alfa\n", alfa );
  printf("%lf real \n %lf im\n",r*cos(n*alfa),r*sin(n*alfa));
    Py_RETURN_NONE;
}

static PyObject* vectors2d_sum(PyObject *self, PyObject *args) {
  double x1, x2;
  double y1, y2;
  if (!PyArg_ParseTuple(args, "dddd", &x1, &x2, &y1, &y2)) {
      return NULL;
  }
  printf("%lf \n %lf \n", x1 + y1, x2 + y2);
return Py_BuildValue("dd", x1 + y1, x2 + y2);
}

static PyObject* vectors2d_sub(PyObject *self, PyObject *args) {
  double x1, x2;
  double y1, y2;
  if (!PyArg_ParseTuple(args, "dddd", &x1, &x2, &y1, &y2)) {
      return NULL;
  }
  printf("%lf \n %lf \n", x1 - y1, x2 - y2);
return Py_BuildValue("dd", x1 - y1, x2 - y2);
}

static PyObject* vectors2d_scalar_prod(PyObject *self, PyObject *args) {
  double x1, x2;
  double y1, y2;
  if (!PyArg_ParseTuple(args, "dddd", &x1, &x2, &y1, &y2)) {
      return NULL;
  }
  printf("%lf\n", x1*y1 + x2*y2);
  return Py_BuildValue("d", x1*y1 + x2*y2);
}


static PyObject* vectors3d_sum(PyObject *self, PyObject *args) {
  double x1, x2, x3;
  double y1, y2, y3;
  if (!PyArg_ParseTuple(args, "dddddd", &x1, &x2, &x3, &y1, &y2, &y3)) {
      return NULL;
  }
  printf("%lf \n %lf \n %lf \n", x1 + y1, x2 + y2, x3 + y3);
return Py_BuildValue("ddd", x1 + y1, x2 + y2, x3 + y3);
}

static PyObject* vectors3d_sub(PyObject *self, PyObject *args) {
  double x1, x2, x3;
  double y1, y2, y3;
  if (!PyArg_ParseTuple(args, "dddddd", &x1, &x2, &x3, &y1, &y2, &y3)) {
      return NULL;
  }
  printf("%lf \n %lf \n %lf \n", x1 - y1, x2 - y2, x3 - y3);
return Py_BuildValue("ddd", x1 - y1, x2 - y2, x3 - y3);
}

static PyObject* vectors3d_scalar_prod(PyObject *self, PyObject *args) {
  double x1, x2, x3;
  double y1, y2, y3;
  if (!PyArg_ParseTuple(args, "dddddd", &x1, &x2, &x3, &y1, &y2, &y3)) {
      return NULL;
  }
  printf("%lf\n", x1*y1 + x2*y2 + x3*y3);
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
    len2 = PySequence_Fast_GET_SIZE(pylist2);// определяем размер

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
      //  printf("%lf\n", list1[i] );
    }//эт заполняет первый массив
    for(i=0; i<len2; i++) {
        PyObject *item2 = PySequence_Fast_GET_ITEM(pylist2,i);
        double_item2 = PyFloat_AsDouble(item2);
        list2[i] = double_item2;
      //  printf("%lf\n", list2[i] );
    }// эт заполняет второй массив

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
      printf("%lf ", inter[i]);
      PyTuple_SET_ITEM(tup, i, PyLong_FromDouble(inter[i]));

    }
    printf("\n");
    return Py_BuildValue("O", tup);
}
static PyMethodDef hello_methods[] = {
    {
        "subtraction", subtraction, METH_VARARGS,
        "subtraction of two complex numbers\nthe first two arguments of the function are the real and imaginary parts of the first number, the second two are the real and imaginary parts of the second number"
    },
    {
        "sum", sum, METH_VARARGS,
        "sum of two complex numbers\nthe first two arguments of the function are the real and imaginary parts of the first number, the second two are the real and imaginary parts of the second number"
    },
    {
        "mult", mult, METH_VARARGS,
        "multiplication of two complex numbers\nthe first two arguments of the function are the real and imaginary parts of the first number, the second two are the real and imaginary parts of the second number"
    },
    {
        "division", division, METH_VARARGS,
        "division of two complex numbers\nthe first two arguments of the function are the real and imaginary parts of the first number, the second two are the real and imaginary parts of the second number"
    },
    {
        "pow_complex", pow_complex, METH_VARARGS,
        "exponentiation of a complex number\nThe first argument to the function is the real part.\nsecond imaginary\nthird degree"
    },
    {
        "intersection", intersection, METH_VARARGS,
        "Print 'hello xxx' from a method defined in a C extension."
    },
    {
        "vectors2d_sum", vectors2d_sum, METH_VARARGS,
        "subtraction of 2-dimension vectors."
    },
    {
        "vectors2d_sub", vectors2d_sub, METH_VARARGS,
        "sum of 2-dimension vectors."
    },
    {
        "vectors2d_scalar_prod", vectors2d_scalar_prod, METH_VARARGS,
        "scalar product of 2-dimension vectors."
    },
    {
        "vectors3d_sum", vectors3d_sum, METH_VARARGS,
        "sum of 3-dimension vectors."
    },
    {
        "vectors3d_sub", vectors3d_sub, METH_VARARGS,
        "subtraction of 3-dimension vectors."
    },
    {
        "vectors3d_scalar_prod", vectors3d_scalar_prod, METH_VARARGS,
        "scalar product of 3-dimension vectors."
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
