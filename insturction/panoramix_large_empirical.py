#conding=utf8
import os
import panoramix

def panoramix_large(directory_path,save_result_path):
    """

    :param directory_path:
    :param save_result_path:
    :return:
    """
    g = os.walk(directory_path)
    for path, dir_list, file_list in g:
        for file_name in file_list:
            json_file = os.path.join(path, file_name)
            panoramix.paronomix_double.get_json_to_panoramix_double(json_file, save_result_path)

