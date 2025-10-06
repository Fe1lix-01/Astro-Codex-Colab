# Astro-Codex NASA

* [Página web Repositorio en GitHub](https://github.com/Fe1lix-01/Astro-Codex-Web)

---

Tool for Tracking Seasonal Cycles of Flowers

This space and aircraft instrument will use color to track the seasonal cycles of flowers. The instrument—an imaging spectrometer—mapped the landscape across hundreds of wavelengths of light, capturing flowers as they bloomed and aged over several months.

The lower panels represent the spectral footprint of each point in the image, capturing the visible range of light (blue, green, and red wavelengths) to the near-infrared (NIR) and beyond. Spatial resolution is around 16 feet (5 meters).

For many plant species, from crops to cacti, flowering is synchronized with seasonal changes in temperature, daylight, and precipitation.

<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/00fe94c3-69d2-48de-841a-a850ce37c79b" />

<img width="1500" height="500" alt="image" src="https://github.com/user-attachments/assets/447cb4c8-e21e-4aca-96ef-455e8e0bd538" />

Key Information

Wildflower studies are typically based on ground-based observations and tools like time-lapse photography. To track flowers on a large scale, Angel and other NASA scientists look for a distinctive quality of flowers: color.

Floral pigments are divided into three main groups: carotenoids and betalains (associated with yellow, orange, and red colors) and anthocyanins (responsible for many deep reds, purples, and blues). The different chemical structures of these pigments reflect and absorb light in unique patterns.

Next-Generation Airborne Instrument

The Next-Generation Airborne Visible-Infrared Imaging Spectrometer (AVIRIS-NG) has been developed to provide continuous access to imaging spectroscopy measurements with a high signal-to-noise ratio in the solar-reflected spectral range.

AVIRIS-NG measures the wavelength range from 380 nm to 2510 nm with 5 nm sampling. The spectra are measured as images with 600 cross-track elements and spatial sampling from 0.3 m to 4.0 m from a Twin Otter platform. A high-altitude platform (NASA's ER-2) will be available in the near future. AVIRIS-NG has a cross-track spectral uniformity greater than 95% and an IFOV spectral uniformity of >= 95%.

AVIRIS-NG has been calibrated and implemented with a new high-speed data acquisition system and a new real-time cloud detection algorithm to support a methane release experiment at the Department of Energy's Rocky Mountain Oilfield Test Center. This instrument's ability to detect and measure methane point sources is of interest for both greenhouse gas research and natural resource exploration, and the onboard cloud detection algorithm is applicable for future space-based imaging spectrometer missions.

FUENTES:
<https://www.jpl.nasa.gov/news/nasa-takes-to-the-air-to-study-wildflowers/>
<https://avirisng.jpl.nasa.gov/> 

**Information on Maize Phenology, Pollination, Bees, NDVI, and Beekeepers**

**1.1 Maize Phenology**
Maize phenology describes the stages from sowing to physiological maturity. The duration and timing of each stage are strongly influenced by temperature and, in some hybrids, by photoperiod. Accurately detecting the flowering phase is critical because it defines the pollination window and determines yield potential.

Maize phenology outlines the morphological and physiological stages of development, divided into two main phases:

Vegetative (V): The plant focuses on leaf and root growth.

Reproductive (R): Encompasses flowering, pollination, ear formation, grain filling, and maturation.

Simplified Maize Phenological Stages (for website display)

Emergence – Establishment (V0–V2): The seed germinates, and the seedling emerges.
• Website label: “Emergence”

Vegetative Growth – Leaf Development (V3): Stem and leaf development, biomass accumulation.
• Website label: “Vegetative Growth”

Pre-Flowering / Tassel Development: Beginning of reproductive structure formation (male tassel on top).
• Website label: “Pre-Flowering”

Flowering – Pollination (R1: Tasseling & Silking): The tassel releases pollen while silks (stigmas) appear.
Ideally, tasseling and silking occur synchronously so that when pollen is available, the silks are ready to receive it.
• Most critical phase of the cycle (for both yield and bees).
• Website label: “Flowering”

Grain Filling (R2–R5): Grains develop and fill with starch.
• Website label: “Grain Filling”

Physiological Maturity – Senescence (R6): The plant dries, and leaves lose their green color.
• Website label: “Maturity / Senescence”

Visual tags with icons and colors:
• Light green → Emergence
• Dark green → Vegetative
• Yellow → Flowering
• Orange → Grain filling
• Brown → Senescence

**1.2 Polinización del maíz y papel de las abejas**

El maíz es principalmente anemófilo (polinización por viento), pero numerosos estudios y
observaciones indican que insectos como las abejas melíferas y otros polinizadores colectan polen
de maíz y pueden contribuir al transporte de granos de polen, especialmente en sistemas agrícolas
heterogéneos o en bordes de cultivo.

Una sola planta de maíz puede producir de 2 a 5 millones de granos de polen. La variabilidad
natural del campo hace que la liberación de polen se produzca en un período de 10 a 14 días. El
pico de liberación de polen suele ocurrir a media mañana, pero una antera húmeda no lo liberará.
El clima más fresco, nublado o húmedo retrasa la liberación de polen, y no se produce durante la
lluvia. El polen puede viajar más de 152 metros, pero la mayor parte del polen liberado solo se
desplaza entre 6 y 15 metros.

**Implicaciones para apicultores:**

• El calendario de floración del maíz informa cuándo la disponibilidad de polen aumenta:
útil para planificar colmenas, alimentación suplementaria y movimientos trashumantes
(práctica de mover colmenas de abejas de un lugar a otro según la disponibilidad de
floraciones o recursos).
• Monitoreo de floraciones cercanas permite reducir conflictos (por ejemplo, la exposición
a pesticidas durante floración) y optimizar la ubicación de colmenas.


**1.2 NDVI y detección remota de eventos de floración**
NDVI acomodado a la primera etapa fenológica del maíz
• Modified Soil-Adjusted Vegetation Index 2 (MSAVI2).
Es una mejora del SAVI (Soil Adjusted Vegetation Index). Fue diseñado para reducir el efecto del
suelo expuesto en el cálculo de la vegetación, algo muy importante en cultivos como el maíz
durante sus primeras etapas (V2–V6), cuando aún no hay mucho follaje.
Calcula el índice de vegetación ajustado al suelo modificado (MSAVI2) a partir de un objeto ráster
multibanda y devuelve un objeto ráster con los valores del índice.
Emergencia – (V0-V2)- Verde claro
MSAV12 =
2 ∗ 𝑁𝐼𝑅 + 1 − √(2 ∗ 𝑁𝐼𝑅 + 1)
2 − 8(𝑁𝐼𝑅 + 𝑅𝑒𝑑)
2
• NIR = valores de píxel de la banda infrarroja cercana
• Rojo = valores de píxel de la banda roja
Si usa una lista delimitada por espacios, identificará las bandas NIR y roja en el siguiente orden:
NIR=4 y Roja=3.
Valores típicos de MSAVI2
• 0.1–0.3 → etapa muy temprana, baja biomasa.
• 0.3–0.5 → rápido crecimiento, cierre parcial de dosel.
• 0.5–0.7 → crecimiento vigoroso (similar a NDVI medio).
• >0.7 → dosel cerrado, similar al máximo de NDVI.
Dosel abierto/parcial: Significa que la vegetación no cubre completamente el suelo y este puede
verse desde arriba. Corresponde a las etapas iniciales o de rápido crecimiento.
Dosel cerrado: Implica que la vegetación forma una capa continua y densa que cubre
completamente el suelo, dificultando o impidiendo la visión de este. Esto se asocia con la biomasa
máxima o la madurez del cultivo/vegetación.
NDVI acomodado a la segunda etapa fenológica del maíz
• Green Normalized Difference Vegetation Index (GNDVI)
El método Índice de vegetación de diferencia normalizada verde (GNDVI) se emplea para realizar
estimaciones de la actividad fotosintética y es un índice de vegetación empleado comúnmente para
determinar el consumo de agua y nitrógeno de la cubierta vegetal.
Se diferencia del popular NDVI en las bandas espectrales que utiliza, lo que le confiere una mayor
sensibilidad al contenido de clorofila. La clorofila de las plantas absorbe fuertemente la luz roja,
pero refleja una porción de la luz verde.
Crecimiento vegetativo – Desarrollo de hojas (V3)-Verde intenso
𝐺𝑁𝐷𝑉𝐼 =
(𝑁𝐼𝑅 − 𝐺𝑟𝑒𝑒𝑛)
(𝑁𝐼𝑅 + 𝐺𝑟𝑒𝑒𝑛)
El GNDVI se basa en la forma en que la vegetación sana refleja la luz en diferentes longitudes de
onda, especialmente la luz verde y la infrarroja cercana (NIR).
• NIR = valores de píxel de la banda infrarroja cercana
• Verde = valores de píxel de la banda verde
• ID de banda NIR: El índice de identificación utiliza indexación basada en uno. (El valor
predeterminado es 5)
• ID de banda verde: El índice de ID utiliza indexación basada en uno. (El valor
predeterminado es 2)
• Normalized Difference Vegetation Index (NDVI)
Es el índice de vegetación más común y fundamental en la teledetección. Es un indicador simple
pero eficaz de la cantidad, densidad y salud del follaje verde o la biomasa fotosintéticamente
activa.
Crecimiento vegetativo – Desarrollo de hojas (V3)-Verde intenso
𝑁𝐷𝑉𝐼 =
(𝑁𝐼𝑅 − 𝑅𝐸𝐷)
(𝑁𝐼𝑅 + 𝑅𝐸𝐷)
• NIR = valores de píxel de la banda infrarroja cercana
• RED = valores de píxel de la banda roja
El NDVI siempre varía en un rango de -1 a +1. La interpretación de este rango es clave para
evaluar la cobertura y el estado de la superficie, para el NDVI del maíz sube a 0.6–0.8.
NDVI acomodado a la tercera etapa fenológica del maíz
• Enhanced Vegetation Index (EVI)
Diseñado específicamente para optimizar la señal de la vegetación en regiones con alta densidad
de biomasa y para reducir las interferencias atmosféricas y del fondo del suelo. Es más sensible a
las variaciones en la estructura del dosel.
Pre-floración / Desarrollo de panoja- Amarillo - floración masculina
𝐸𝑉𝐼 = 𝐺(
(𝑁𝐼𝑅 − 𝑅𝐸𝐷)
(𝑁𝐼𝑅 + 𝐶1)𝑅𝐸𝐷 − 𝐶2(𝐵𝐿𝑈𝐸 + 𝐿)
• NIR, RED, BLUE: Son los valores de reflectancia de la superficie en las bandas Infrarrojo
Cercano, Roja y Azul, respectivamente.
• L (Canopy Background Adjustment): Es un factor de ajuste del dosel/fondo del suelo
(típicamente 1), que ayuda a mitigar la influencia del suelo expuesto, especialmente en
áreas de vegetación escasa.
• C1 y C2 (Atmospheric Resistance Coefficients): Son coeficientes para la resistencia
atmosférica (típicamente C1=6 y C2=7.5), que utilizan la banda azul para corregir los
efectos de los aerosoles atmosféricos.
• G (Gain Factor): Es un factor de ganancia o escala (típicamente 2.5).
Al igual que el NDVI, el EVI varía entre −1 y 1.
• Kernel Normalized Difference Vegetation Index (KNDVI)
Es un índice de vegetación avanzado que utiliza una técnica de aprendizaje automático conocida
como funciones kernel para mejorar el rendimiento del índice NDVI tradicional.
El kNDVI busca superar las limitaciones del NDVI (como la saturación en alta biomasa) al
introducir una transformación no lineal de los datos espectrales (NIR y RED), capturando así
relaciones más complejas entre estas bandas que los índices lineales no pueden.
Pre-floración / Desarrollo de panoja- Amarillo - floración masculina
KNDVI =
1 − 𝑒
−
(𝑁𝐼𝑅−𝑅𝐸𝐷)
2
2𝜎2
1 − 𝑒
−
(𝑁𝐼𝑅+𝑅𝐸𝐷)
2
2𝜎2
• NIR y RED: Son los valores de reflectancia de la superficie en el Infrarrojo Cercano y
Rojo, respectivamente.
• σ (Sigma): Es un parámetro de escala o longitud de onda del kernel, esencial para el
índice. Este valor debe estimarse a partir de los datos, típicamente utilizando la distancia
promedio entre los píxeles NIR y RED de la región de interés. Un valor común sugerido
es σ=0.5×(NIR+RED), que actúa como una aproximación del albedo del píxel.
• Normalized Difference Vegetation Index (NDVI)
Pre-floración / Desarrollo de panoja- Amarillo - floración masculina
𝑁𝐷𝑉𝐼 =
(𝑁𝐼𝑅 − 𝑅𝐸𝐷)
(𝑁𝐼𝑅 + 𝑅𝐸𝐷)
NDVI acomodado a la cuarta etapa fenológica del maíz
• Normalized Difference Red Edge (NDRE)
Es un índice de vegetación fundamental en la agricultura de precisión y la teledetección avanzada.
Es una variante del NDVI, pero utiliza una banda espectral diferente y crucial para el monitoreo
de la salud vegetal: la banda del Borde Rojo (Red Edge).
Floración – Polinización (R1: tasseling & silking) Amarillo - floración fememina
𝑁𝐷𝑅𝐸 =
(𝑁𝐼𝑅 − 𝑅𝐸)
(𝑁𝐼𝑅 + 𝑅𝐸)
• NIR (Infrarrojo Cercano): Rango de longitudes de onda donde la vegetación sana tiene una
alta reflectancia (aprox. 770 - 860 nm).
• RE (Borde Rojo): Es una banda estrecha que se ubica en la transición entre la luz roja
visible y el infrarrojo cercano (aprox. 680 - 750 nm). Es la zona donde la reflectancia de la
vegetación aumenta drásticamente.
El resultado es un valor acotado entre −1 y 1, donde los valores más altos indican una vegetación
más sana y con alto contenido de clorofila.
• Enhanced Vegetation Index (EVI)
Floración – Polinización (R1: tasseling & silking) Amarillo - floración fememina
𝐸𝑉𝐼 = 𝐺(
(𝑁𝐼𝑅 − 𝑅𝐸𝐷)
(𝑁𝐼𝑅 + 𝐶1)𝑅𝐸𝐷 − 𝐶2(𝐵𝐿𝑈𝐸 + 𝐿)
• Normalized Difference Vegetation Index (NDVI)
Floración – Polinización (R1: tasseling & silking) Amarillo - floración fememina
𝑁𝐷𝑉𝐼 =
(𝑁𝐼𝑅 − 𝑅𝐸𝐷)
(𝑁𝐼𝑅 + 𝑅𝐸𝐷)
NDVI acomodado a la quinta etapa fenológica del maíz
• Normalized Difference Vegetation Index (NDVI)
Llenado de grano (R2–R5)- Naranja
𝑁𝐷𝑉𝐼 =
(𝑁𝐼𝑅 − 𝑅𝐸𝐷)
(𝑁𝐼𝑅 + 𝑅𝐸𝐷)
• Enhanced Vegetation Index (EVI)
Llenado de grano (R2–R5)- Naranja
𝐸𝑉𝐼 = 𝐺(
(𝑁𝐼𝑅 − 𝑅𝐸𝐷)
(𝑁𝐼𝑅 + 𝐶1)𝑅𝐸𝐷 − 𝐶2(𝐵𝐿𝑈𝐸 + 𝐿)
NDVI acomodado a la sexta etapa fenológica del maíz
• Normalized Difference Vegetation Index (NDVI)
Madurez fisiológica – Senescencia (R6)- Marrón
𝑁𝐷𝑉𝐼 =
(𝑁𝐼𝑅 − 𝑅𝐸𝐷)
(𝑁𝐼𝑅 + 𝑅𝐸𝐷)
REFERENCIAS DE FORMULAS
• https://pro.arcgis.com/es/pro-app/3.3/arcpy/image-analyst/msavi.htm
• https://pro.arcgis.com/es/pro-app/3.3/arcpy/image-analyst/gnvdi.htm


# Polen dispersion simulation

One of the big difficulties identified in this challenge was the ability to track down pollen particles, as it is currently not possible to identify them from satellite data and differenciate it from other aerosols. Therefore an innovative approach was needed. Our proposed methodology consists of **four steps** to carry out the simulation. One advantage of this approach, will be the ability to distinguish pollen originating from different sources.

### Step 1: Crop Detection

A combination of data will be used to reliably identify the location of **corn, wheat, agave,** or **bean** crops.  
With **Sentinel-1 SAR**, it will be possible to detect crops in areas with high cloud coverage (for example, *Chiapas*).  
This will be combined with the **optical instruments of Sentinel-2** to detect them through temporal analysis of vegetation indices.  

Additionally, there is the possibility of detecting them using **spectral signatures** from **Landsat, EMIT,** and **MODIS**.  
Auxiliary data will also be added to more easily delineate the zones.  

Using **elevation models**, we will discard areas that are too high or steep for certain types of crops.  
With **historical climate data** (temperature, precipitation, and humidity), we can delimit areas where planting specific crops is feasible.  
Furthermore, **agricultural census data** will be used for model validation and sampling.

---

### Step 2: Flowering Detection


<img width="574" height="369" alt="image" src="https://github.com/user-attachments/assets/8b81d056-844b-49d7-94b5-1e018f0db83d" />


<img width="781" height="335" alt="image" src="https://github.com/user-attachments/assets/7118ea46-19ab-4914-8ffb-46be6ef39af0" />

### Step 2: Flowering Detection

To detect flowering, the methodology proposed by **Angel Y., Raihno A., Kathuria D., et al.** will be adapted.  
This approach will be used to detect flowering events of **bean, corn, wheat,** and **agave** crops using the **multispectral sensor of Sentinel-2**.

---

### Step 3: Simulation

To simulate **pollen dispersion**, the initial parameters will include:
- The **location and extent** of flowering events detected by multispectral sensors  
- **Historical and forecasted climate data** from **ERA5** or **MERRA-2**  

The **HYSPLIT** model/tool will be used to perform the simulation.

---

### Step 4: Visualization

The results will be represented on a **map**, using a **color gradient** based on the predicted **pollen density**.


<img width="702" height="468" alt="image" src="https://github.com/user-attachments/assets/66e14c13-4603-4bb2-8534-df8fff8cda45" />

<img width="730" height="430" alt="image" src="https://github.com/user-attachments/assets/ab2d4c07-7718-4363-ae05-6c5434594560" />


---

* [Team Roles](TeamInfo)
* [Página web Repositorio en GitHub](https://github.com/Fe1lix-01/Astro-Codex-Project)
* [Prototipo en Figma](https://www.figma.com/site/WVLBzxRr8Yb6DWZpjeD0M7/Untitled?node-id=63-316&t=Ns9aMdjGTmc2HcsG-1)




