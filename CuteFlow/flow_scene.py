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
from PySide6.QtGui import QBrush,QColor,QPen, QPainter
from PySide6.QtCore import QLine
from flow_configs import FlowSceneConfig
import math


class FlowScene(QGraphicsScene):
    def __init__(self, parent=None):
        super(FlowScene, self).__init__(parent)
        self.setup()

    def setup(self):
        print("setup scene")
        self.setBackgroundBrush(QBrush(QColor(FlowSceneConfig.flow_scene_green_bg))) # 设置背景颜色
        width = FlowSceneConfig.flow_scene_width
        height = FlowSceneConfig.flow_scene_height
        self.setItemIndexMethod(QGraphicsScene.NoIndex)
        self.setSceneRect(QRectF(-width/2, -height/2, width, height)) # 设置背景区域

        self.addText("this is a text in scene")

        # 设置普通线的笔颜色和粗细
        self.flow_scene_normal_line_pen = QPen(QColor(FlowSceneConfig.flow_scene_normal_line_color))
        self.flow_scene_normal_line_pen.setWidth(FlowSceneConfig.flow_scene_normal_line_width)

        # 设置粗线的笔颜色和粗细
        self.flow_scene_dark_line_pen = QPen(QColor(FlowSceneConfig.flow_scene_dark_line_color))
        self.flow_scene_dark_line_pen.setWidth(FlowSceneConfig.flow_scene_dark_line_widths)

        # 设置小格子和大格子的尺寸
        self.flow_scene_small_grid_size = FlowSceneConfig.flow_scene_small_grip_size
        self.flow_scene_big_grid_size = FlowSceneConfig.flow_scene_big_grip_size

    # 重写背景
    def drawBackground(self, painter: QPainter, rect) -> None:
        super(FlowScene, self).drawBackground(painter, rect)

        # 获得组成格子的细线和粗线数组
        normal_lines, dark_lines = self.get_grid_lines(rect)

        # 使用细线笔画线
        painter.setPen(self.flow_scene_normal_line_pen)
        painter.drawLines(normal_lines)

        # 使用粗线笔画线
        painter.setPen(self.flow_scene_dark_line_pen)
        painter.drawLines(dark_lines)

    # 获得组成网格的线
    def get_grid_lines(self, rect):

        normal_lines = []
        dark_lines = []

        # 获得显示区域矩形的上下左右
        left = math.floor(rect.left())
        right= math.floor(rect.right())
        top = math.floor(rect.top())
        bottom = math.floor(rect.bottom())

        # print(rect)
        # print(left, right, top, bottom)

        # 第一个网格的起始位置
        first_left = left - (left % self.flow_scene_small_grid_size)
        first_top = top - (top % self.flow_scene_small_grid_size)

        # 横线
        for v in range(first_top, bottom,self.flow_scene_small_grid_size):
            line = QLine(left, v, right, v)

            # 当到达可组成大格子时，粗线
            if v % (self.flow_scene_small_grid_size * self.flow_scene_small_grid_size) == 0:
                dark_lines.append(line)
            else:
                normal_lines.append(line)

        # 竖线
        for h in range(first_left, right, self.flow_scene_small_grid_size):
            line =QLine(h, top, h, bottom)

            # 当到达可组成大格子时，粗线
            if h % (self.flow_scene_small_grid_size * self.flow_scene_small_grid_size) == 0:
                dark_lines.append(line)
            else:
                normal_lines.append(line)

        return normal_lines, dark_lines











