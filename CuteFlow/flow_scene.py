#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author wuhongyu
    @Date 2023/5/7 9:40 PM
    @Describe 
    @Version 1.0
"""

from PySide6.QtWidgets import QGraphicsScene
from PySide6.QtCore import QRectF
from PySide6.QtGui import QBrush,QColor,QPen
from flow_configs import FlowSceneConfig


class FlowScene(QGraphicsScene):
    def __init__(self, parent=None):
        super(FlowScene, self).__init__(parent)
        self.setup()

    def setup(self):
        print("setup scene")
        self.setBackgroundBrush(QBrush(QColor('#212621')))
        width = FlowSceneConfig.flow_scene_width
        height = FlowSceneConfig.flow_scene_height
        self.setItemIndexMethod(QGraphicsScene.NoIndex)
        self.setSceneRect(QRectF(-width/2, -height/2, width, height))

        self.addText("this is a text in scene")






