#include "Python.h"
// gcc -c $(python2.7-config --cflags) test_python.c
// gcc test_python.o $(/usr/bin/python2.7-config --ldflags)
int main(int argc, char *argv[])
{
  Py_SetProgramName(argv[0]);  /* optional but recommended */
  Py_Initialize();
  PyRun_SimpleString("from time import time,ctime\n"
                     "print 'Today is',ctime(time())\n");

  /*Or if you want to run python file within from the C code*/
  //pyRun_SimpleFile("Filename");
  Py_Finalize();
  return 0;
}
