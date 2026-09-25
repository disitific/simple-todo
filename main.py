#!/usr/bin/env python3

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QFrame
)

class ToDoItemWidget(QWidget):
    def __init__(self, text, parent_list_widget, item_reference):
        super().__init__()
        self.parent_list_widget = parent_list_widget
        self.item_reference = item_reference

        self.label = QLabel(text)
        self.label.setStyleSheet("font-size: 15px;")

        self.delete_btn = QPushButton("X")
        self.delete_btn.setFixedWidth(30)
        self.delete_btn.setStyleSheet("color: red; font-weight: bold;")
        self.delete_btn.clicked.connect(self.remove_self)

        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        line.setStyleSheet("color: #e0e0e0;")

        content_layout = QHBoxLayout()
        content_layout.addWidget(self.label)
        content_layout.addWidget(self.delete_btn)
        content_layout.setContentsMargins(5, 2, 5, 2)

        main_layout = QVBoxLayout()
        main_layout.addLayout(content_layout)
        main_layout.addWidget(line)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(2)
        
        self.setLayout(main_layout)

    def remove_self(self):
        row = self.parent_list_widget.row(self.item_reference)
        self.parent_list_widget.takeItem(row)


class ToDoWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple To-Do")
        self.setFixedSize(500, 900)

        self.list_widget = QListWidget()

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Search or enter new task")
        self.input_field.textChanged.connect(self.filter_tasks)
        self.input_field.returnPressed.connect(self.add_task)
        self.input_field.setStyleSheet("font-size:20px;")

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.input_field)

        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.list_widget)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        initial_tasks = ["do this", "do that"]
        for task in initial_tasks:
            self.create_todo_item(task)

    def create_todo_item(self, text):
        item = QListWidgetItem(self.list_widget)
        row_widget = ToDoItemWidget(text, self.list_widget, item)
        item.setSizeHint(row_widget.sizeHint())
        self.list_widget.setItemWidget(item, row_widget)

    def filter_tasks(self, text):
        query = text.strip().lower()
        for i in range(self.list_widget.count()):
            item = self.list_widget.item(i)
            widget = self.list_widget.itemWidget(item)
            if widget:
                match = query in widget.label.text().lower()
                item.setHidden(not match)

    def add_task(self):
        text = self.input_field.text().strip()
        if not text:
            return

        exists = False
        for i in range(self.list_widget.count()):
            item = self.list_widget.item(i)
            widget = self.list_widget.itemWidget(item)
            if widget and widget.label.text().strip().lower() == text.lower():
                exists = True
                break

        if not exists:
            self.create_todo_item(text)
        
        self.input_field.clear()


app = QApplication(sys.argv)
window = ToDoWindow()
window.show()
sys.exit(app.exec())