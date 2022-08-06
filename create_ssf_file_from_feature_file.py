"""Create a file in SSF format from feature file."""
import re
import argparse


def read_lines_from_file(file_path):
    '''
    Read lines from a file.
    '''
    with open(file_path, 'r', encoding='utf-8') as file_read:
        return file_read.readlines()


def read_feature_file_and_create_ssf(file_path):
    '''
    Read feature file and create ssf formatted file.
    '''
    final_string = ''
    sent_count = 1
    cntr = 1
    sent_string = ''
    prev_tag = ''
    prev_sent_count = 0
    lines = open(file_path, 'r', encoding='utf-8').readlines()
    sent_string += "<Sentence id='" + str(sent_count) + "'>\n"
    for line in lines:
        if line.strip() != '':
            features = line.strip().split('\t')
            sent_string += str(cntr) + '\t' + \
                features[0] + '\t' + features[-1] + '\t\n'
            cntr += 1
        else:
            sent_string += '</Sentence>\n'
            final_string += sent_string + '\n'
            sent_count += 1
            cntr = 1
            sent_string = "<Sentence id='" + \
                str(sent_count) + "'>\n"
    return final_string


def write_text_to_file(out_path, data):
    '''
    :param out_path: Enter the path of the output file
    :param data: Enter the token features of sentence separated by a blank line
    :return: None
    '''
    with open(out_path, 'w+', encoding='utf-8') as fout:
        fout.write(data + '\n')
        fout.close()


def main():
    '''
    Pass arguments and call functions here.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input', dest='inp', help="Add the input path from where tokens and its features will be extracted")
    parser.add_argument(
        '--output', dest='out', help="Add the output file where the features will be saved")
    args = parser.parse_args()
    ssf_string = read_feature_file_and_create_ssf(args.inp)
    write_text_to_file(args.out, ssf_string)


if __name__ == '__main__':
    main()
