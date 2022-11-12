clear all
fid=fopen("datatest/obs.m15"); %ﬁle name to import
output=[];
%check if format is compact3
tipoFile=fgetl(fid);
if (~strcmp(tipoFile, 'COMPACT3'))
    warning(strcat('WRONG FORMAT: ',tipoFile, 'IS NOT COMPACT3'))
    return
end
%Start epoch
lineaEpoca=fgetl(fid);
if (contains(lineaEpoca,'GPS_START_TIME'))
    %process string
    cellData=strsplit(lineaEpoca);
    cellData(1)=[];
    anno=str2double(cellData{1});
    mese=str2double(cellData{2});
    giorno=str2double(cellData{3});
    ora=str2double(cellData{4});
    minuti=str2double(cellData{5});
    secondi=str2double(cellData{6});
else
    warning('I can not ﬁnd ﬁrst epoch')
    return
end
ii=0;
while ~feof(fid)
    lineaHeaderEpoca=fgetl(fid);
    %is the ﬁrst line?
    lineaHeaderEpocaCell=strsplit(lineaHeaderEpoca,' ');
    %delete ﬁrst cell because is empty
    lineaHeaderEpocaCell(1)=[];
    numSatEpoca=str2double(lineaHeaderEpocaCell(2));
    numSecDaAggiungere=str2double(lineaHeaderEpocaCell(1));
    if (numSatEpoca==-1) %Sats are the same of previous epoch
        vectNumSec=ones(size(PRN,1),1)*numSecDaAggiungere;
        %we need prevuois PRN
        lineaMisure=fgetl(fid);
        lineaMisureCell=strsplit(lineaMisure,' ');
        lineaMisureCell(1)=[];
        for m=1:size(PRN,1)
    misure(m,1)=str2double(lineaMisureCell{m});
        end
        output=[output;vectNumSec,PRN,misure];
    else %sats are changed
numSatEpoca=str2double(lineaHeaderEpocaCell(2));
vectNumSec=ones(numSatEpoca,1)*numSecDaAggiungere;
clear PRN;
satSysNum=0;
for i=3:numSatEpoca+2
    satSys=lineaHeaderEpocaCell{i}(1);
    switch satSys
        case 'G'
        satSysNum=1000;
        case 'E'
        satSysNum=3000;
        case 'R' 
        satSysNum=2000;
        end
        PRN(i-2,1)=satSysNum+str2double(lineaHeaderEpocaCell{i}(2:3));
end
lineaMisure=fgetl(fid);
lineaMisureCell=strsplit(lineaMisure,' ');
lineaMisureCell(1)=[];
clear misure;
for m=1:numSatEpoca
    misure(m,1)=str2double(lineaMisureCell{m});
end
output=[output;vectNumSec,PRN,misure];
end
end
fclose(fid);