#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author wuhongyu
    @Date 2023/5/7 9:37 PM
    @Describe 
    @Version 1.0
"""
from PySide6.QtWidgets import QGraphicsView
from flow_scene import FlowScene


class FlowView(QGraphicsView):
    def __init__(self, scene: FlowScene, parent=None):
        super(FlowView, self).__init__(parent)
        self.scene = scene
        self.setup()

    def setup(self):
        self.setWindowTitle("view")
        print("setup view")
        self.setScene(self.scene)




