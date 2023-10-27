import os
import shutil

source_folder = 'D:'

destination_folder = 'D:'

for filename in os.listdir(source_folder):
    source_file = os.path.join(source_folder, filename)

    if os.path.isfile(source_file):
        # Estrai il nome del file (senza estensione)
        file_name, file_extension = os.path.splitext(filename)
        
        # Crea una sottocartella con il nome del file (se non esiste già)
        target_folder = os.path.join(destination_folder, file_name)
        os.makedirs(target_folder, exist_ok=True)
        
        # Sposta il file nella sottocartella
        shutil.move(source_file, os.path.join(target_folder, filename))

print('Operazione completata.')
