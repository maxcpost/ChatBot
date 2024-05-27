 __    __     ______     __         __  __   
/\ "-./  \   /\  __ \   /\ \       /\ \_\ \  
\ \ \-./\ \  \ \ \/\ \  \ \ \____  \ \____ \ 
 \ \_\ \ \_\  \ \_____\  \ \_____\  \/\_____\
  \/_/  \/_/   \/_____/   \/_____/   \/_____/


=========================================================
Version: 4.0
Authors: Maximillian Post
=========================================================

COMPONENTS
1 - (data_muncher.py) A tool that processes data (PDFs, Word documents, Excel sheets, PowerPoint presentations, text files, and HTML files) and turns it into json files for the llm to more easily use.

2 - (moly.agoratree.xyz) A web based chatbot that uses Retrieval-Augmented Generation (RAG) system to answer users questions.


1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

STEPS
1 - Gather data into a single folder
2 - Run the data muncher to convert those files into something that is more digestable for the LLM

DEPENDANCIES
pip install flask flask-cors openai PyPDF2 python-docx pandas xlrd openpyxl beautifulsoup4 lxml python-pptx langchain unstructured


