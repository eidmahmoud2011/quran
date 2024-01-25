import openai
from pywebio import *
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from pywebio.output import put_table
from pywebio.input import input
from pywebio import config
import os
import json

#from pywebio import start_server
#from pywebio.input import input, PASSWORD
#from pywebio.input import PASSWORD
#import os
from dotenv import load_dotenv

#from pywebio import start_server, input, output
#import openai
#import os

# Sample JSON data
json_data = """
[
    {"id": "الفاتحة", "name": "https://server13.mp3quran.net/husr/001.mp3"},
    {"id": "البقرة", "name": "https://server13.mp3quran.net/husr/002.mp3"},
    {"id": "أل عمران", "name": "https://server13.mp3quran.net/husr/003.mp3"},
    {"id": "النساء", "name": "https://server13.mp3quran.net/husr/004.mp3"},

    {"id": "المائدة", "name": "https://server13.mp3quran.net/husr/005.mp3"},
    {"id": "الأنعام", "name": "https://server13.mp3quran.net/husr/006.mp3"},
    {"id": "الأعراف", "name": "https://server13.mp3quran.net/husr/007.mp3"},
    {"id": "الأنفال", "name": "https://server13.mp3quran.net/husr/008.mp3"},

    {"id": "التوبة", "name": "https://server13.mp3quran.net/husr/009.mp3"},
    {"id": "يونس", "name": "https://server13.mp3quran.net/husr/010.mp3"},
    {"id": "هود", "name": "https://server13.mp3quran.net/husr/011.mp3"},
    {"id": "يوسف", "name": "https://server13.mp3quran.net/husr/012.mp3"},

    {"id": "الرعد", "name": "https://server13.mp3quran.net/husr/013.mp3"},
    {"id": "إبراهيم", "name": "https://server13.mp3quran.net/husr/014.mp3"},
    {"id": "الحجر", "name": "https://server13.mp3quran.net/husr/015.mp3"},
    {"id": "النحل", "name": "https://server13.mp3quran.net/husr/016.mp3"},

    {"id": "الإسراء", "name": "https://server13.mp3quran.net/husr/017.mp3"},
    {"id": "الكهف", "name": "https://server13.mp3quran.net/husr/018.mp3"},
    {"id": "مريم", "name": "https://server13.mp3quran.net/husr/019.mp3"},
    {"id": "طه", "name": "https://server13.mp3quran.net/husr/020.mp3"},

    {"id": "الأنبياء", "name": "https://server13.mp3quran.net/husr/021.mp3"},
    {"id": "الحج", "name": "https://server13.mp3quran.net/husr/022.mp3"},
    {"id": "المؤمنون", "name": "https://server13.mp3quran.net/husr/023.mp3"},
    {"id": "النور", "name": "https://server13.mp3quran.net/husr/024.mp3"},

    {"id": "الفرقان", "name": "https://server13.mp3quran.net/husr/025.mp3"},
    {"id": "الشعراء", "name": "https://server13.mp3quran.net/husr/026.mp3"},
    {"id": "النمل", "name": "https://server13.mp3quran.net/husr/027.mp3"},
    {"id": "القصص", "name": "https://server13.mp3quran.net/husr/028.mp3"},

    {"id": "العنكبوت", "name": "https://server13.mp3quran.net/husr/029.mp3"},
    {"id": "الروم", "name": "https://server13.mp3quran.net/husr/030.mp3"},
    {"id": "لقمان", "name": "https://server13.mp3quran.net/husr/031.mp3"},
    {"id": "السجدة", "name": "https://server13.mp3quran.net/husr/032.mp3"},

     {"id": "الأحزاب", "name": "https://server13.mp3quran.net/husr/033.mp3"},
    {"id": "سبأ", "name": "https://server13.mp3quran.net/husr/034.mp3"},
    {"id": "فاطر", "name": "https://server13.mp3quran.net/husr/035.mp3"},
    {"id": "يس", "name": "https://server13.mp3quran.net/husr/036.mp3"},

    {"id": "الصافات", "name": "https://server13.mp3quran.net/husr/037.mp3"},
    {"id": "ص", "name": "https://server13.mp3quran.net/husr/038.mp3"},
    {"id": "الزمر", "name": "https://server13.mp3quran.net/husr/039.mp3"},
    {"id": "غافر", "name": "https://server13.mp3quran.net/husr/040.mp3"},

    {"id": "فصلت", "name": "https://server13.mp3quran.net/husr/041.mp3"},
    {"id": "الشورى", "name": "https://server13.mp3quran.net/husr/042.mp3"},
    {"id": "الزخرف", "name": "https://server13.mp3quran.net/husr/043.mp3"},
    {"id": "الدخان", "name": "https://server13.mp3quran.net/husr/044.mp3"},

    {"id": "الجاثية", "name": "https://server13.mp3quran.net/husr/045.mp3"},
    {"id": "الأحقاف", "name": "https://server13.mp3quran.net/husr/046.mp3"},
    {"id": "محمد", "name": "https://server13.mp3quran.net/husr/047.mp3"},
    {"id": "الفتح", "name": "https://server13.mp3quran.net/husr/048.mp3"},

    {"id": "الحجرات", "name": "https://server13.mp3quran.net/husr/049.mp3"},
    {"id": "ق", "name": "https://server13.mp3quran.net/husr/050.mp3"},
    {"id": "الزاريات", "name": "https://server13.mp3quran.net/husr/051.mp3"},
    {"id": "الطور", "name": "https://server13.mp3quran.net/husr/052.mp3"},

    {"id": "النجم", "name": "https://server13.mp3quran.net/husr/053.mp3"},
    {"id": "القمر", "name": "https://server13.mp3quran.net/husr/054.mp3"},
    {"id": "الرحمن", "name": "https://server13.mp3quran.net/husr/055.mp3"},
    {"id": "الواقعة", "name": "https://server13.mp3quran.net/husr/056.mp3"},

    {"id": "الحديد", "name": "https://server13.mp3quran.net/husr/057.mp3"},
    {"id": "المجادلة", "name": "https://server13.mp3quran.net/husr/058.mp3"},
    {"id": "الحشر", "name": "https://server13.mp3quran.net/husr/059.mp3"},
    {"id": "الممتحنة", "name": "https://server13.mp3quran.net/husr/060.mp3"},

    {"id": "الصف", "name": "https://server13.mp3quran.net/husr/061.mp3"},
    {"id": "الجمعة", "name": "https://server13.mp3quran.net/husr/062.mp3"},
    {"id": "المنافقون", "name": "https://server13.mp3quran.net/husr/063.mp3"},
    {"id": "التغابن", "name": "https://server13.mp3quran.net/husr/064.mp3"},

    {"id": "الطلاق", "name": "https://server13.mp3quran.net/husr/065.mp3"},
    {"id": "التحريم", "name": "https://server13.mp3quran.net/husr/066.mp3"},
    {"id": "الملك", "name": "https://server13.mp3quran.net/husr/067.mp3"},
    {"id": "القلم", "name": "https://server13.mp3quran.net/husr/068.mp3"},

    {"id": "الحاقة", "name": "https://server13.mp3quran.net/husr/069.mp3"},
    {"id": "المعارج", "name": "https://server13.mp3quran.net/husr/070.mp3"},
    {"id": "نوح", "name": "https://server13.mp3quran.net/husr/071.mp3"},
    {"id": "الجن", "name": "https://server13.mp3quran.net/husr/072.mp3"},

    {"id": "المزمل", "name": "https://server13.mp3quran.net/husr/073.mp3"},
    {"id": "المدثر", "name": "https://server13.mp3quran.net/husr/074.mp3"},
    {"id": "القيامة", "name": "https://server13.mp3quran.net/husr/075.mp3"},
    {"id": "الإنسان", "name": "https://server13.mp3quran.net/husr/076.mp3"},

    {"id": "المرسلات", "name": "https://server13.mp3quran.net/husr/077.mp3"},
    {"id": "النبأ", "name": "https://server13.mp3quran.net/husr/078.mp3"},
    {"id": "النازعات", "name": "https://server13.mp3quran.net/husr/079.mp3"},
    {"id": "عبس", "name": "https://server13.mp3quran.net/husr/080.mp3"},

    {"id": "التكوير", "name": "https://server13.mp3quran.net/husr/081.mp3"},
    {"id": "الإنفطار", "name": "https://server13.mp3quran.net/husr/082.mp3"},
    {"id": "المطففين", "name": "https://server13.mp3quran.net/husr/083.mp3"},
    {"id": "الإنشقاق", "name": "https://server13.mp3quran.net/husr/084.mp3"},

    {"id": "البروج", "name": "https://server13.mp3quran.net/husr/085.mp3"},
    {"id": "الطارق", "name": "https://server13.mp3quran.net/husr/086.mp3"},
    {"id": "الأعلى", "name": "https://server13.mp3quran.net/husr/087.mp3"},
    {"id": "الغاشية", "name": "https://server13.mp3quran.net/husr/088.mp3"},

    {"id": "الفجر", "name": "https://server13.mp3quran.net/husr/089.mp3"},
    {"id": "البلد", "name": "https://server13.mp3quran.net/husr/090.mp3"},
    {"id": "الشمس", "name": "https://server13.mp3quran.net/husr/091.mp3"},
    {"id": "الليل", "name": "https://server13.mp3quran.net/husr/092.mp3"},

    {"id": "الضحى", "name": "https://server13.mp3quran.net/husr/093.mp3"},
    {"id": "الشرح", "name": "https://server13.mp3quran.net/husr/094.mp3"},
    {"id": "التين", "name": "https://server13.mp3quran.net/husr/095.mp3"},
    {"id": "العلق", "name": "https://server13.mp3quran.net/husr/096.mp3"},

    {"id": "القدر", "name": "https://server13.mp3quran.net/husr/097.mp3"},
    {"id": "البينة", "name": "https://server13.mp3quran.net/husr/098.mp3"},
    {"id": "الزلزلة", "name": "https://server13.mp3quran.net/husr/099.mp3"},
    {"id": "العاديات", "name": "https://server13.mp3quran.net/husr/100.mp3"},

    {"id": "القارعة", "name": "https://server13.mp3quran.net/husr/101.mp3"},
    {"id": "التكاثر", "name": "https://server13.mp3quran.net/husr/102.mp3"},
    {"id": "العصر", "name": "https://server13.mp3quran.net/husr/103.mp3"},
    {"id": "الهمزة", "name": "https://server13.mp3quran.net/husr/104.mp3"},

    {"id": "الفيل", "name": "https://server13.mp3quran.net/husr/105.mp3"},
    {"id": "قريش", "name": "https://server13.mp3quran.net/husr/106.mp3"},
    {"id": "الماعون", "name": "https://server13.mp3quran.net/husr/107.mp3"},
    {"id": "الكوثر", "name": "https://server13.mp3quran.net/husr/108.mp3"},

    {"id": "الكافرون", "name": "https://server13.mp3quran.net/husr/109.mp3"},
    {"id": "النصر", "name": "https://server13.mp3quran.net/husr/110.mp3"},
    {"id": "المسد", "name": "https://server13.mp3quran.net/husr/111.mp3"},
    {"id": "الإخلاص", "name": "https://server13.mp3quran.net/husr/112.mp3"},

    {"id": "الفلق", "name": "https://server13.mp3quran.net/husr/113.mp3"},
    {"id": "الناس", "name": "https://server13.mp3quran.net/husr/114.mp3"}
]
"""
 
