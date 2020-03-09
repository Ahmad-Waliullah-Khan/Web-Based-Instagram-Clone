import uuid
import os


#===============================================================================
# get_file_path
#===============================================================================
def get_file_path(instance, filename):
    """
    ------------------------------------------
    Method to provide filename and upload path
    ------------------------------------------
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/photos', filename)
