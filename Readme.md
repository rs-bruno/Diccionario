<details>
  <summary>diccionario.es</summary>
  Repositorio para el desarrollo de herramientas relacionadas al diccionario del idioma español.
</details>
<h3>Herramientas a implementar</h3>
<b>Definiciones:</b>
<details>
  <summary>Permite obtener definiciones utilizando servicios web.</summary>
  Sin detalles.
</details>
<b>Analizador:</b>
<details>
  <summary>Devuelve datos estadísticos sobre un texto, hace uso del resto de las herramientas.</summary>
  Sin detalles.
</details>
<b>Porcentuador:</b>
<details>
  <summary>Permite estimar el porcentaje del idioma utilizado por un texto. Útil para tener una idea de la riqueza de un texto de forma rápida.</summary>
  <p align="justify">
  Lo que se intenta calcular es lo siguiente: PORCENTAJE = 100*(cantidad de palabras(distintas) utilizadas)/(cantidad de palabras existentes(en el diccionario)). Debido a que el diccionario (palabras.txt) sólo presenta la forma más elemental de cada palabra (verbos sólo en infinitivo, sustantivos y adjetivos sólo en singular masculino/neutro, adverbios que se derivan de otra palabra son omitidos y solo se incluyen adverbios "puros" o de uso frecuente, etc.), si para calcular la cantidad PORCENTAJE se limitara a simplemente buscar cada palabra del archivo palabras.txt en el texto a analizar lo que se obtendría sería solo una estimación muy burda y poco realista de lo que se pretende calcular. Para hacer que la estimación sea mas realista se usan las siguientes heurísticas:
  <ol>
    <li>Se agregan todas las conjugaciones de los verbos regulares al diccionario, las ocurrencias de cualquier conjugación de un mismo verbo cuentan como una única plabra utilizada, por lo que, por ejemplo 'pinto' y 'pintas' cuentan como una única palabra utilizada (el verbo pintar).</li>
    <li>Se agregan todas las conjugaciones de los verbos irregulares al diccionario, las ocurrencias de cualquier conjugacion de un verbo irregular cuentan como palabras utilizadas individuales, por lo que, por ejemplo 'soy' y 'eres' cuentan como dos palabras utilizadas (aunque ambas palabras sean derivadas del verbo ser).</li>
    <li>Para los sustantivos que admiten forma femenina se agregan las mismas, también se agregan las formas masculina y femenina en plural. Aclaración: los sustantivos que no admiten forma femenina no introducen su forma plural al diccionario.</li>
  </ol>
  Finalmente las palabras del texto analizado que no estaban presentes en el diccionario son devueltas en un archivo con el nombre ausentes_fecha_hora.txt, tambien se muestran en la salida tanto el porcentaje real, como el porcentaje extendido, el cual resulta de agregar las palabras ausentes al diccionario, y el mismo se calcula de la siguiente forma: PORCENTAJE_EXTENDIDO: = 100*(cantidad de palabras utilizadas + cantidad de palabras ausentes)/(cantidad de palabras existentes + cantidad de palabras ausentes).
</p>
</details>