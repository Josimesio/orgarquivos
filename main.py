import os
import shutil
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtGui import QIcon
from ui_main import Ui_MainWindow
import sys   
   
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("PYTAX - Organizador de arquivos")
        appIcon = QIcon(":/icons/_imgs/folder.png")
        self.setWindowIcon(appIcon)

        self.btn_open.clicked.connect(self.open_path)
        self.btn_organize.clicked.connect(self.organizer)

    def open_path(self):
        self.path = QFileDialog.getExistingDirectory(
            self, 'Pasta com arquivos', '/home',
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks
        )
        self.txt_path.setText(self.path)
        self.path = str(self.path)

    def organizer(self):
        if not self.path:
            QMessageBox.warning(self, "Atenção", "Por favor, selecione uma pasta antes de organizar.")
            return

        try:
            files = os.listdir(self.path)
            
            for file in files:
                filename, extension = os.path.splitext(file)
                extension = extension[1:]  # remove o ponto da extensão
                if not extension:  # pula arquivos sem extensão
                    continue
                
                destination_dir = os.path.join(self.path, extension)
                
                if not os.path.exists(destination_dir):
                    os.makedirs(destination_dir)
                
                shutil.move(os.path.join(self.path, file), os.path.join(destination_dir, file))

            QMessageBox.information(self, "Sucesso", "Arquivos organizados com sucesso!")

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Ocorreu um erro: {e}")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
