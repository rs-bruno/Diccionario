<details>
  <summary>diccionario.es</summary>
  Repositorio para el desarrollo de herramientas relacionadas al diccionario del idioma español.
</details>
<h3>Herramientas a implementar</h3>
<b>Definiciones:</b>
<details>
  <summary>Permite obtener definiciones utilizando servicios web.</summary>
  Aún no implementado.
</details>
<b>Porcentuador:</b>
<details>
  <summary>Permite estimar el porcentaje del idioma utilizado por un texto. Útil para tener una idea de la riqueza de un texto de forma rápida.</summary>
  <p align="justify">
  Lo que se intenta calcular es lo siguiente: PORCENTAJE = 100*(cantidad de palabras(distintas) utilizadas)/(cantidad de palabras existentes(en el diccionario)). Debido a que el diccionario (palabras.txt) sólo presenta la forma más elemental de cada palabra (verbos sólo en infinitivo, sustantivos y adjetivos sólo en singular masculino/neutro, adverbios que se derivan de otra palabra son omitidos y solo se incluyen adverbios "puros" o de uso frecuente, etc.), si para calcular la cantidad PORCENTAJE se limitara a simplemente buscar cada palabra del archivo palabras.txt en el texto a analizar lo que se obtendría sería solo una estimación muy burda y poco realista de lo que se pretende calcular. Para hacer que la estimación sea mas realista se usan las siguientes heurísticas:
  <ol>
    <li>Se agregan todas las conjugaciones de los verbos regulares al diccionario, las ocurrencias de cualquier conjugación de un mismo verbo cuentan como una única plabra utilizada, por lo que, por ejemplo 'pinto' y 'pintas' cuentan como una única palabra utilizada (el verbo pintar).</li>
    <li>Se agregan todas las conjugaciones de los verbos irregulares al diccionario, las ocurrencias de cualquier conjugacion de un verbo irregular cuentan como palabras utilizadas individuales, por lo que, por ejemplo 'soy' y 'eres' cuentan como dos palabras utilizadas (aunque ambas palabras sean derivadas del verbo ser).</li>
    <li>Para los sustantivos y adjetivos que admiten forma femenina se agregan las mismas, también se agregan las formas masculina y femenina en plural. Al igual que con los verbos regulares, la ocurrencia de cualquiera de éstas cuatro formas (masculina/femenina, plural/singular) de una de éstas palabras cuentan como una única palabra utilizada. Aclaración: los sustantivos y adjetivos que no admiten forma femenina no introducen su forma plural al diccionario.</li>
  </ol>
  Finalmente las palabras del texto analizado que no estaban presentes en el diccionario son devueltas en un archivo con el nombre ausentes_fecha_hora.txt, tambien se muestran en la salida tanto el porcentaje real, como el porcentaje extendido, el cual resulta de agregar las palabras ausentes al diccionario, y el mismo se calcula de la siguiente forma: PORCENTAJE_EXTENDIDO: = 100*(cantidad de palabras utilizadas + cantidad de palabras ausentes)/(cantidad de palabras existentes + cantidad de palabras ausentes).
</p>
</details>
<details>
  <summary>Casos de prueba porcentuador.</summary>
  Nombre obra | Porcentaje real | Porcentaje extendido<br>
  4 3 2 1 (Paul Auster) | 15.184529941326645%, (13561/89308) | 22.42851876126495%, (21901/97648)<br>
  La Santa Biblia (Digitalización por google) | 12.295651005509026%, (10981/89308) | 42.51018385995816%, (57918/136245)<br>
  Don Quijote de la Mancha (Miguel de Cervantes) | 11.832086711156895%, (10567/89308) | 18.917332564461653%, (18371/97112)<br>
  Cien años de soledad (Gabriel García Márquez) | 10.522013705379138%, (9397/89308) | 14.218085791575422%, (13245/93156)<br>
  Odisea (Homero) | 7.207640972813186%, (6437/89308) | 13.074809096249057%, (12465/95336)<br>
  Ilíada (Homero) | 6.903076991982801%, (6165/89308) | 12.164846077457796%, (11515/94658)<br>
</details>
