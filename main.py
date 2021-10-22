from src.ParseText import ParseText
from src.ConvertDirectory import ConvertDirectory

parse_text = ParseText()
#print(parse_text.convert("def populateEntity(self, sqlCommand, dataRows)"))
convert_directory = ConvertDirectory()
convert_directory.convert_files(r"C:\Users\ds267f\Documents\github\LearningACodeBase")