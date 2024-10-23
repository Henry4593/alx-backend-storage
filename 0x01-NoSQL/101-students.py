#!/usr/bin/env python3
'''Module for retrieving top students based on their average score.
'''


def top_students(mongo_collection):
    '''Returns all students in a collection sorted by average score.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB
        collection containing student documents.

    Returns:
        pymongo.command_cursor.CommandCursor: A cursor to the sorted list of
        students.
    '''
    students = mongo_collection.aggregate(
        [
            {
                '$project': {
                    '_id': 1,
                    'name': 1,
                    'averageScore': {
                        '$avg': '$topics.score',
                    },
                    'topics': 1,
                },
            },
            {
                '$sort': {'averageScore': -1},
            },
        ]
    )
    return students
