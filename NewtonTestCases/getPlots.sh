#!/bin/bash -e

planeTests=/home/hilary/OpenFOAM/hilary-2.1.0/run/shallowWaterPlane
planeTests_=`echo $planeTests | sed 's/\//_/g'`

cpFiles=()

pngFiles=(
    $planeTests/cubeSphere_r/50x50/0/hU.eps
    $planeTests/cubeSphere_r/100x100/0/hU.eps
    $planeTests/cubeSphere_r/100x100/600000/hUDiff.eps
    $planeTests/cubeSphere/100x100/600000/hUDiff.eps
    $planeTests/orthog_r/100x100/600000/hUDiff.eps
    $planeTests/orthog/100x100/600000/hUDiff.eps
)

pdfFiles=(
    $planeTests/plots/hErrorSeries.eps
    $planeTests/plots/hErrorRes.eps
)

for file in ${pngFiles[*]}
do
    fileNew=`echo $file | sed 's/\//_/g' | sed 's/'$planeTests_'_//g' | \
        sed 's/'$planeTests_'//g' | sed 's/.eps//g'`
    fileNew=graphics/$fileNew.png
    pngFile=`echo $file | sed 's/.eps/.png/g'`

    if [ ! -e $pngFile ] || [ `stat -c "%Y" $file` -gt `stat -c "%Y" $pngFile` ]
      then
        echo converting $file to $pngFile
        eps2png $file
    fi

    rsync -ut $pngFile $fileNew
done

for file in ${pdfFiles[*]}
do
    fileNew=`echo $file | sed 's/\//_/g' | sed 's/'$planeTests_'_//g' | \
        sed 's/.eps//g'`
    fileNew=graphics/$fileNew.pdf
    pdfFile=`echo $file | sed 's/.eps/.pdf/g'`

    if [ ! -e $pdfFile ] || [ `stat -c "%Y" $file` -gt `stat -c "%Y" $pdfFile` ]
      then
        echo converting $file to $pdfFile
        makebb $file
        epstopdf $file
    fi

    rsync -ut $pdfFile $fileNew
done

