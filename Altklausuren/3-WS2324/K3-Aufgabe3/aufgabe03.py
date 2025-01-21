import re 
 
def entferne_sonderzeichen(text): 
    words = re.sub(r"[^\w\s]", "", text).lower() 
    return words 
