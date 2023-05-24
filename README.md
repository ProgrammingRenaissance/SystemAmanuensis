# SystemAmanuensis

This product is intended to help take the pain out of system administration. It will have a number of components:
* Framework
* Action Module<br>
  There will be one for each action to be performed.

Incidentally, the use of the word **amanuensis** may need some explanation.It has dropped out of current usage but it describes a helper or personal assistant. It perfectly describes what the <abbr title=System Amanuensis>SA</abbr> product is all about.

## Framework

The purpose of the framework is to provide a common environment and to provide access to the common services that should be available to every SA component.

### Framework Services

#### Command Line Argument Capture

#### Configuration

#### Logging Initialization

#### Setup

#### Teardown

#### Action management

##### Structure

All actions will have a common infrastructure that will support error management specifically. This infrastructure will capture all unhandled exceptions, handle them appropriately doing such things as logging, error reporting and recovery where meaningful.

###### Error Management

###### Logging

###### Action Specific Initialization and Cleanup

### Testing Framework

Testing of any type will be based on testing framework supplied by Python.

### Production Framework

## Actions
