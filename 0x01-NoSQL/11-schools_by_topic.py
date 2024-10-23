#!/usr/bin/env python3
'''Module to find schools by topic in a MongoDB collection.
'''


def schools_by_topic(mongo_collection, topic):
    '''Returns a list of schools that have a specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB
                                                        collection to search.
        topic (str): The topic to search for.

    Returns:
        list: A list of dictionaries representing the schools that have the
            specified topic.
    '''
    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(topic_filter)]
