# Astro-Codex NASA
Su desafío es aprovechar el poder de los datos de observación de la Tierra de la NASA para desarrollar una herramienta que monitoree y visualice eventos de floración de plantas en todo el mundo o dentro de una región local específica, y aborda directamente una necesidad específica de monitoreo de vegetación, predicción o gestión en la escala elegida.

[BloomWatch NASA](https://www.spaceappschallenge.org/2025/challenges/bloomwatch-an-earth-observation-application-for-global-flowering-phenology/?tab=details)

![BLOOMWATCH](assets/images/BloomWatch.jpg)

---

## Tareas para la semana del 18 al 21

| Tarea | Responsable | Estado |
|---|---|---|
| Diseño web en Figma | Amy | En progreso |
| Mapa con geometría y coordenadas en web | Félix | Listo |
| Imágenes de Google Earth Engine | Emanuel | Pendiente |
| Imágenes de la Nasa | Didier | Pendiente |
| Fórmulas con código para detectar polen, y fenologías | Sofi | Pendiente |
| Información sobre la fenología del Maíz | Mary | Pendiente |

---

## Tareas para la semana del 22 al 26

| Tarea | Responsable | Estado |
|---|---|---|
| Diseño web y Base de Datos | Amy | En progreso |
| Diseño de la página web y Reporte | Félix | Pendiente |
| Animaciones, Investigación y Investigación Maíz, Trigo, Frijol | Emanuel | Pendiente |
| Reporte general, Diseño, Simulaciones 3D | Didier | Pendiente |
| Dispersión del polen en las zonas | Sofi | Pendiente |
| Investigación plantas, polinización, abejas, NDVI apicultores | Mary | Pendiente |

---

## Tareas para la semana del 27 al 02

* Definir cómo detectaremos la polinización mediante imágenes
* Reunión con Rodo y Ana
* Boletos y Airbnb

---

## Herramienta que utilizaremos para el RASTREO DE CICLOS ESTACIONALES DE LAS FLORES 

Con este instrumento espacial y de aeronaves vamos a utilizar el color para rastrear los ciclos estacionales de las flores.

El instrumento —un espectrómetro de imágenes— mapeó el paisaje en cientos de longitudes de onda de luz, capturando las flores a medida que florecían y envejecían a lo largo de los meses.

Los paneles inferiores representan la huella espectral de cada punto de la imagen, capturando el rango visible de luz (longitudes de onda azul, verde y roja) hasta el infrarrojo cercano (NIR) y más allá. La resolución espacial es de alrededor de 16 pies (5 metros).

Para muchas especies de plantas, desde cultivos hasta cactus, la floración está sincronizada con los cambios estacionales de temperatura, luz diurna y precipitaciones.

<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/00fe94c3-69d2-48de-841a-a850ce37c79b" />

Por lo general, los estudios de flores silvestres se basan en observaciones desde el terreno y en herramientas como la fotografía time-lapse. 

Para rastrear las flores a gran escala, Angel y otros científicos de la NASA buscan una de las cualidades distintivas de las flores: el color.

Los pigmentos florales se dividen en tres grupos principales: carotenoides y betalaínas (asociados con los colores amarillo, naranja y rojo) y antocianinas (responsables de muchos rojos intensos, violetas y azules). Las diferentes estructuras químicas de los pigmentos reflejan y absorben la luz en patrones únicos.

<img width="1500" height="500" alt="image" src="https://github.com/user-attachments/assets/447cb4c8-e21e-4aca-96ef-455e8e0bd538" />


El espectrómetro de imágenes infrarrojas visibles aerotransportado de próxima generación (AVIRIS-NG) se ha desarrollado para proporcionar acceso continuo a mediciones de espectroscopia de imágenes con alta relación señal-ruido en el rango espectral reflejado solar. 

AVIRIS-NG mide el rango de longitud de onda de 380 nm a 2510 nm con un muestreo de 5 nm. Los espectros se miden como imágenes con 600 elementos transversales y muestreo espacial de 0,3 m a 4,0 m desde una plataforma Twin Otter. En un futuro próximo estará disponible una plataforma de gran altitud (ER-2 de la NASA). AVIRIS-NG tiene una uniformidad espectral cruzada superior al 95% y una uniformidad espectral IFOV >= del 95%.

AVIRIS-NG ha sido calibrado e implementado con un nuevo sistema de captura de datos de alta velocidad y un nuevo algoritmo de detección de nubes en tiempo real para respaldar un experimento de liberación de metano en el Centro de pruebas de campos petrolíferos de las Montañas Rocosas del Departamento de Energía. La capacidad de este instrumento para detectar y medir fuentes puntuales de metano es de interés tanto para la investigación de gases de efecto invernadero como para la exploración de recursos naturales, y el algoritmo de detección de nubes a bordo es aplicable para misiones de espectrómetros de imágenes espaciales.

FUENTES:
<https://www.jpl.nasa.gov/news/nasa-takes-to-the-air-to-study-wildflowers/>
<https://avirisng.jpl.nasa.gov/> 

**Información sobre la fenología del maíz, polinización, abejas, NDVI apicultores**

**1.1 Fenología del maíz**
La fenología del maíz describe las etapas desde siembra hasta la madurez fisiológica. La duración
y el calendario de cada etapa están fuertemente controlados por temperatura y en algunos híbridos,
por fotoperíodo. Detectar con precisión la fase de floración es crítico porque define la ventana de
polinización y es determinante del rendimiento.

La fenología del maíz describe las etapas morfológicas y fisiológicas de su desarrollo, divididas
en dos fases principales:
• Vegetativa (V): la planta se enfoca en el crecimiento de hojas y raíces.
• Reproductiva (R): abarca la floración, la polinización, la formación de la mazorca, el
llenado del grano y la maduración.

Etapas fenológicas del maíz (simplificadas para la página web)

1. Emergencia – Establecimiento (V0-V2)
Semilla germinada, plántula emergiendo.
• Etiqueta web: “Emergencia”.

3. Crecimiento vegetativo – Desarrollo de hojas (V3)
Desarrollo de tallo y hojas, acumulación de biomasa.
• Etiqueta web: “Crecimiento vegetativo”.

5. Pre-floración / Desarrollo de panoja
Inicio de formación de estructuras reproductivas (panoja masculina arriba).
• Etiqueta web: “Pre-floración”.

7. Floración – Polinización (R1: tasseling & silking)
Panoja libera polen, aparecen las sedas (estigmas).

Lo ideal es que tasseling y silking ocurran de forma sincronizada, de manera que cuando el
polen está disponible, las sedas también lo estén para recibirlo.
• Momento más crítico del ciclo (rendimiento y abejas).
• Etiqueta web: “Floración”.

9. Llenado de grano (R2–R5)
Granos creciendo y llenándose de almidón.
• Etiqueta web: “Llenado de grano”.

10. Madurez fisiológica – Senescencia (R6)
Planta seca, hojas pierden verdor.
• Etiqueta web: “Madurez / Senescencia”.

Etiquetas visuales con íconos y colores:
• Verde claro → emergencia.
• Verde intenso → vegetativo.
• Amarillo → floración.
• Naranja → llenado.
• Marrón → senescencia.

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


**Simulación de la dispersión del polen**

La metodología propuesta consta de 4 pasos para realizar la simulación, con este enfoque se podrán distinguir entre polen provenientes de distintas especies.


**Paso 1: Detección de cultivos**
Se usará una combinación de datos para identificar con confiabilidad la ubicación de cultivos de maíz, trigo, agave o frijol. Con el SAR de Sentinel-1 podremos detectar cultivos en zonas con mucha nubosidad (por ejemplo Chiapas), esto se combinará con los instrumentos ópticos de Sentinel-2 para detectarlos mediante análisis temporales de índices de vegetación. Además está la opción de detectarlos con firmas espectrales con el Sentinel-2, Landsat, EMIT y MODIS.
A esto se le añadirán datos auxiliares para delimitar las zonas con mayor facilidad. Con modelos de elevación descartaremos zonas demasiado elevadas o inclinadas para cierto tipo de cultivos. Con datos históricos del clima (temperatura, precipitación y humedad) podemos delimitar en qué zonas es factible la siembra de ciertos cultivos. Asimismo existen censos agropecuarios para la validación y muestreo de nuestro modelo.


**Paso 2: Detección de floración**
Una vez identificados los cultivos, con índices de vegetación y conocimiento sobre la fenología de los cultivos, estimar las fechas de floración.


**Paso 3: Simulación**
En base a la cantidad de cultivos, ubicación, condiciones meteorológicas y topografía del terreno se realizará la simulación estadística de la dispersión del polen.


**Paso 4: Visualización**
Esto finalmente se visualizará en el mapa.

**Detección de Cultivos**

La identificación de los cultivos desde etapas tempranas puede realizarse mediante índices de vegetación específicos. Para la detección de trigo se pueden utilizar series espectrales de NDVI como lo realizó Zhao Y., Jiang R., et. Al (2025). Pero también está la posibilidad de usar SAVI en la etapa de germinación, NDRE o NDMI durante el crecimiento. Para el maíz, el NDVI es ampliamente utilizado y ha demostrado ser adecuado. Para el agave, los índices NDWI, MSI y NDSSI son ideales por las condiciones semi-áridas en las que se da esta planta. Por último, para el frijol, NDRE, GNDVI, SAVI, NDVI son aplicables según la región. 

Adicional a la identificación por satélite, se puede incorporar información proveniente de bases de datos gubernamentales sobre la producción agrícola, como el censo agropecuario realizado en México por el INEGI. Los datos históricos del clima provenientes de ERA5 y mapas topográficos. Todo esto para decidir si hay mayor o menor probabilidad de que un cultivo detectado sea de un tipo u otro.

<img width="574" height="369" alt="image" src="https://github.com/user-attachments/assets/8b81d056-844b-49d7-94b5-1e018f0db83d" />


**Detección de floración**
<img width="781" height="335" alt="image" src="https://github.com/user-attachments/assets/7118ea46-19ab-4914-8ffb-46be6ef39af0" />


Para la detección de la floración, se propone adaptar la metodología presentada por Angel Y., Raihno A, Kathuria D., et. al. Para detectar los eventos de floración del frijol, maíz, trigo y agave con el sensor multiespectral de Sentinel-2.
Simulación
Para simular la dispersión de polen, se tomarán como parámetros iniciales la ubicación y extensión de los eventos de floración detectados con los sensores multiespectrales, los datos históricos y predicciones climáticas de ERA5 o MERRA-2. Se utilizará la herramienta/modelo HYSPLIT
Visualización
Se representará en un mapa con un gradiente de color en base a la predicción de la densidad de polen esperada.


**Visualización**

Se representará en un mapa con un gradiente de color en base a la predicción de la densidad de polen esperada.

<img width="702" height="468" alt="image" src="https://github.com/user-attachments/assets/66e14c13-4603-4bb2-8534-df8fff8cda45" />

<img width="730" height="430" alt="image" src="https://github.com/user-attachments/assets/ab2d4c07-7718-4363-ae05-6c5434594560" />







---

* [Guía para trabajar en colab desde GitHub Colab](Guia)
* [Prototipo en Figma](https://www.figma.com/site/WVLBzxRr8Yb6DWZpjeD0M7/Untitled?node-id=0-3&t=HE5KVVbup1LbzWQS-1)
* [Página web Repositorio en GitHub](https://github.com/Fe1lix-01/Astro-Codex-Web)
* [Airbnb opción](https://www.airbnb.mx/rooms/1492159875712234338?adults=6&check_in=2025-10-02&check_out=2025-10-03&guests=6&search_mode=regular_search&children=0&infants=0&pets=0&source_impression_id=p3_1758577246_P3OY-nC_hLphE8nc&previous_page_section_name=1000&federated_search_id=d4f05ba7-34b5-405b-a2e0-c346e4caaaed)



