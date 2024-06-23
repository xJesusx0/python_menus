### Módulo de Menús en Python

Este módulo proporciona varias funciones para imprimir menús con diferentes estilos visuales utilizando caracteres ASCII y colores ANSI en la terminal de Python.

#### Contenido del Módulo

El módulo `python-menu` incluye las siguientes funciones de menú:

- `menu1(opciones: list)`: Imprime un menú con líneas simples y encabezado y pie en rojo.
- `menu2(opciones: list)`: Imprime un menú con encabezado y pie en cian y opciones en negrita o cursiva alternadas.
- `menu3(opciones: list)`: Imprime un menú con fondo blanco y texto negro, utilizando caracteres ASCII para el diseño.
- `menu4(opciones: list)`: Imprime un menú con encabezado y pie en púrpura y opciones centradas entre líneas.
- `menu5(opciones: list)`: Imprime un menú con bordes estilo caja en azul y opciones numeradas.
- `menu6(opciones: list)`: Imprime un menú con fondo amarillo y opciones enmarcadas con líneas simples.
- `menu7(opciones: list)`: Imprime un menú con fondo verde y opciones en formato de lista vertical.
- `menu8(opciones: list)`: Imprime un menú con fondo blanco y opciones numeradas con líneas divisorias.
- `menu9(opciones: list)`: Imprime un menú con fondo cian y opciones numeradas enmarcadas con bordes.
- `menu10(opciones: list)`: Imprime un menú con fondo azul y opciones numeradas en un marco estilo ASCII.

#### Uso del Módulo

Para usar este módulo en tu script de Python, sigue estos pasos:

1. **Dirigete a tu proyecto:**
   ```bash
   cd tu_proyecto/
   ```
2. **Clona el repositorio en tu proyecto:**
   ```bash
   git clone https://github.com/xJesusx0/python_menus.git
   ```

3. **Importa las funciones de `menus.py`**:
   ```python
   from python_menus.menus import *
   # o el menu en especifico que quieras
   from python_menus.menus import menu1
   ```

4. **Define una lista de opciones que deseas mostrar en los menús**:
   ```python
   opciones = [
       'opcion 1',
       'opcion 2',
       'opcion 3',
       'opcion 4',
       'opcion 5'
   ]
   ```

5. **Llama a las funciones de menú** que desees utilizar, pasando la lista de opciones como argumento:
   ```python
   menu1(opciones)
   menu2(opciones)
   menu3(opciones)
   menu4(opciones)
   menu5(opciones)
   menu6(opciones)
   menu7(opciones)
   menu8(opciones)
   menu9(opciones)
   menu10(opciones)
   ```

6. **Configura los estilos y colores** según tus preferencias editando los diccionarios en `colors.py` o los colores de los menus en `menus.py`.

#### Ejemplo de Ejecución

El archivo `test.py` proporciona un ejemplo básico de cómo llamar y ejecutar los menús definidos en `menus.py`.

```bash
python3 python_menus/test.py
```

### Requisitos

- Python 3.x
- Terminal con soporte para códigos de escape ANSI (para colores y estilos).
