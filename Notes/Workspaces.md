# workspaces

Workspaces are at the core of <abbr title="System Amanuensis - product">SA</abbr>. They can support the execution project that include tasks or standalone tasks. They provide a storage space for data and tools associated with a task. It is intended that workspaces should be self sufficient and that they should supply all the resources needed to perform a task.

These are initial thoughts and subject to change before they are used, in any way, to support application development.

## Nature

Tasks are a unit of work. They can be standalone or they can be found as the executable components of projects. Other classifications can be used if they make more sense in specialized environments.

Workspaces are essentially containers that hold all the computer based resources needed to perform a task. These can include:

* Data
* Information
* Tools

## Content

Everything that can be defined for a task can be defined for a project and individual tasks within a project only need to contain changes from the project requirements that provide specialized support  for an individual project. On the other hand, standalone tasks need a full definition of the resources required and do not depend on a parent for data and tools.

### Data

This is data needed for completion of the task or data generated during the process of doing the task. Using or generating such data is frequently needed to accomplish a task. If a project or other high-level infrastructure is involved, data may reside at the parent level, rather than in individual tasks.

### Information

Here we have data related to a task or to its' performance that helps one understand the task and all the aspects of task performance without directly helping task performance. An example might be a list of the people involved in doing the task along with a reason for their involvement.
Information helps people involved in a task but does not contribute directly to its' execution.

#### Task Information

This generally includes meta-information about a task that helps others to undersand the reason for a task and what it is trying to do.

#### External Resources

Any information that is useful for understanding or managing the task, goes here.

### Tools

Whatever tools that are necessary should be included here, It is intended that a workspace is fully self contained, that is, all the tools needed to do the job are contained in it. This is an extension of the idea of virtual environments that is used in Python. The tools are all at specific versions that work together and they don't impact any other task. By collecting everything together, setting up a clone of the workspace becomes simple.>

Examples of tools could include an editor, a language compiler or a program library.

## Purpose

### Projects

### Tasks

#### Execution

## Types

### People

#### Jonathan Gossage

### Organizations

#### Programming Renaissance

##### System Amanuensis

