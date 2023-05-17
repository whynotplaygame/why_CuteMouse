#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author wuhongyu
    @Date 2023/5/7 10:42 AM
    @Describe 
    @Version 1.0
"""
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from flow_view import FlowView
from flow_scene import FlowScene
from flow_configs import FlowMianConfig


class FlowMain(QMainWindow):
    def __init__(self):
        super(FlowMain, self).__init__()
        self.setup()

    def setup(self):
        self.setWindowTitle("flow")
        self.resize(FlowMianConfig.flow_main_width, FlowMianConfig.flow_mian_height)

        self.layout = QVBoxLayout()
        scene = FlowScene()
        view = FlowView(scene)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    flow = FlowMain()
    app.exec()
