import re
import os 
from shutil import copyfile

# srcPath = 'C:\\Users\\Dinith Jaybaodhi\\Desktop\\toBeProcessed'
srcPath = 'C:\\Users\\Dinith Jaybaodhi\\Music\\toBeProcessed'
artistNames = ['gunadasa', 'kapuge' ,'clarance' ,'wijewardana', 'daddy' ,'damith' , 'asanka' , 
'athula' ,'adhikari','samitha' , 'vijaya', 'kumarathunga','amaredeva' , 'umaria', 'chandana' ,'liyanarachchi' , 'athma' ,
'liyanage' , 'punsiri' , 'soysa', 'henry' , 'kaldera' , ' deepika'  ,'priyadharshani' , 'rodni' , 'warnakula'
'kasun' , 'kalhara' , 'dayarathna' , 'ranathunga' , 'deepika'  , 'priyadharshani', 'namal' , 'udugama']
otherJunkWords = ['wwwsindume', 'wwwtopsinhalamp3', 'www' , 'top' , 'sinhala' , 'mp3' , 'sindu' , ]

folder = os.listdir(srcPath)

for file in folder:
    if(file != 'desktop.ini'):
        fileName = file
        endPosition = len(fileName) - 4
        modifiedName = fileName[0:endPosition]
        modifiedName = re.sub(r'[0-9,-/+{}=,.!]','',modifiedName).lower()
        modifiedName = re.sub(r'[_]',' ',modifiedName)

        for name in artistNames:
            modifiedName = re.sub(name ,'',modifiedName)

        for word in otherJunkWords:
            modifiedName = re.sub(word , '', modifiedName)
        
        modifiedName =  modifiedName.strip()
        os.rename(srcPath + '\\' + file,'./processed/' + modifiedName+'.mp3')
        print(modifiedName)

print('')



