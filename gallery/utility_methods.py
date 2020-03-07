import uuid
import os

"""
------------------------------------------
Method to provide filename and upload path
------------------------------------------
"""
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/photos', filename)
