#include <Python.h>
#include <math.h>


static PyObject *G6Error;
static PyObject *NoVerticesError;
static PyObject *TooManyVerticesError;

typedef struct {
    PyObject_HEAD
    char order;
    char **matrix;
} AdjacencyMatrix;

static int number = 0;

static void AdjacencyMatrix__del__(AdjacencyMatrix *self) {

    //printf("Delete %i\n", number--);
    //fflush(stdout);
    for (int i = 0; i < self->order; ++i) {
        free(self->matrix[i]);
    }
    free(self->matrix);
    self->matrix = NULL;
    Py_TYPE(self)->tp_free((PyObject *) self);
}

static PyObject *AdjacencyMatrix__str__(AdjacencyMatrix *self) {
    //printf("String");
    int matrixCells = ((self->order * self->order) - self->order) / 2;
    matrixCells += matrixCells % 6;
    int size = (matrixCells/ 6) + 2;
    //printf("order = %i size= %i matrixCels = %i",self->order,size ,matrixCells);
    char *text = (char*)malloc(size * sizeof(char));
    char *ptr_text = text;
    int k=5;
    char c = 0;
    int v=0;
    int u=0;

    *ptr_text = self->order + 63;

    for ( v= 1; v < self->order; ++v) {
        for (u = 0; u < v; ++u) {
            if(self->matrix[u][v])
            {
                c|= (1<<k);
            }
            if(k==0){
                ptr_text++;
                *ptr_text = c+63;
                k = 6;
                c = 0;
            }
            k-=1;
        }

    }
    if(k!=5){
        ptr_text++;
        *ptr_text = c+63;
    }

    ptr_text++;
    *ptr_text = 0;
//    PyObject *x = PyFloat_FromDouble(self->x);
//    PyObject *y = PyFloat_FromDouble(self->y);
//    PyObject *r = PyUnicode_FromFormat("(%S,%S)", x, y);
//    Py_XDECREF(x);
//    Py_XDECREF(y);
    PyObject* result =PyUnicode_FromString(text);
    //printf("String end\n");
    Py_XINCREF(result);
    return result;
}

static PyObject *AdjacencyMatrix__new__(PyTypeObject *type, PyObject *args) {

    //printf("New %i\n", number++);
    //fflush(stdout);
    return type->tp_alloc(type, 0);
}

static PyObject *AdjacencyMatrix_Order(AdjacencyMatrix *self) {
    //printf("Order");
    long order = self->order;
    PyObject *result =  PyLong_FromLong(order);
    //printf("Order end\n");
    Py_XINCREF(result);
    return result;
}

static PyObject *AdjacencyMatrix_AddVertex(AdjacencyMatrix *self) {
    //printf("addVertex");
    if (self->order == 16) {
        PyErr_SetString(TooManyVerticesError, "too many vertices");
        return 0;
    }
    for (int v = 0; v < self->order; ++v) {
        self->matrix[v] = realloc(self->matrix[v], (self->order + 1) * sizeof(char));
        self->matrix[v][self->order] = 0;
    }
    self->matrix = realloc(self->matrix, (self->order + 1) * sizeof(char *));
    self->matrix[self->order] = (char *) calloc((self->order + 1), sizeof(char));
    self->order += 1;
    //printf("addVertex end\n");
    Py_RETURN_NONE;
}

static PyObject *AdjacencyMatrix_DeleteVertex(AdjacencyMatrix *self, PyObject *args) {
    int i = 0;
    int j = 0;

    //printf("Delete vertex");
    if (self->order == 1 || self->order == 0) {
        printf("NoVertex\n");
        PyErr_SetString(NoVerticesError, "graph must have vertices");
        return 0;
    }
    double d = PyLong_AsDouble(args);
    int u = d;

    free(self->matrix[u]);
    self->order -= 1;
    for (i = u; i < self->order; ++i) {
        self->matrix[i] = self->matrix[i + 1];
    }
    for (i = 0; i < self->order; ++i) {
        for (j = u; j < self->order; ++j) {

            self->matrix[i][j] = self->matrix[i][j + 1];
        }
    }

    //printf("Delete vertex end\n");
    Py_RETURN_NONE;
}

