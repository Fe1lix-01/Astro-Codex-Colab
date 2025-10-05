import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt

ruta_a_la_imagen = r'C:\Users\Usuario\Downloads\TrigoSonora\2024-10-02-00_00_2024-10-02-23_59_Sentinel-2_L2A_B02_(Raw).tiff'


try:
    with rasterio.open(ruta_a_la_imagen) as src:
        print("Abriendo la imagen...")
        
        
        fig, ax = plt.subplots(1, figsize=(10, 10))
        
        
        show(src, ax=ax, cmap='gray')
        
        
        ax.set_title("Visualizador de Banda Satelital")
        plt.show()
        
        print("Cierra la ventana de la imagen para terminar.")

except Exception as e:
    print(f"Ocurrió un error: {e}")
    print("Asegúrate de que la ruta al archivo es correcta.")