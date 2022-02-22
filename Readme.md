<p>Repositorio para el desarrollo de herramientas relacionadas al diccionario del idioma español.</p>
<h3>Herramientas a implementar</h3>
<b>Definiciones:</b>
<p>Permite obtener definiciones utilizando servicios web.</p>
<b>Analizador:</b>
<p>Devuelve datos estadísticos sobre un texto, hace uso del resto de las herramientas.</p>
<b>Porcentuador:</b>
<p>
  Permite estimar el porcentaje del idioma utilizado por un texto. Útil para tener una idea de la riqueza de un texto de forma rápida.<br><br>
  Lo que se intenta calcular es lo siguiente: PORCENTAJE = 100*(cantidad de palabras utilizadas)/(cantidad de palabras existentes).
  Debido a que el diccionario (palabras.txt) sólo presenta la forma más elemental de cada palabra (verbos sólo en infinitivo, sustantivos y adjetivos sólo en singular, adverbios que se derivan de otra palabra son omitidos y solo se incluyen adverbios de uso frecuente, etc.), si para calcular la cantidad PORCENTAJE se limitara a simplemente buscar cada palabra del archivo palabras.txt en el texto a analizar lo que se obtendría sería solo una estimación muy burda y poco realista de lo que se pretende calcular.<br><br>
  Para hacer que la estimación sea mas realista se siguen las siguientes heurísticas:
  <ol>
    <li>Se agregan todas las conjugaciones de los verbos regulares al diccionario, las ocurrencias de cualquier conjugación de un mismo verbo cuentan como una única plabra utilizada, por lo que, por ejemplo 'pinto' y 'pintas' cuentan como una única palabra utilizada.</li>
    <li>Se agregan todas las conjugaciones de los verbos irregulares al diccionario, las ocurrencias de cualquier conjugacion de un mismo verbo cuenta como palabras utilizadas de forma individual, por lo que, por ejemplo 'soy' y 'eres' cuentan como dos palabras utilizadas.
  </ol>
  
</p>
