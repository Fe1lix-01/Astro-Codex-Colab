import rasterio
import numpy as np
import os


output_dir = 'resultados_frijol'


path_red = r'C:\Ruta\a\tu\banda_roja.tif'
path_nir = r'C:\Ruta\a\tu\banda_nir.tif'
path_swir = r'C:\Ruta\a\tu\banda_swir.tif' # Banda necesaria para NDMI

def calculate_savi(nir_band, red_band):
    """Calcula SAVI para la fase Inicial del frijol."""
    # SAVI = ((NIR - Red) / (NIR + Red + L)) * (1 + L)
    L = 0.5 # Factor de corrección recomendado 
    savi = ((nir_band - red_band) / (nir_band + red_band + L)) * (1 + L)
    return savi

def calculate_ndvi(nir_band, red_band):
    """Calcula NDVI para la fase de Floración/Llenado del frijol."""
    # NDVI = (NIR - Red) / (NIR + Red)
    ndvi = (nir_band - red_band) / (nir_band + red_band)
    return ndvi

def calculate_ndmi(nir_band, swir_band):
    """Calcula NDMI para la fase de Floración/Llenado (estrés hídrico)."""
    # NDMI = (NIR - SWIR) / (NIR + SWIR)
    ndmi = (nir_band - swir_band) / (nir_band + swir_band)
    return ndmi


def main():
    print("Iniciando el cálculo de índices de vegetación para el FRIJOL...")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    bands = {}
    paths = {'red': path_red, 'nir': path_nir, 'swir': path_swir}
    meta = None

    
    for band_name, band_path in paths.items():
        if os.path.exists(band_path):
            with rasterio.open(band_path) as src:
                if meta is None: meta = src.meta
                bands[band_name] = src.read(1).astype('float64')
                print(f"Banda '{band_name}' cargada.")
        else:
            bands[band_name] = None
            print(f"Advertencia: No se encontró la banda '{band_name}'.")

    
    def save_output(data, index_name):
        if data is None or np.all(np.isnan(data)):
            print(f"No se pudo calcular '{index_name}' por falta de bandas.")
            return
        output_path = os.path.join(output_dir, f'{index_name}.tif')
        profile = meta.copy()
        profile.update(dtype=rasterio.float64, count=1)
        with rasterio.open(output_path, 'w', **profile) as dst:
            dst.write(data.astype(rasterio.float64), 1)
        print(f"-> Índice '{index_name}' guardado.")

    np.seterr(divide='ignore', invalid='ignore')

    # --- ETAPA INICIAL: EMERGENCIA A DESARROLLO ---
    if bands.get('nir') is not None and bands.get('red') is not None:
        savi_result = calculate_savi(bands['nir'], bands['red'])
        save_output(savi_result, 'SAVI_Inicial_Frijol')

    # --- ETAPA SEGUNDA: FLORACIÓN A LLENADO ---
    if bands.get('nir') is not None and bands.get('red') is not None:
        ndvi_result = calculate_ndvi(bands['nir'], bands['red'])
        save_output(ndvi_result, 'NDVI_Floracion_Frijol')
    if bands.get('nir') is not None and bands.get('swir') is not None:
        ndmi_result = calculate_ndmi(bands['nir'], bands['swir'])
        save_output(ndmi_result, 'NDMI_EstresHidrico_Frijol')
        
    print("\n¡Proceso para Frijol finalizado!")

if __name__ == '__main__':
    main()