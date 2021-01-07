def make_tlp(whatsapp_template, waid, context):

    whatsapp_api_link = 

    raw_text = whatsapp_template.content

    text = urllib.parse.quote(raw_text)
    
    whatsapp_link = 'https://api.whatsapp.com/send?phone={}'.format(waid) + '&text=' + text

    return whatsapp_link
