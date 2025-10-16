import os 
import re
import difflib
import itertools
from prettytable import PrettyTable

def tok_norm(code):
    code = re.sub(r'//.*|/\*[\s\S]*?\*/|#.*', '', code)
    
    code = re.sub(r'".*?"|\'.*?\'', 'STR', code)
    
    code = re.sub(r'\b\d+\b', 'NUM', code)

    code = re.sub(r'\b\d+\b', 'NUM', code)

    code = re.sub(r'\b\d+\b', 'NUM', code)

    return code

def sim_score(code1, code2):
    seq = difflib.SequenceMatcher(None, code1, code2)
    return round(seq.ratio() * 100,2)

def jplag_light(folder_path):
    files = [f for f in os.listdir(folder_path) if f.endswith(('.py', '.cpp', '.java', '.c'))]
    processed = {}
    
    for file in files:
        with open(os.path.join(folder_path, file), 'r', encoding='utf-8', errors='ignore') as f:
            raw_code = f.read()
            processed[file] = tok_norm(raw_code)
            
            
    results = PrettyTable(["File 1", "File 2", "Similarity (%)"])
    for f1, f2 in itertools.combinations(files, 2):
        score = sim_score(processed[f1], processed[f2])
        results.add_row([f1, f2, score])
        
        print(results)
        
if __name__ == "__main__":
    folder = input("Enter path to folder containing code files: ")
    jplag_light(folder)