import rasterio
import numpy as np
import os

output_dir = 'resultados_indices'

path_blue = r'C:\Users\Usuario\Downloads\Proyecto maiz\Browser_images\2024-10-03-00_00_2024-10-03-23_59_Sentinel-2_L2A_B02_(Raw).tiff'
path_green = r'C:\Users\Usuario\Downloads\Proyecto maiz\Browser_images\2024-10-03-00_00_2024-10-03-23_59_Sentinel-2_L2A_B03_(Raw).tiff'
path_red = r'C:\Users\Usuario\Downloads\Proyecto maiz\Browser_images\2024-10-03-00_00_2024-10-03-23_59_Sentinel-2_L2A_B04_(Raw).tiff'
path_red_edge = r'C:\Users\Usuario\Downloads\Proyecto maiz\Browser_images\2024-10-03-00_00_2024-10-03-23_59_Sentinel-2_L2A_B05_(Raw).tiff'
path_nir = r'C:\Users\Usuario\Downloads\Proyecto maiz\Browser_images\2024-10-03-00_00_2024-10-03-23_59_Sentinel-2_L2A_B08_(Raw).tiff'       

# ÍNDICES DE VEGETACIÓN
def calculate_ndvi(nir_band, red_band):
    """Calcula el NDVI. Se usa en múltiples etapas."""
    # NDVI = (NIR - RED) / (NIR + RED)
    ndvi = (nir_band - red_band) / (nir_band + red_band)
    return ndvi

def calculate_msavi2(nir_band, red_band):
    """Calcula el MSAVI2 para la etapa de Emergencia."""
    msavi2 = (2 * nir_band + 1 - np.sqrt((2 * nir_band + 1)**2 - 8 * (nir_band - red_band))) / 2
    return msavi2

def calculate_gndvi(nir_band, green_band):
    """Calcula el GNDVI para la etapa de Crecimiento Vegetativo."""
    # GNDVI = (NIR - Green) / (NIR + Green)
    gndvi = (nir_band - green_band) / (nir_band + green_band)
    return gndvi

def calculate_evi(nir_band, red_band, blue_band):
    """Calcula el EVI, usado en Pre-floración, Floración y Llenado."""
    # EVI = G * ((NIR - RED) / (NIR + C1 * RED - C2 * BLUE + L))
    G = 2.5
    C1 = 6.0
    C2 = 7.5
    L = 1.0
    evi = G * ((nir_band - red_band) / (nir_band + C1 * red_band - C2 * blue_band + L))
    return evi

def calculate_kndvi(nir_band, red_band):
    """Calcula el kNDVI para la etapa de Pre-floración."""
    # kNDVI = tanh(((NIR - RED) / (2 * sigma))^2)
    sigma = 0.5 * (nir_band + red_band)

    num = 1 - np.exp(-((nir_band - red_band)**2) / (2 * sigma**2))
    den = 1 - np.exp(-((nir_band + red_band)**2) / (2 * sigma**2))
    kndvi = num / den
    return kndvi

def calculate_ndre(nir_band, red_edge_band):
    """Calcula el NDRE para la etapa de Floración."""
    # NDRE = (NIR - RE) / (NIR + RE)
    ndre = (nir_band - red_edge_band) / (nir_band + red_edge_band)
    return ndre



def main():
    """
    Función principal que lee las bandas, calcula todos los índices
    y guarda los resultados en archivos GeoTIFF.
    """
    print("Iniciando el cálculo de índices de vegetación para el maíz...")


    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Directorio de salida creado en: {output_dir}")


    bands = {}
    paths = {
        'blue': path_blue, 'green': path_green, 'red': path_red,
        'red_edge': path_red_edge, 'nir': path_nir
    }

    meta = None
    try:
        for band_name, band_path in paths.items():
            if os.path.exists(band_path):
                with rasterio.open(band_path) as src:
                
                    if meta is None:
                        meta = src.meta
                    
                    bands[band_name] = src.read(1).astype('float64')
                print(f"Banda '{band_name}' cargada exitosamente.")
            else:
                print(f"Advertencia: No se encontró el archivo para la banda '{band_name}' en la ruta: {band_path}")
                bands[band_name] = None
    except Exception as e:
        print(f"Error fatal al leer los archivos de las bandas: {e}")
        return

    
    def save_output(data, index_name):
        if data is None or np.all(np.isnan(data)):
            print(f"No se pudo calcular '{index_name}' por falta de bandas o error en el cálculo.")
            return

        output_path = os.path.join(output_dir, f'{index_name}.tif')
        profile = meta.copy()
        profile.update(dtype=rasterio.float64, count=1, compress='lzw')

        with rasterio.open(output_path, 'w', **profile) as dst:
            dst.write(data.astype(rasterio.float64), 1)
        print(f"-> Índice '{index_name}' calculado y guardado en: {output_path}")


    np.seterr(divide='ignore', invalid='ignore') 

    # Etapa 1: Emergencia
    if bands.get('nir') is not None and bands.get('red') is not None:
        msavi2_result = calculate_msavi2(bands['nir'], bands['red'])
        save_output(msavi2_result, 'MSAVI2_Emergencia')

    # Etapa 2: Crecimiento Vegetativo
    if bands.get('nir') is not None and bands.get('green') is not None:
        gndvi_result = calculate_gndvi(bands['nir'], bands['green'])
        save_output(gndvi_result, 'GNDVI_Crecimiento')
    if bands.get('nir') is not None and bands.get('red') is not None:
        
        ndvi_result = calculate_ndvi(bands['nir'], bands['red'])
        save_output(ndvi_result, 'NDVI_General') 

    # Etapa 3: Pre-floración
    if bands.get('nir') is not None and bands.get('red') is not None and bands.get('blue') is not None:
        evi_result = calculate_evi(bands['nir'], bands['red'], bands['blue'])
        save_output(evi_result, 'EVI_General') # También se usa en varias etapas
    if bands.get('nir') is not None and bands.get('red') is not None:
        kndvi_result = calculate_kndvi(bands['nir'], bands['red'])
        save_output(kndvi_result, 'kNDVI_PreFloracion')

    # Etapa 4: Floración
    if bands.get('nir') is not None and bands.get('red_edge') is not None:
        ndre_result = calculate_ndre(bands['nir'], bands['red_edge'])
        save_output(ndre_result, 'NDRE_Floracion')

    print("\n¡Proceso finalizado!")


if __name__ == '__main__':
    main()