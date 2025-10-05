import rasterio
import numpy as np
import os

output_dir = 'resultados_indices_trigo'


path_blue = r'C:\Users\Usuario\Downloads\TrigoSonora\2024-10-02-00_00_2024-10-02-23_59_Sentinel-2_L2A_B02_(Raw).tiff'
path_green = r'C:\Users\Usuario\Downloads\TrigoSonora\2024-10-03-00_00_2024-10-03-23_59_Sentinel-2_L2A_B03_(Raw).tiff'
path_red = r'C:\Users\Usuario\Downloads\TrigoSonora\2024-10-03-00_00_2024-10-03-23_59_Sentinel-2_L2A_B04_(Raw).tiff'

path_red_edge = r'C:\Users\Usuario\Downloads\TrigoSonora\2024-10-03-00_00_2024-10-03-23_59_Sentinel-2_L2A_B05_(Raw).tiff' 
path_nir = r'C:\Users\Usuario\Downloads\TrigoSonora\2024-10-03-00_00_2024-10-03-23_59_Sentinel-2_L2A_B08_(Raw).tiff' 
path_swir = r''     

def calculate_savi(nir_band, red_band):
    """Calcula SAVI para la fase de Establecimiento del trigo."""
    L = 0.5
    savi = ((nir_band - red_band) / (nir_band + red_band + L)) * (1 + L)
    return savi

def calculate_ndre(nir_band, red_edge_band):
    """Calcula NDRE para la fase de Crecimiento del trigo."""
    ndre = (nir_band - red_edge_band) / (nir_band + red_edge_band)
    return ndre

def calculate_evi(nir_band, red_band, blue_band):
    """Calcula EVI para la fase de Crecimiento (alternativa)."""
    G, C1, C2, L_evi = 2.5, 6.0, 7.5, 1.0
    evi = G * ((nir_band - red_band) / (nir_band + C1 * red_band - C2 * blue_band + L_evi))
    return evi

def calculate_ndmi(nir_band, swir_band):
    """Calcula NDMI para la fase de Llenado de Grano del trigo."""
    ndmi = (nir_band - swir_band) / (nir_band + swir_band)
    return ndmi


def main():
    print("Iniciando el cálculo de índices de vegetación para el TRIGO...")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    bands = {}
    paths = {
        'blue': path_blue, 'green': path_green, 'red': path_red,
        'red_edge': path_red_edge, 'nir': path_nir, 'swir': path_swir
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
            print("Error fatal: No se pudieron cargar los metadatos de ninguna banda. Revisa las rutas.")
            return

        if data is None or np.all(np.isnan(data)):
            print(f"No se pudo calcular '{index_name}' por falta de datos en las bandas.")
            return
            
        output_path = os.path.join(output_dir, f'{index_name}.tif')
        profile = meta.copy()
        profile.update(dtype=rasterio.float64, count=1)
        
        with rasterio.open(output_path, 'w', **profile) as dst:
            dst.write(data.astype(rasterio.float64), 1)
        print(f"-> Índice '{index_name}' guardado en: {output_path}")

    np.seterr(divide='ignore', invalid='ignore')

    # --- FASE 1: ESTABLECIMIENTO ---
    if bands.get('nir') is not None and bands.get('red') is not None:
        savi_result = calculate_savi(bands['nir'], bands['red'])
        save_output(savi_result, 'SAVI_Establecimiento_Trigo')

    # --- FASE 2: CRECIMIENTO ---
    if bands.get('nir') is not None and bands.get('red_edge') is not None:
        ndre_result = calculate_ndre(bands['nir'], bands['red_edge'])
        save_output(ndre_result, 'NDRE_Crecimiento_Trigo')
    if bands.get('nir') is not None and bands.get('red') is not None and bands.get('blue') is not None:
        evi_result = calculate_evi(bands['nir'], bands['red'], bands['blue'])
        save_output(evi_result, 'EVI_Crecimiento_Trigo')

    # --- FASE 3: LLENADO DE GRANO ---
    if bands.get('nir') is not None and bands.get('swir') is not None:
        ndmi_result = calculate_ndmi(bands['nir'], bands['swir'])
        save_output(ndmi_result, 'NDMI_Llenado_Trigo')
        
    print("\n¡Proceso para Trigo finalizado!")

if __name__ == '__main__':
    main()