#########
pl-s3push
#########


Abstract
========

A Chris 'ds' plugin to push files/folders in input directory to Amazon S3 service.

Preconditions
=============

This plugin requires input and output directories as a precondition.

Run
===

Using ``docker run``
--------------------

Assign an "input" directory to ``/incoming`` and an output directory to ``/outgoing``

.. code-block:: bash

    docker run --rm                                                     \
        -v /tmp/input:/incoming                                         \
        -v /tmp/output:/outgoing                                        \
        fnndsc/pl-s3push                                                \
        s3push.py --awskeyid KEYID --awssecretkey ACCESSKEY --bucket bch-fnndsc --prefix test /incoming /outgoing

The above will push a copy of each file/folder in the container's ``/incoming`` to Amazon
S3 storage and prefix the copy with the ``prefix`` text (in this case "test"). Some
metadata files will be written to the container's ``/outgoing`` directory.

Make sure that the host ``/tmp/input`` directory is world readable and ``/tmp/output``
directory is world writable!