static PyObject *AdjacencyMatrix_IsEdge(AdjacencyMatrix *self, PyObject *obj) {
    int u, v;

    //printf("Add Edge");
    if (!PyArg_ParseTuple(obj, "|ii", &u, &v)) {
        Py_RETURN_NONE;
    }

    if(self->matrix[u][v])
    {
        Py_RETURN_TRUE;
    } else{
        Py_RETURN_FALSE;
    }
}

static PyObject *AdjacencyMatrix_AddEdge(AdjacencyMatrix *self, PyObject *obj) {
    int u, v;

    //printf("Add Edge");
    if (!PyArg_ParseTuple(obj, "|ii", &u, &v)) {
        Py_RETURN_NONE;
    }
    self->matrix[u][v] = 1;
    self->matrix[v][u] = 1;
    //printf("Add Edge end\n");
    Py_RETURN_NONE;
}

static PyObject *AdjacencyMatrix_DeleteEdge(AdjacencyMatrix *self, PyObject *obj) {
    int u, v;

    //printf("Delete Edge");
    if (!PyArg_ParseTuple(obj, "|ii", &u, &v)) {
        Py_RETURN_NONE;
    }
    self->matrix[u][v] = 0;
    self->matrix[v][u] = 0;
    //printf("Delete Edge end\n");
    Py_RETURN_NONE;
}

static PyObject *AdjacencyMatrix_FromString(AdjacencyMatrix *self, PyObject *obj) {

    char *c_text;
    char c = NULL;
    char k = NULL;
    char v, u;

    //printf("FromString\n");
    if (!PyArg_ParseTuple(obj, "s", &c_text)) {
        printf("return 0");
        PyErr_Clear();
        Py_RETURN_NONE;
    }

    //printf("string = %s ", c_text);
    //printf("value = %i\n", (int) (*c_text));
    if (*c_text == 0) {
        PyErr_SetString(G6Error, "too short text");
        return 0;
    }
    c = *c_text - 63;
    if (c < 1 || c > 16) {
        PyErr_SetString(G6Error, "wrong order");
        return 0;
    }
    self->matrix = (char **) malloc(sizeof(char *) * c);
    for (v = 0; v < c; ++v) {
        self->matrix[v] = (char *) malloc(sizeof(char) * c);
    }
    self->order = c;

    //printf("order %i \n", self->order);
    for (v = 0; v < self->order; ++v) {
        for (u = 0; u < v; ++u) {

            //printf("value[%i][%i]\n", u,v);
            if (k == 0) {
                c_text++;

                //printf("char %c \n", *c_text);
                if (*c_text == 0) {
                    PyErr_SetString(G6Error, "too short text");
                    return -1;
                }
                c = *c_text - 63;
                if (c < 0 || c > 63) {
                    PyErr_SetString(G6Error, "wrong character");
                    return 0;
                }
                k = 6;
            }
            k -= 1;
            //printf("value[%i][%i] %i \n", u,v,(c & (1 << k)));
            self->matrix[u][v] = (char) (c & (1 << k));
            self->matrix[v][u] = (char) (c & (1 << k));
        }
    }
    c_text++;
    if (*c_text != 0) {
        PyErr_SetString(G6Error, "too long text");
        return 0;
    }
    //printf("FromString end\n");
    Py_RETURN_NONE;
}

static int AdjacencyMatrix__init__(AdjacencyMatrix *self, PyObject *args) {
    PyObject *t = AdjacencyMatrix_FromString(self, args);
    if(t!=Py_None)
    {
        Py_XDECREF(t);
        return -1;
    }
    Py_XDECREF(t);
    return 0;
}

static PyObject* AdjacencyMatrix_richcompare(PyObject *a, PyObject *b, int op)
{
    //printf("Compare");
    PyObject *a_temp = PyObject_Str(a);
    PyObject *b_temp = PyObject_Str(b);

    const char* a_text;
    const char* b_text;

    if (!PyArg_ParseTuple(a_temp, "s", &a_text)) {
        printf("return 0");
        PyErr_Clear();
        Py_RETURN_NONE;
    }

    if (!PyArg_ParseTuple(b_temp, "s", &b_text)) {
        printf("return 0");
        PyErr_Clear();
        Py_RETURN_NONE;
    }

    Py_XDECREF(a_temp);
    Py_XDECREF(b_temp);

    while  (*a_text != 0 && *b_text!=0)
    {
        if(*a_text!=*b_text)
        {
            if(op == Py_EQ)
            {
                //printf("Compare end");
                Py_RETURN_FALSE;
            } else
            {
                //printf("Compare end");
                Py_RETURN_TRUE;
            }
        }
        a_text++;
        b_text++;
    }

    if(*a_text == 0 && *b_text==0)
    {
        if(op == Py_EQ)
        {
            //printf("Compare end");
            Py_RETURN_TRUE;
        } else
        {
            //printf("Compare end");
            Py_RETURN_FALSE;
        }
    }

    if(op == Py_EQ)
    {
        //printf("Compare end");
        Py_RETURN_FALSE;
    } else
    {
        //printf("Compare end");
        Py_RETURN_TRUE;
    }
}

