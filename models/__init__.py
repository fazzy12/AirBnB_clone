#!/usr/bin/env python3
"""This module contains the BaseModel class"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
