from jikanpy import Jikan
from pathlib import Path
import xml.etree.ElementTree as ET
import zipfile, re, xml.dom.minidom, os

# Handle file

src = Path(input('Please insert file: ').strip('& ').strip("'"))

fileName = src.stem
mangaTitle = fileName.split('(')

if bool(re.search('v[0-9]{1,3}', mangaTitle[0])): # Series
    searchTerm = mangaTitle[0].split('v')[0].strip()
    currentVolume = mangaTitle[0].split('v')[1].strip()
else: # One-Shot
    searchTerm = mangaTitle[0].strip()
    currentVolume = 1

# API
jikan = Jikan()

output = jikan.search(
    'manga', searchTerm
)

output = output['data'][0]

manga_title = output['titles'][0]['title']

# Check if finished
onGoingSeries = output['volumes']
if onGoingSeries == "null":
    latestVolume = "None"
else:
    onGoingSeries = str(output['volumes'])
    latestVolume = onGoingSeries

print("Collecting metadata...")

metadata = {
    'Series': str(manga_title),
    'Count': str(latestVolume),
    'Author': str(output['authors'][0]['name']),
    'Genre': str(output['genres'][0]['name']),
    'Synopsis': str(output['synopsis']),
    'Web': str(output['url']),
    'ID': str(output['mal_id']),
    'Volume': str(currentVolume),
    'Type': str(output['type']),
    'Year': str(output['published']['prop']['from']['year']),
    'Month': str(output['published']['prop']['from']['month']),
    'Day': str(output['published']['prop']['from']['day']),
}

# Write to XML
print("Writing ComicInfo.xml...")

data = ET.Element('ComicInfo')

xmlElements = len(metadata)
    
for i in range(xmlElements):
    globals()[f'x{i}'] = i
    
    for key, value in metadata.items():
        i = ET.SubElement(data, key)
        i.text = value
    break

et = ET.ElementTree(data)

b_xml = ET.tostring(data)

temp = xml.dom.minidom.parseString(b_xml)
pretty = temp.toprettyxml(encoding = 'UTF-8', indent = "  ")

with open("ComicInfo.xml", "wb") as f:
    f.write(pretty)

with zipfile.ZipFile(src, 'a') as zipf:
    source_path = 'ComicInfo.xml'
    zipf.write(source_path)

print(f"Metadata has been added to {src.stem}.")


os.system('pause')