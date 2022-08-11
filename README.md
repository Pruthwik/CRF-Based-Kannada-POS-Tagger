# This is a repository for CRF based Kannada POS tagger.
## Install CRF++ from this link https://taku910.github.io/crfpp/
## How to run the code
## sh run_kannada_pos_model_and_create_ssf_files.sh input_folder_path output_folder_path model_path format
### input_folder_path: contains Kannada raw sentences, a sentence in each line [avoid the backslash / at the end of the path]
### output_folder_path: after the predictions by the tagger, the POS tagged data will be written in SSF format (https://aclanthology.org/W14-5208.pdf) [avoid the backslash / at the end of the path]
### model_path: Path of the model
### format: conll or raw (type conll for conll format file, type raw for raw sentences)
### Give absolute paths for all the paths (relative path may throw an error)
