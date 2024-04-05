class LoggerMixin:
    def log(self, message):
        print(f"[LOG] {message}")

class DatabaseManager:
    def save_data(self, data):
        # Guardar datos en la base de datos
        self.log("Datos guardados exitosamente")

class FileManager:
    def save_file(self, file):
        # Guardar archivo en el sistema de archivos
        self.log("Archivo guardado exitosamente")

class DataManager(DatabaseManager, LoggerMixin):
    pass

class FileManagerWithLogging(FileManager, LoggerMixin):
    pass

data_manager = DataManager()
data_manager.save_data("Datos de ejemplo")

file_manager = FileManagerWithLogging()
file_manager.save_file("archivo.txt")