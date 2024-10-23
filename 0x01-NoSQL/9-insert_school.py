#!/usr/bin/env python3
"""
Module for inserting a new document into a MongoDB collection.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a specified MongoDB collection.

    Args:
        mongo_collection: The MongoDB collection instance.
        **kwargs: Arbitrary keyword arguments representing the document fields.

    Returns:
        The ID of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
