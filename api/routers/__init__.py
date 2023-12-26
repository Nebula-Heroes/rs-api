from fastapi import APIRouter
router = APIRouter(tags=["stacks"])
from ..main import engine, users_interactions_table, articles_table
from ..main import popularity_worker, content_based_worker, hybrid_worker

from .index import *
from .interaction import *