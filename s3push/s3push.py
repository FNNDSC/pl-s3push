#                                                            _
# S3 Push ds app
#
# (c) 2016 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#

import os

# import the Chris app superclass
from chrisapp.base import ChrisApp
import boto3


class S3PushApp(ChrisApp):
    """
    Push the files/folders in input directory to Amazon S3 service.
    """
    AUTHORS         = 'FNNDSC (dev@babyMRI.org)'
    SELFPATH        = os.path.dirname(os.path.abspath(__file__))
    SELFEXEC        = os.path.basename(__file__)
    EXECSHELL       = 'python3'
    TITLE           = 'S3 Push'
    CATEGORY        = ''
    TYPE            = 'ds'
    DESCRIPTION     = 'An app to push data of interest to Amazon S3 service'
    DOCUMENTATION   = 'http://wiki'
    LICENSE         = 'Opensource (MIT)'
    VERSION         = '0.1'

    # Fill out this with key-value output descriptive info (such as an output file path
    # relative to the output dir) that you want to save to the output meta file when
    # called with the --saveoutputmeta flag
    OUTPUT_META_DICT = {}

    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        """
        self.add_argument('--bucket', dest='bucket', type=str, optional=False,
                          help='name of the Amazon S3 bucket')
        self.add_argument('--prefix', dest='prefix', type=str, optional=False,
                           help='prefix string to be added to the s3 objects key')
        self.add_argument('--awskeyid', dest='awskeyid', type=str,
                          optional=False, help='aws access key id')
        self.add_argument('--awssecretkey', dest='awssecretkey',
                          type=str, optional=False, help='aws secret access key')

    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """

        # options.outputdir is not being used! Some output data file needs to be written!

        # get Amazon S3 credentials
        if options.awskeyid and options.awssecretkey:
            s3client = boto3.client(
                's3',
                aws_access_key_id=options.awskeyid,
                aws_secret_access_key=options.awssecretkey
            )
        else:
            s3client = boto3.client('s3')

        # upload folders/files to Amazon S3
        for (dirpath, dirnames, filenames) in os.walk(options.inputdir):
            relative_path = dirpath.replace(options.inputdir, "").strip('/')
            for fname in filenames:
                key = os.path.join(options.prefix, relative_path, fname)
                s3client.upload_file(os.path.join(dirpath, fname), options.bucket, key,
                                     {'ServerSideEncryption': 'AES256'})


# ENTRYPOINT
if __name__ == "__main__":
    app = S3PushApp()
    app.launch()
