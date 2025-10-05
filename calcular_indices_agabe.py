import rasterio
import numpy as np
import os

output_dir = 'resultados_agave'


path_red = r'C:\Ruta\a\tu\banda_roja_B04.tif'
path_nir = r'C:\Ruta\a\tu\banda_nir_B08.tif'

path_red_edge = r'C:\Ruta\a\tu\banda_red_edge_B05.tif'
path_swir = r'C:\Ruta\a\tu\banda_swir_B11.tif'

def calculate_savi(nir_band, red_band):
    """Calcula SAVI para la etapa de Establecimiento del agave."""
    # SAVI = ((NIR - Red) / (NIR + Red + L)) * (1 + L)
    L = 0.5
    savi = ((nir_band - red_band) / (nir_band + red_band + L)) * (1 + L)
    return savi

def calculate_ndvi(nir_band, red_band):
    """Calcula NDVI para la etapa de Crecimiento y Desarrollo del agave."""
    # NDVI = (NIR - Red) / (NIR + Red)
    ndvi = (nir_band - red_band) / (nir_band + red_band)
    return ndvi

def calculate_ndre(nir_band, red_edge_band):
    """Calcula NDRE para la etapa de Maduración (salud y clorofila)."""
    # NDRE = (NIR - Red Edge) / (NIR + Red Edge)
    ndre = (nir_band - red_edge_band) / (nir_band + red_edge_band)
    return ndre

def calculate_ndmi(nir_band, swir_band):
    """Calcula NDMI para la etapa de Maduración (estrés hídrico)."""
    # NDMI = (NIR - SWIR) / (NIR + SWIR)
    ndmi = (nir_band - swir_band) / (nir_band + swir_band)
    return ndmi

def main():
    print("Iniciando el cálculo de índices de vegetación para el AGAVE...")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    bands = {}
    paths = {
        'red': path_red, 'nir': path_nir,
        'red_edge': path_red_edge, 'swir': path_swir
    }
    meta = None
    
    
    for band_name, band_path in paths.items():
        if band_path and os.path.exists(band_path):
            try:
                with rasterio.open(band_path) as src:
                    if meta is None:
                        meta = src.meta
                    bands[band_name] = src.read(1).astype('float64')
                    print(f"Banda '{band_name}' cargada.")
            except Exception as e:
                print(f"Error al leer la banda '{band_name}': {e}")
                bands[band_name] = None
        else:
            bands[band_name] = None
            if band_path:
                print(f"Advertencia: No se encontró el archivo para la banda '{band_name}'.")

    
    def save_output(data, index_name):
        if meta is None:
            print("Error fatal: No se pudieron cargar los metadatos. Revisa que al menos una ruta sea correcta.")
            return

        if data is None:
            print(f"Cálculo de '{index_name}' omitido por falta de bandas necesarias.")
            return
        
        if np.all(np.isnan(data)):
            print(f"Advertencia: El resultado de '{index_name}' es inválido (posiblemente toda la imagen es 'sin datos'). No se guardará el archivo.")
            return
            
        output_path = os.path.join(output_dir, f'{index_name}.tif')
        profile = meta.copy()
        profile.update(dtype=rasterio.float64, count=1)
        
        with rasterio.open(output_path, 'w', **profile) as dst:
            dst.write(data.astype(rasterio.float64), 1)
        print(f"-> ¡Éxito! Índice '{index_name}' guardado en: {output_path}")

    np.seterr(divide='ignore', invalid='ignore')

    # --- ETAPA 1: ESTABLECIMIENTO (0-12 MESES) ---
    if bands.get('nir') is not None and bands.get('red') is not None:
        savi_result = calculate_savi(bands['nir'], bands['red'])
        save_output(savi_result, 'SAVI_Establecimiento_Agave')

    # --- ETAPA 2: CRECIMIENTO Y DESARROLLO (1-4 AÑOS) ---
    if bands.get('nir') is not None and bands.get('red') is not None:
        ndvi_result = calculate_ndvi(bands['nir'], bands['red'])
        save_output(ndvi_result, 'NDVI_Crecimiento_Agave')

    # --- ETAPA 3: MADURACIÓN (4-7 AÑOS) ---
    if bands.get('nir') is not None and bands.get('red_edge') is not None:
        ndre_result = calculate_ndre(bands['nir'], bands['red_edge'])
        save_output(ndre_result, 'NDRE_Maduracion_Agave')
    if bands.get('nir') is not None and bands.get('swir') is not None:
        ndmi_result = calculate_ndmi(bands['nir'], bands['swir'])
        save_output(ndmi_result, 'NDMI_Maduracion_Agave')
        
    print("\n¡Proceso para Agave finalizado!")

if __name__ == '__main__':
    main()