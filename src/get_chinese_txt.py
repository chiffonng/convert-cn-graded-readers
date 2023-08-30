from dataclasses import dataclass
import re
import os

@dataclass
class ConvertToChineseTxt:
    """ 
    Convert a txt file to a Chinese-only txt file.
    """
    original_file_path: str
    
    def __post_init__(self, result_file_path:str=None):
        if result_file_path:
            self.result_file_path = result_file_path
        else:
            self.result_file_path = self._get_result_file_path()
        
    def convert_txt(self) -> None:
        """Convert a txt file to a Chinese-only txt file.
        Args:
            file_path (str): path of the txt file
        Returns:
            None
        """
        chinese_text = self.get_chinese_from_txt()
        self.write_chinese_to_txt(chinese_text)

    def get_chinese_from_txt(self) -> str:
        """Get chinese characters and punctuation from a txt file.
        
        Returns:
            str: Chinese-only text
        """
        with open(self.original_file_path, 'r') as f:
            text = f.read()
        return self.get_chinese_from_str(text)
                    
    # Clean the write_chinese_to_txt method, make it shorter
    def write_chinese_to_txt(self, chinese_text:str) -> None:
        """Write chinese text to a txt file, sentence by sentence.

        Args:
            chinese_text (str): Chinese-only text
        Returns:
            None
        """
        # Separate chinest text by sentence, using punctuation ？！。 
        chinese_sentences = re.split(r'([？！。])', chinese_text)
        
        # Merge punctuation ？！。 with the sentence.
        for i in range(len(chinese_sentences)-1):
            if i % 2 == 0:
                chinese_sentences[i] += chinese_sentences[i+1]
                chinese_sentences[i+1] = ''
        
        # Write chinese text to a txt file, sentence by sentence.
        with open(self.result_file_path, 'w') as f:
            f.write('\n'.join(chinese_sentences))
    
                    
    def get_chinese_from_str(self, text:str) -> str:
        """Get chinese characters and punctuation from a string.
        Args:
            text (str): original text
        Returns:
            str: Chinese-only text
        """
        pattern = re.compile(r'[\u4e00-\u9fa5，。；：‘’“”（）【】、！？《》]')
        chinese_text = ''.join(pattern.findall(text))
        
        chinese_text_no_dup_punc = chinese_text.replace('“”', '')
        return chinese_text_no_dup_punc
    
    def _get_result_file_path(self) -> str:
        """Get the path of the result file.
        Returns:
            str: path of the result file
        """
        # Get the directory and name of the original file.
        original_file_dir = os.path.dirname(self.original_file_path)
        original_file_name = os.path.basename(self.original_file_path)
        
        # Get the path of the result file.
        result_file_name = 'cn_' + original_file_name
        result_file_dir = 'cn-' + original_file_dir.split('/')[-1]
        
        os.makedirs(result_file_dir, exist_ok=True)
        result_file_path = os.path.join(result_file_dir, result_file_name)
        
        return result_file_path