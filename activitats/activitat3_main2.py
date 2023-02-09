import sys, os
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()
app = QtWidgets.QApplication(sys.argv)
ui_path = os.path.join(os.path.dirname(__file__), "Activitat 1 - Apartat 2 - formulari de text I.ui")
window = loader.load(ui_path, None)
window.show()
app.exec()
