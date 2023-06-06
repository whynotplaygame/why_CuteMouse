#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author wuhongyu
    @Date 2023/5/7 11:38 PM
    @Describe 
    @Version 1.0
"""
from PySide6.QtWidgets import QGraphicsItem,QGraphicsRectItem
from PySide6.QtCore import QRectF,QPointF,QLine, Qt
from PySide6.QtGui import QBrush, QPen, QPainter, QColor, QPainterPath


class FlowRectItem(QGraphicsItem):
    def __init__(self, default_rect: QRectF):
        super(FlowRectItem, self).__init__()
        self.deafultrect = default_rect
        self.setup()

    def setup(self):
        print("added a item")


    def boundingRect(self) -> QRectF:
        return QRectF(self.deafultrect.left(),
                      self.deafultrect.top(),
                      self.deafultrect.right(),
                      self.deafultrect.bottom())


    def paint(self, painter: QPainter, option, widget) -> None:
        print("draw a line")

        self.pen = QPen(QColor("#663366"))
        self.pen.setWidth(2.5)

        line = QLine(self.deafultrect.left(),self.deafultrect.top()+10,
                     self.deafultrect.right(),self.deafultrect.top()+10)

        painter.setPen(self.pen)

        # painter.drawRoundedRect(self.deafultrect,5,5)

        painter.drawLine(line)

        outline = QPainterPath()
        outline.addRoundedRect(self.deafultrect,5,5)

        # painter.setPen(Qt.NoPen)
        painter.setBrush(QColor("#339900"))
        painter.drawPath(outline.simplified())

        title_outline = QPainterPath()
        






