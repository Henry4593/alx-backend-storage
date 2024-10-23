#!/usr/bin/env python3
"""
A module for caching and tracking HTTP requests using Redis.
"""
import redis
import requests
from functools import wraps
from typing import Callable

redis_store = redis.Redis()
"""The module-level Redis instance."""


def data_cacher(method: Callable) -> Callable:
    """
    Decorator that caches the output of the decorated function.

    Args:
        method (Callable): The function to be decorated.

    Returns:
        Callable: The wrapped function with caching.
    """
    @wraps(method)
    def invoker(url: str) -> str:
        """
        Wrapper function that implements caching.

        Args:
            url (str): The URL to fetch.

        Returns:
            str: The content of the URL, either from cache or fetched.
        """
        redis_store.incr(f'count:{url}')
        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        redis_store.set(f'count:{url}', 0)
        redis_store.setex(f'result:{url}', 10, result)
        return result
    return invoker


@data_cacher
def get_page(url: str) -> str:
    """
    Fetches the content of a URL and caches the response.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The content of the URL.
    """
    return requests.get(url).text
