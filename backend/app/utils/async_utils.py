"""
Async utility helpers for concurrent execution and retries.
"""

import asyncio
from typing import Any, Awaitable, Callable


async def run_async_tasks(tasks: list[Awaitable[Any]]) -> list[Any]:
    """
    Run multiple async tasks concurrently.

    Example:
        results = await run_async_tasks([
            scrape_site(),
            fetch_jobs(),
            fetch_news(),
        ])
    """

    return await asyncio.gather(*tasks, return_exceptions=True)


async def retry_async(
    func: Callable,
    *args,
    retries: int = 3,
    delay: int = 2,
    **kwargs,
):
    """
    Retry async function execution.

    Example:
        result = await retry_async(fetch_data, url)
    """

    last_exception = None

    for attempt in range(retries):
        try:
            return await func(*args, **kwargs)

        except Exception as exc:
            last_exception = exc

            if attempt < retries - 1:
                await asyncio.sleep(delay)

    raise last_exception


async def timeout_wrapper(
    coro: Awaitable[Any],
    timeout: int = 30,
):
    """
    Add timeout protection to async operations.
    """

    return await asyncio.wait_for(coro, timeout=timeout)