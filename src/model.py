from dotenv import load_dotenv, find_dotenv
import os
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams

load_dotenv(find_dotenv())
WATSON_ML_URL = os.environ["WATSON_ML_URL"]
WATSONX_API_KEY = os.environ["WATSONX_API_KEY"]
PROJECT_ID = os.environ["WATSONX_PROJECT_ID"]

my_credentials = {"url": WATSON_ML_URL, "apikey": WATSONX_API_KEY}

generate_params = {GenParams.TEMPERATURE: 1.0, GenParams.MAX_NEW_TOKENS: 400}

model_id = ModelTypes.MPT_7B_INSTRUCT2
project_id = PROJECT_ID
space_id = None
verify = False

model = Model(model_id, my_credentials, generate_params, project_id, space_id, verify)
