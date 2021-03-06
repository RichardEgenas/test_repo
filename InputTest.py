import re
import os.path

api_key = prompt(message = "Enter the API key to use for uploading",
                 errormessage= "A valid API key must be provided. This key can be found in your user profile",
                 isvalid = lambda v : re.search(r"(([^-])+-){4}[^-]+", v))

filename = prompt(message = "Enter the path of the file to upload",
        errormessage= "The file path you provided does not exist",
        isvalid = lambda v : os.path.isfile(v))

dataset_name = prompt(message = "Enter the name of the dataset you want to create",
        errormessage= "The dataset must be named",
        isvalid = lambda v : len(v) > 0)