# # Convert JSON data to a Python object
# data = json.loads(json_data)
 
# # Iterate through the JSON array
# for item in data:
#     print(item["id"], item["name"])
######################################################
#key1='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'
#openai.api_key = key1
##################################
# Load OpenAI API key from environment variable
#openai.api_key = os.getenv("OPENAI_API_KEY")

# Load OpenAI API key from environment variable
#openai.api_key = os.getenv("OPENAI_API_KEY1")
####################################
def load_api_key(secrets_file="secrets.json"):
    with open(secrets_file) as f:
        secrets = json.load(f)
    return secrets["OPENAI_API_KEY"]

# Set secret API key
# Typically, we'd use an environment variable (e.g., echo "export OPENAI_API_KEY='yourkey'" >> ~/.zshrc)
# However, using "internalConsole" in launch.json requires setting it in the code for compatibility with Hebrew
api_key = load_api_key()
openai.api_key = api_key
##################################
css="""
    @import url('https://fonts.googleapis.com/css2?family=Marhey:wght@300&display=swap');
    #h3{
    font-family: 'Marhey', sans-serif;
    }
    #para{
    font-family: 'Marhey', sans-serif;
    color:gray;
    }
    .y{
    width:33%;
    float:right;
    }
 .center {
     display: block;
     margin-left: auto;
     margin-right: auto;
     width: 50%;
}
"""
@config(css_style=css)
def app():

    #put_image('https://drive.google.com/file/d/1jNCEanTTWhtTSR3NWj7Lv_r4ntpAz1hs/view',width='200',height='200')
    put_html("""<h2 id='para'> مرحباً بكم في أكاديمية نور القرأن</h2>
             """).style('direction:rtl; text-align:center;')
    put_image('https://envato-shoebox-0.imgix.net/6b94/c775-99b3-4bf6-83e1-5afa0b9e0d8e/610d0efc6e60182b1eb018e6_withmeta.jpg?auto=compress%2Cformat&mark=https%3A%2F%2Felements-assets.envato.com%2Fstatic%2Fwatermark2.png&w=1000&fit=max&markalign=center%2Cmiddle&markalpha=18&s=794ddf1d3aee45f59360b28c3c803a3e',width='100%',height='100')
    put_html("""<p> القرأن الكريم بصوت الشيخ محمود خليل الحصري برواية حفص عن عاصم</p>
             """).style('direction:rtl; text-align:center;')
    #<p> القرأن الكريم بصوت الشيخ محمود خليل الحصري برواية حفص عن عاصم</p>
    detail_str=''
    # sno=0
    # for chapter_no in suar :
    #     detail_str=detail_str+'<details> <summary>'+chapter_no[]
    # Convert JSON data to a Python object
    data = json.loads(json_data)
 
    # Iterate through the JSON array
    for item in data:
        detail_str=detail_str+'<details> <summary> '+item["id"]+'</summary> <audio controls> <source src='+item["name"]+' type="audio/mp3"> </audio></details>'
        #print(item["id"], item["name"])
    put_html(detail_str).style('direction:rtl; text-align:right;')

    # put_html("""              
    #          <details>
    #             <summary>'الفاتحة'</summary>
    #             <audio controls>
    #                 <source src="https://server13.mp3quran.net/husr/001.mp3" type="audio/mp3">
    #             </audio>
    #          </details>
    #     """).style('direction:rtl; text-align:right;')


    put_html("""<hr>
             <p>هذا التطبيق متاح للجميع مجانا لتعليم كتاب الله تعالى ... نسألكم الدعاء
             <br>
                (ملفات الصوت المستخدمة من موقع 
             https://server13.mp3quran.net/husr/)</p>
             """).style('direction:rtl; text-align:right;')
#app()

def openai_response(question):
    response = openai.Completion.create(
    #engine="text-davinci-002",
    engine="gpt-3.5-turbo-instruct",
    prompt=question,
    temperature=0.7,
    max_tokens=4000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    return '{}'.format(response.choices[0].text[0:])

def main():
    app()
    while True:
        question = input('أسأل اجيبك بإذن الله تعالى')
        put_table([
            [question , ':السؤال'],
            [ openai_response(question), ':الجواب']
        ])
        
#main()

#start_server(main, port=8080, debug=True)

if __name__ == '__main__':
    start_server(main, port=8080, debug=True)