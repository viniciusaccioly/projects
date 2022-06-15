from xml.dom import minidom
from rich import print
import os

with open("/home/vinicius/codes/projects/Exemplos-Python/25220521071914000113650010000308389841013502-nfe.xml", 'rw', encoding='utf-8') as f:
    xml = minidom.parse(f)
    
    vBC = xml.getElementsByTagName("vBC")
    bc= 0
    for tag in vBC:
        bc += float(tag.firstChild.data)
    bc -= float(tag.lastChild.data)
    

    icms = xml.getElementsByTagName("vICMS")
    totalICMS = 0
    for tag in icms:
        totalICMS += float(tag.firstChild.data)
    totalICMS -= float(tag.lastChild.data)


    totTrib = xml.getElementsByTagName("vTotTrib")
    tributos = 0
    for tag in totTrib:
        tributos += float(tag.firstChild.data)
    tributos -= float(tag.lastChild.data)
    
   
    print(f'[on green]Total dos Produtos/BC:[/] {bc}{os.linesep}[on red]ICMS:[/] {totalICMS}{os.linesep}[on blue]Total de Tributos:[/] {tributos}')

f.close()