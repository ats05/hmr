for s in `seq 5 8`
do
  for seq in `seq 1 2`
  do
      mkdir -p "human_datasets/mpi_inf_3dhp/S$s/Seq$seq/imageData"
      for file in `ls "human_datasets/mpi_inf_3dhp/S$s/Seq$seq/imageSequence/"`;
      do
          fileNum=`echo $file | grep -o '[0-9]'`
          echo $s $seq $file
          cpulimit -l 20 ffmpeg -i "human_datasets/mpi_inf_3dhp/S${s}/Seq${seq}/imageSequence/$file" -qscale:v 1 "human_datasets/mpi_inf_3dhp/S${s}/Seq${seq}/imageData/img_${fileNum}_%06d.jpg"
      done
  done
done
