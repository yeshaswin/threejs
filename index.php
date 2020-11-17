 $str = file_get_contents($_FILES["file"]["tmp_name"]);
  $tojson = json_decode($str);
  echo (file_put_contents($tojson->way, $tojson->datable) !== false) ? 1 : 0;
