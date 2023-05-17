#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author wuhongyu
    @Date 2023/5/7 9:40 PM
    @Describe 
    @Version 1.0
"""

from PySide6.QtWidgets import QGraphicsScene
from flow_configs import FlowSceneConfig


class FlowScene(QGraphicsScene):
    def __init__(self):
        super(FlowScene, self).__init__()
        self.setup()

    def setup(self):
        print("setup scene")
        width = FlowSceneConfig.flow_scene_width
        height = FlowSceneConfig.flow_scene_height

        self.setSceneRect(-width/2, -height/2, width, height)

        self.addText("this is a text in scene")





