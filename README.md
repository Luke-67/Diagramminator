# Diagramminator
Programma per realizzare diagrammi di imprese/organizzazioni perché mi annoiavo di studiare GPO
## Requisiti!!
 - una chiave api di OpenAI
 - Graphviz
 - Windows, duh

## TODO:
- aggiungere supporto a linux
- aggiungere supporto a LLAMA (quindi modificare endpoint e key da GUI o file .config)
- aggiungere possibilità di modificare PATH da GUI e location output
- pulire un pò
- impacchettare dipendenze
- aggiungere configurazione tramite file

## ISTRUZIONI:
> non sono riuscito ancora ad includere le dipendenze quindi servono
1. metti tutto in una cartella
2. installa le dipendenze tramite pip:
    -openai
    -dotenv
3. installa [Graphviz](https://gitlab.com/api/v4/projects/4207231/packages/generic/graphviz-releases/12.2.0/windows_10_cmake_Release_graphviz-install-12.2.0-win64.exe) _il link rimanda all'installazione per Windows, dato che il Diagramminator non è ancora compatibile con linux_
4. crea un file `.env` contenente OPENAI_API_KEY='la tua chiave' _verrà incluso un file di configurazione nelle versioni successive_
5. esegui il programma e scrivi il tipo di azienda e il tipo di output
6. enjoy
