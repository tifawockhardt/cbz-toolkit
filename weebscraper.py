from jikanpy import Jikan
from pathlib import Path
import xml.etree.ElementTree as ET
import zipfile, re, xml.dom.minidom

# TODO: 
# Switch APIs
#   MAL does not carry info about individual volumes
# Clean up a million things
# Show a few results and pick the right series

# Handle file

filePath = input('Please insert file: ')
filePath = Path(filePath.strip('& ').strip("'"))

fileName = filePath.stem

mangaTitle = fileName.split('(')

if bool(re.search('v[0-9]{1,3}', mangaTitle[0])): # Series
    searchTerm = mangaTitle[0].split('v')[0].strip()
    currentVolume = mangaTitle[0].split('v')[1].strip()
else: # One-Shot
    searchTerm = mangaTitle[0].strip()
    currentVolume = 1

# API
jikan = Jikan()

mangaInput = searchTerm

search_result = jikan.search(
    'manga', mangaInput, parameters={'limit': 1}
)

mangaid = int(search_result['data'][0]['mal_id'])

output = jikan.manga(mangaid)['data']

animeTitle = output['titles'][0]['title']

onGoingSeries = None
latestVolume = None

if onGoingSeries == "null":
    latestVolume = "None"
else:
    onGoingSeries = str(output['volumes'])
    latestVolume = onGoingSeries

metadata = {
    'Series': str(animeTitle),
    'Count': str(latestVolume),
    'Author': str(output['authors'][0]['name']),
    'Genre': str(output['genres'][0]['name']),
    'Synopsis': str(output['synopsis']),
    'Web': str(output['url']),
    'ID': str(mangaid),
    'Volume': str(currentVolume),
    'Type': str(output['type']),
    'Year': str(output['published']['prop']['from']['year']),
    'Month': str(output['published']['prop']['from']['month']),
    'Day': str(output['published']['prop']['from']['day']),
}

data = ET.Element('ComicInfo')


# Write to XML

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


# Handle Cbz

oldExt = ".cbz"
newExt = ".zip"

filePathNew = filePath.with_suffix(newExt)

try:
    filePathRenamed = filePath.rename(filePathNew)
except FileNotFoundError:
    print(f"Error: Couldn't find {filePath}.")
except FileExistsError:
    print(f"Error: {filePath} already exists.")

with zipfile.ZipFile(filePathRenamed, 'a') as zipf:
    source_path = 'ComicInfo.xml'
    zipf.write(source_path)

filePathOld = filePath.with_suffix(oldExt)

try:
    filepathRerenamed = filePathRenamed.rename(filePathOld)
except FileNotFoundError:
    print(f"Error: Couldn't find {filePath}.")
except FileExistsError:
    print(f"Error: {filePath} already exists.")
else:
    print(f"Success: Metadata has been collected and been placed in {filepathRerenamed}.")