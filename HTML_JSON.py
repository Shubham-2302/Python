from bs4 import BeautifulSoup
import json

def html_to_json_read(html_file_path):

    try:
        with open(html_file_path,'r',encoding='utf-8') as file:
            html_content = file.read()
    except :
        print("Error opening file")
    
        # print(html_content)


    html_to_json(html_content)

def html_to_json(html_content):
    # print(html_content)

    soup = BeautifulSoup(html_content,"html.parser")
    print(soup.name)
    for child in soup.children:
        print(f"child : {child} \n")
    # json_data = {
    #     "tag": soup.name,
    #     "children": [html_to_json(child) if child else str(child) for child in soup.children]
    #     # if child:
    #     #     html_to_json(child)
    #     # else:
    #     #     str(child)
    # }
    # # for child in soup.children:
    #     print((child.format_string))
    #     breaks

    # return json_data
    

def save_to_json(json_data,json_file_path):
    with open(json_file_path,'w',encoding='utf-8') as json_file:
        json.dump(json_data,json_file,ensure_ascii=False)



html_file_path = 'HTML.html'

json_data = html_to_json_read(html_file_path)

# json_file_path = "Indeed_JSON.json"

# save_to_json(json_data=json_data,json_file_path=json_file_path)

# print(f"HTML content from '{html_file_path}' has been parsed and saved to '{json_file_path}'.")