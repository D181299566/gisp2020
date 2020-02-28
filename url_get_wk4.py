from gisp2020.read_from_file_or_net import get_stuff_from_net as gn
from gisp2020.read_from_file_or_net import read_any_text_file as rf

try:
    my_url = "http://193.1.33.31:88/pa1/gettysburg.txt"

    my_data = gn(my_url)
    print(f"From {my_url}\n\n{my_data}")
except Exception as e:
    print(f"Something bad happened, probably DIT firewall-related\n{e}")
finally:
    print("="*50)

try:
    my_file = "data/gettysburg.txt"
    my_data = rf(my_file)
    print(f"From {my_file}\n\n{my_data}")
except Exception as e:
    print(f"Couldn't read the file.\n{e}")
finally:
    print("="*50)
