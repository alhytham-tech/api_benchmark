#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-11-19 04:52:34
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


from pydantic import BaseModel, Field


class URL(BaseModel):
    url: str = Field(..., description="URL")


class NoServersFile(Exception):
    pass


class CriticalError(Exception):
    pass

