*********
Templates
*********

The template mechanism provides a way for Python source code to be
generated rather than on it being duplicated by typing the same
structural thing time after time.

Initial
=======

Initially, the template mechanism will be kept simple so as to get
something useful as quickly as possible.

Templates will be Python source code modules that control the process of
generating Python modules that will perform whatever processing that is
required of a Python script or application.

The base modules will contain the infrastructure code that supports the
generation of any Python module. Base template modules will be
subclassed by modules that define how a specific module should be
generated.
