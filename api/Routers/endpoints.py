from fastapi import APIRouter, Header
from data.connection import confirmed_global
from data.connection import deaths_global
from data.connection import recovered_global
from bson import json_util
from json import loads

router = APIRouter()

### endpoints
