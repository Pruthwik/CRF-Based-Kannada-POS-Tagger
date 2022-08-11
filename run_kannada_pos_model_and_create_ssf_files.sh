# Select the create features program based on raw or conll format.
input_folder=$1
output_folder=$2
model_path=$3
format=$4
if [ ! -d $output_folder ];then
	mkdir $output_folder
fi
for fl in $(ls $input_folder); do
	input_path=$input_folder"/"$fl
	feature_path=$input_folder"/"$fl"-features"
	pred_path=$input_folder"/"$fl"-pred-pos"
	output_path=$output_folder"/"$fl".ssf"
	if [ $format == "conll" ];then
		python3 create_features_for_pos_tagging_on_sentences_conll_format.py --input $input_path --output $feature_path
	else
		python3 create_features_for_pos_tagging_on_raw_sentences.py --input $input_path --output $feature_path
	fi
	crf_test -m $model_path $feature_path > $pred_path
	python3 create_ssf_file_from_feature_file.py --input $pred_path --output $output_path
	rm -rf $feature_path $pred_path
done
