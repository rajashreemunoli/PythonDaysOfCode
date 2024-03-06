#Create a function to extract all URLs from a given text using regular expressions

#funtion to extract all URLs from a text file
def get_urls(f):
    import re
    pattern='\\b((?:https?|ftp|file):\/\/[-a-zA-Z0-9+&@#\/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#\/%=~_|])'
    s=''
    with open(f,'r') as text_file:
        s=text_file.read()
    urls=re.findall(pattern,s)
    return urls

#function to save list items in a text file
def list_in_txt(f,list):
    with open(f,'w') as fp:
        for item in list:
            fp.write(f'{item}\n')
    return

# Driver Code
if __name__ == '__main__':
   
    txt_in=input("Enter the text file to extract URLs from: ")
    txt_out=input("Enter the text file to save the URLs in: ")
    url_list=get_urls(txt_in)
    list_in_txt(txt_out,url_list)
    print(url_list)