def m33t_language_conversion(text):
    conversions = {
        'e': '3', 'a': '4', 'i': '1', 'o': '0', 's': '5',
        'а': '4', 'б': '6', 'в': 'b', 'г': 'r', 'д': 'd',
        'е': '3', 'ё': 'e', 'ж': 'zh', 'з': '3', 'и': '1',
        'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
        'о': '0', 'п': 'p', 'р': 'p', 'с': '5', 'т': 't',
        'у': 'u', 'ф': 'f', 'х': 'x', 'ц': 'ts', 'ч': 'ch',
        'ш': 'sh', 'щ': 'sch', 'ы': 'y', 'э': 'e', 'ю': 'yu',
        'я': 'ya'
    }
    return ''.join(conversions.get(char, char) for char in text)

def convert_to_m33t(text):
    text = text.lower()
    return m33t_language_conversion(text)
