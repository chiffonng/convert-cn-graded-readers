from src.get_chinese_txt import ConvertToChineseTxt

file_path = './graded-reader-500/story7.txt'
convert_to_chinese_txt = ConvertToChineseTxt(file_path)
convert_to_chinese_txt.convert_txt()