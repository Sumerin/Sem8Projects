#include <Python.h>
#include <math.h>



static PyObject *G6Error;
static PyObject *NoVerticesError;
static PyObject *TooManyVerticesError;

typedef struct{
    PyObject_HEAD
    double x,y;
} AdjacencyMatrix;

static PyObject* AdjacencyMatrix__init__(AdjacencyMatrix *self, PyObject *args)
{
    PyErr_SetString(G6Error,"lol");
    return NULL;
    /*double x = 0.0, y = 0.0;
    if (PyArg_ParseTuple( args, "|dd", &x, &y ))
    {
        self->x = x;
        self->y = y;
        return 0;
    }
    return -1;*/
}

static void AdjacencyMatrix__del__( AdjacencyMatrix *self ) 
{
Py_TYPE( self )->tp_free( (PyObject *)self );
}

static PyObject *AdjacencyMatrix__str__( AdjacencyMatrix *self )
 {
PyObject *x = PyFloat_FromDouble( self->x );
PyObject *y = PyFloat_FromDouble( self->y );
PyObject *r = PyUnicode_FromFormat( "(%S,%S)", x, y );
Py_XDECREF( x );
Py_XDECREF( y );
return r;
}

static PyObject *AdjacencyMatrix__new__(PyTypeObject *type, PyObject *args ) 
{
return type->tp_alloc( type, 0 );
}

static PyObject *AdjacencyMatrix_Order( AdjacencyMatrix *self ) {
return PyFloat_FromDouble( self->x );
}

static PyObject *AdjacencyMatrix_AddVertex( AdjacencyMatrix *self ) {
return PyFloat_FromDouble( self->x );
}

static PyObject *AdjacencyMatrix_DeleteVertex( AdjacencyMatrix *self ) {
return PyFloat_FromDouble( self->x );
}

static PyObject *AdjacencyMatrix_IsEdge( AdjacencyMatrix *self ) {
return PyFloat_FromDouble( self->x );
}

static PyObject *AdjacencyMatrix_AddEdge( AdjacencyMatrix *self ) {
return PyFloat_FromDouble( self->x );
}

static PyObject *AdjacencyMatrix_DeleteEdge( AdjacencyMatrix *self ) {
return PyFloat_FromDouble( self->x );
}

static PyObject *AdjacencyMatrix_FromString( AdjacencyMatrix *self ) {
return PyFloat_FromDouble( self->x );
}



static PyMethodDef AdjacencyMatrixMethods[] = {
{ "order", (PyCFunction)AdjacencyMatrix_Order, METH_NOARGS,"Return the first coordinate." },
{ "addVertex", (PyCFunction)AdjacencyMatrix_AddVertex, METH_NOARGS,"Return the first coordinate." },
{ "deleteVertex", (PyCFunction)AdjacencyMatrix_DeleteVertex, METH_NOARGS,"Return the first coordinate." },
{ "isEdge", (PyCFunction)AdjacencyMatrix_IsEdge, METH_NOARGS,"Return the first coordinate." },
{ "addEdge", (PyCFunction)AdjacencyMatrix_AddEdge, METH_NOARGS,"Return the first coordinate." },
{ "deleteEdge", (PyCFunction)AdjacencyMatrix_DeleteEdge, METH_NOARGS,"Return the first coordinate." },
{ "fromString", (PyCFunction)AdjacencyMatrix_FromString, METH_NOARGS,"Return the first coordinate." },
{ NULL }
};

static PyTypeObject AdjacencyMatrixType = {
PyVarObject_HEAD_INIT(NULL,0)
"simple_graphs.AdjacencyMatrix",
sizeof(AdjacencyMatrix),
0,
(destructor)AdjacencyMatrix__del__,
0,0,0,0,0,0,0,0,0,0,
(reprfunc)AdjacencyMatrix__str__,
0,0,0,
Py_TPFLAGS_DEFAULT,
"MY CLASS TEST",
0,0,0,0,0,0,
AdjacencyMatrixMethods,
0,0,0,0,0,0,0,
(initproc)AdjacencyMatrix__init__,
0,
(newfunc)AdjacencyMatrix__new__
};

static PyModuleDef simple_graphs_module = {
PyModuleDef_HEAD_INIT,
"AdjacencyMatrix",
"CLASS TEST",
-1,
NULL, NULL, NULL, NULL, NULL
};

PyMODINIT_FUNC PyInit_simple_graphs( void ) 
{
AdjacencyMatrixType.tp_dict = PyDict_New();
if(!AdjacencyMatrixType.tp_dict) return NULL;
/*
if (PyType_Ready( &G6ErrorType ) < 0) return NULL;
Py_INCREF(&G6ErrorType);
PyDict_SetItemString(AdjacencyMatrixType.tp_dict, "G6Error", (PyObject*)&G6ErrorType);

if (PyType_Ready( &NoVerticesErrorType ) < 0) return NULL;
Py_INCREF(&NoVerticesErrorType);
PyDict_SetItemString(AdjacencyMatrixType.tp_dict, "NoVerticesError", (PyObject*)&NoVerticesErrorType);

if (PyType_Ready( &TooManyVerticesErrorType ) < 0) return NULL;
Py_INCREF(&TooManyVerticesErrorType);
PyDict_SetItemString(AdjacencyMatrixType.tp_dict, "TooManyVerticesError", (PyObject*)&TooManyVerticesErrorType);
*/

G6Error = PyErr_NewException("simple_graph.AdjacencyMatrix.G6Error", NULL, NULL);
Py_INCREF(G6Error);
PyDict_SetItemString(AdjacencyMatrixType.tp_dict, "G6Error",G6Error );

NoVerticesError = PyErr_NewException("simple_graph.AdjacencyMatrix.NoVerticesError", NULL, NULL);
Py_INCREF(NoVerticesError);
PyDict_SetItemString(AdjacencyMatrixType.tp_dict, "NoVerticesError",NoVerticesError );

TooManyVerticesError = PyErr_NewException("simple_graph.AdjacencyMatrix.TooManyVerticesError", NULL, NULL);
Py_INCREF(TooManyVerticesError);
PyDict_SetItemString(AdjacencyMatrixType.tp_dict, "TooManyVerticesError",TooManyVerticesError );

if (PyType_Ready( &AdjacencyMatrixType ) < 0) return NULL;
PyObject* m = PyModule_Create( &simple_graphs_module );

if (m == NULL) return NULL;

Py_INCREF( &AdjacencyMatrixType );
PyModule_AddObject( m, "AdjacencyMatrix",(PyObject *)&AdjacencyMatrixType );

return m;
}
