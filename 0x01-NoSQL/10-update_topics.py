#!/usr/bin/env python3
"""
Module for updating topics in a MongoDB collection.
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates all topics of a document in a MongoDB collection based on the name.

    Args:
        mongo_collection: The pymongo collection object.
        name (str): The name of the document to update.
        topics (list of str): The list of topics to set for the document.
    """
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
