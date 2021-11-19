#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-11-19 04:43:37
# @Author  : Dahir Muhammad Dahir
# @Description : Tool for benchmarking web applications


from typing import List
from threading import Thread

from models import URL, CriticalError
from requester import requester

def main():
    urls = get_urls()
    benchmark(urls)


def get_urls() -> List[URL]:
    url_list_file = input("{x} Enter the url list filename, [urls_file.dmd]:\n").strip("\n")

    if not url_list_file:
        print("{x} No filename provided, using default filename: urls_file.dmd\n")
        url_list_file = "sample/urls_file.dmd"
    
    try:
        with open(url_list_file) as f:
            urls = f.readlines()
        
        if not urls:
            raise CriticalError("{x} No urls found in the file")
        
        return [URL(url=url.strip().strip("\r\n").strip("\r").strip("\n")) for url in urls]

    except FileNotFoundError:
        raise CriticalError("{x} URLs File not found, Please a provide a full file path\n")


def benchmark(urls: List[URL]):
    print("{x} Starting benchmarking...\n")
    print(f"{{x}} Loaded {len(urls)} URLs...")

    auth_token = input("{x} Provide optional JWT authentication token [None]:\n").strip("\n")
    if auth_token and not auth_token.startswith("Bearer"):
        auth_token = f"Bearer {auth_token}"
    
    headers = {"Authorization": auth_token}

    try:
        requests_per_url = int(input("{x} How many requests per url? \n").strip("\n"))
        concurrency = int(input("{x} How many concurrent requests per url? \n").strip("\n"))
    except ValueError:
        raise CriticalError("{x} Only numbers are allowed")
    
    rounds = requests_per_url // concurrency

    total_requests = len(urls) * requests_per_url

    workers: List[Thread] = []

    for round in range(1, rounds + 1):
        workers = []
        for url in urls:
            for i in range(1, concurrency + 1):
                worker = Thread(target=requester, args=(url.url, "get", None, None, headers))
                workers.append(worker)
        
        print(f"{{x}} Queued {len(workers)} requests")
        
        for worker in workers:
            worker.start()
        
        for worker in workers:
            worker.join()
        
        print(f"{{x}} Completed {len(workers) * round} requests of {total_requests} requests...")
    
    print(f"{{x}} All jobs completed successfully")


if __name__ == "__main__":
    main()

