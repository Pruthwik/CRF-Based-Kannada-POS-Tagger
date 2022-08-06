input_folder=$1
output_folder=$2
model_path=$3
if [ ! -d $output_folder ];then
	mkdir $output_folder
fi
for fl in $(ls $input_folder); do
	input_path=$input_folder"/"$fl
	feature_path=$input_folder"/"$fl"-features"
	pred_path=$input_folder"/"$fl"-pred-pos"
	output_path=$output_folder"/"$fl".ssf"
	python3 create_features_for_pos_tagging.py --input $input_path --output $feature_path
	crf_test -m $model_path $feature_path > $pred_path
	python3 create_ssf_file_from_feature_file.py --input $pred_path --output $output_path
	rm -rf $feature_path $pred_path
done
