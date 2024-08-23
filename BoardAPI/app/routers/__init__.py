import glob
import os.path as path
from fastapi import APIRouter
from importlib import import_module
# from app.internal.common_route_class import MyCustomRoute

modules = glob.glob(path.join(path.dirname(__file__), "*.py"))
__all__ = [path.basename(f)[:-3] for f in modules if path.isfile(f) and not f.endswith("__.py")]

app_v1 = APIRouter(prefix="/v1", tags=["Board API"])

# app_v1.route_class = MyCustomRoute

for name in __all__:
    module = import_module(f"app.routers.{name}")
    app_v1.include_router(module.router)