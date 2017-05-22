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
        -e AWS_ACCESS_KEY_ID=KEYID                                      \
        -e AWS_SECRET_ACCESS_KEY=ACCESSKEY                              \
        -v $(pwd)/out:/incoming                                         \
        -v $(pwd)/out2:/outgoing                                        \
        fnndsc/pl-s3push                                                \
        s3push.py --bucket bch-fnndsc --prefix test /incoming /outgoing

The above will push a copy of each file/folder in the container's ``/incoming`` to Amazon
S3 storage and prefix the copy with the ``prefix`` text (in this case "test"). Some
metadata files will be written to the container's ``/outgoing`` directory.

Make sure that the host ``$(pwd)/out`` directory is world readable and ``$(pwd)/out2``
directory is world writable!
