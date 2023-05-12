#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author wuhongyu
    @Date 2023/5/7 11:38 PM
    @Describe 
    @Version 1.0
"""
from PySide6.QtWidgets import QGraphicsRectItem


class FlowRectItem(QGraphicsRectItem):
    def __init__(self):
        super(FlowRectItem, self).__init__()
        self.setup()

    def setup(self):
        print("added a item")

