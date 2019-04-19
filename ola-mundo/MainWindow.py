#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python e PyQt5.

Acessando/interagindo com um arquivo ``*.ui`` (XML).
"""
from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi


class MeuAplicativo:
    """Classe."""

    def __init__(self, window):
        """Construtor."""
        # Widgets
        self.label = window.label
        self.line_edit = window.lineEdit
        self.push_button = window.pushButton
        # Conectando um método ao evento de clique do botão.
        self.push_button.clicked.connect(self._on_button_clicked)

    def _on_button_clicked(self):
        """Método é executado quando o botão é pressionado."""
        # Coletando o valor do campo de entrada de texto.
        text = self.line_edit.text()
        # Verificando se algo foi digitado.
        if text:
            self.label.setText(text)
        else:
            self.label.setText('Digite algo no campo de texto :)')


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    # Lendo o arquivo de interface.
    # window = loadUi('forms/mainwindow-creator.ui')
    window = loadUi('forms/mainwindow-designer.ui')
    ui = MeuAplicativo(window=window)
    window.show()
    sys.exit(app.exec_())
