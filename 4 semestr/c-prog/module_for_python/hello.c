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

static PyObject *py_expected_value(PyObject *self, PyObject *args) {
    PyObject *pylist1, *pylist2;
    double  double_item1, double_item2, len1, len2;
    double result = 0;
    double* list1;
    double* list2;
    double* inter;
    int i,i1;
    int i2 = -1;

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
        printf("f\n");
        if(list1[i]== list2[i1]){
          //printf("%d\n",i );
          i2++;
          inter[i2] = list1[i];
        }
      }
    }
    for(i = 0; i<= sizeof(inter)/8;i++){//воспомнить,какой критерий остановки динамического массива
      printf("%lf\n", inter[i]);
    }
    return Py_BuildValue("d", result);
}

/* here is how you expose it to Python code: */


// Method definition object for this extension, these argumens mean:
// ml_name: The name of the method
// ml_meth: Function pointer to the method implementation
// ml_flags: Flags indicating special features of this method, such as
//          accepting arguments, accepting keyword arguments, being a
//          class method, or being a static method of a class.
// ml_doc:  Contents of this method's docstring
//какое-то оформление
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
    {
        "py_expected_value", py_expected_value, METH_VARARGS,
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
