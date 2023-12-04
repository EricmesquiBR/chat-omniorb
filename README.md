# OmniORB - CORBA Chat

Implementation of a CORBA based chat using omniorb and tkinter for the interface.


## 1. Create and activate a CONDA env:

    $ conda create -n omni-env -c conda-forge python=3.10 omniorb omniorbpy

    $ conda activate omni-env

## 2. Generate Python Code from IDL on both computers:

    $ omniidl -bpython chat.idl

## 3. Run the OmniORB Service on both computers:

    $ omniNames -start

## 4. Run the Server on computer A:

    $ python server.py

## 5. Run the Client on computer B:

    $ python client.py

## 6. Enter the IOR obtained from the server terminal on computer A:

    $ Enter IOR:

    IOR:010000001a...