static PyMethodDef AdjacencyMatrixMethods[] = {
        {"order",        (PyCFunction) AdjacencyMatrix_Order,        METH_NOARGS,  "Return the first coordinate."},
        {"addVertex",    (PyCFunction) AdjacencyMatrix_AddVertex,    METH_NOARGS,  "Return the first coordinate."},
        {"deleteVertex", (PyCFunction) AdjacencyMatrix_DeleteVertex, METH_O,       "Return the first coordinate."},
        {"isEdge",       (PyCFunction) AdjacencyMatrix_IsEdge,       METH_VARARGS, "Return the first coordinate."},
        {"addEdge",      (PyCFunction) AdjacencyMatrix_AddEdge,      METH_VARARGS, "Return the first coordinate."},
        {"deleteEdge",   (PyCFunction) AdjacencyMatrix_DeleteEdge,   METH_VARARGS, "Return the first coordinate."},
        {"fromString",   (PyCFunction) AdjacencyMatrix_FromString,   METH_O,       "Return the first coordinate."},
        {NULL}
};

static PyTypeObject AdjacencyMatrixType = {
        PyVarObject_HEAD_INIT(NULL, 0)
        "simple_graphs.AdjacencyMatrix",
        sizeof(AdjacencyMatrix),
        0,
        (destructor) AdjacencyMatrix__del__,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        (reprfunc) AdjacencyMatrix__str__,
        0, 0, 0,
        Py_TPFLAGS_DEFAULT,
        "MY CLASS TEST",
        0, 0,
        (richcmpfunc)AdjacencyMatrix_richcompare,
        0, 0, 0,
        AdjacencyMatrixMethods,
        0, 0, 0, 0, 0, 0, 0,
        (initproc) AdjacencyMatrix__init__,
        0,
        (newfunc) AdjacencyMatrix__new__
};

static PyModuleDef simple_graphs_module = {
        PyModuleDef_HEAD_INIT,
        "AdjacencyMatrix",
        "CLASS TEST",
        -1,
        NULL, NULL, NULL, NULL, NULL
};

PyMODINIT_FUNC PyInit_simple_graphs(void) {
    AdjacencyMatrixType.tp_dict = PyDict_New();
    if (!AdjacencyMatrixType.tp_dict) return NULL;


    G6Error = PyErr_NewException("simple_graph.AdjacencyMatrix.G6Error", NULL, NULL);
    Py_INCREF(G6Error);
    PyDict_SetItemString(AdjacencyMatrixType.tp_dict, "G6Error", G6Error);

    NoVerticesError = PyErr_NewException("simple_graph.AdjacencyMatrix.NoVerticesError", NULL, NULL);
    Py_INCREF(NoVerticesError);
    PyDict_SetItemString(AdjacencyMatrixType.tp_dict, "NoVerticesError", NoVerticesError);

    TooManyVerticesError = PyErr_NewException("simple_graph.AdjacencyMatrix.TooManyVerticesError", NULL, NULL);
    Py_INCREF(TooManyVerticesError);
    PyDict_SetItemString(AdjacencyMatrixType.tp_dict, "TooManyVerticesError", TooManyVerticesError);

    if (PyType_Ready(&AdjacencyMatrixType) < 0) return NULL;
    PyObject *m = PyModule_Create(&simple_graphs_module);

    if (m == NULL) return NULL;

    Py_INCREF(&AdjacencyMatrixType);
    PyModule_AddObject(m, "AdjacencyMatrix", (PyObject *) &AdjacencyMatrixType);

    return m;
}


//int main()
//{
//    AdjacencyMatrix d;
//    AdjacencyMatrix_FromString(&d,"O????????????????????");
//    return 0;
//}