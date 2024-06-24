
#https://fosspost.org/divide-pdf-small-chunks-linux-command-line

number=$(pdfinfo -- "$file" 2> /dev/null | awk '$1 == "Pages:" {print $2}')

count=$((($number+$pagesper-1)/$pagesper))
filename=${file%.pdf}

counter=0
while [ "$count" -gt "$counter" ]; do
  start=$((counter*pagesper + 1));
  end=$((start + pagesper - 1));
  if [ $end -gt $number ]; then
    end=$number
  fi

 counterstring=$(printf %01d "$counter")
  pdftk "$file" cat "${start}-${end}" output "${filename}_${counterstring}.pdf"
  counter=$((counter + 1))
done