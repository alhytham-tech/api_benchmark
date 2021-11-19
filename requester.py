#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-11-19 04:45:26
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


from typing import Optional, Dict
import requests


def requester(
    url, 
    method: str = "get", 
    files: Optional[Dict] = None, 
    data: Optional[Dict] = None, 
    headers: Optional[Dict] = None,
    json: Optional[Dict] = None
) -> None:
    with requests.Session() as s:
        response: requests.Response = getattr(s, method)(url, files=files, data=data, json=json, headers=headers)
        print(f"{{x}} Request for: {url} got response: {response.status_code}\n")


