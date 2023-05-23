#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author wuhongyu
    @Date 2023/5/7 10:42 AM
    @Describe 
    @Version 1.0
"""
import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QBoxLayout
from flow_view import FlowView
from flow_scene import FlowScene
from flow_configs import FlowMianConfig


class FlowMain(QWidget):
    def __init__(self):
        super(FlowMain, self).__init__()
        self.setup()

    def setup(self):
        self.setWindowTitle("flow")
        self.resize(FlowMianConfig.flow_main_width, FlowMianConfig.flow_mian_height)
        scene = FlowScene(self)
        view = FlowView(scene, self)

        layout = QBoxLayout(QBoxLayout.BottomToTop)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.addWidget(view)
        self.setLayout(layout)

        self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    flow = FlowMain()
    app.exec()
