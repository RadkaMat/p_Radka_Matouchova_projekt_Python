{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "5c20db35",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting streamlit\n",
      "  Downloading streamlit-1.12.0-py2.py3-none-any.whl (9.1 MB)\n",
      "     ---------------------------------------- 9.1/9.1 MB 6.7 MB/s eta 0:00:00\n",
      "Collecting altair>=3.2.0\n",
      "  Downloading altair-4.2.0-py3-none-any.whl (812 kB)\n",
      "     -------------------------------------- 812.8/812.8 kB 7.4 MB/s eta 0:00:00\n",
      "Collecting blinker>=1.0.0\n",
      "  Downloading blinker-1.5-py2.py3-none-any.whl (12 kB)\n",
      "Requirement already satisfied: numpy in c:\\users\\legion\\anaconda3\\lib\\site-packages (from streamlit) (1.21.5)\n",
      "Collecting pydeck>=0.1.dev5\n",
      "  Downloading pydeck-0.7.1-py2.py3-none-any.whl (4.3 MB)\n",
      "     ---------------------------------------- 4.3/4.3 MB 7.8 MB/s eta 0:00:00\n",
      "Requirement already satisfied: protobuf<4,>=3.12 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from streamlit) (3.19.1)\n",
      "Requirement already satisfied: pandas>=0.21.0 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from streamlit) (1.4.2)\n",
      "Collecting gitpython!=3.1.19\n",
      "  Downloading GitPython-3.1.27-py3-none-any.whl (181 kB)\n",
      "     -------------------------------------- 181.2/181.2 kB 5.5 MB/s eta 0:00:00\n",
      "Requirement already satisfied: click>=7.0 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from streamlit) (8.0.4)\n",
      "Collecting rich>=10.11.0\n",
      "  Downloading rich-12.5.1-py3-none-any.whl (235 kB)\n",
      "     -------------------------------------- 235.6/235.6 kB 7.3 MB/s eta 0:00:00\n",
      "Collecting pympler>=0.9\n",
      "  Downloading Pympler-1.0.1-py3-none-any.whl (164 kB)\n",
      "     ------------------------------------- 164.8/164.8 kB 10.3 MB/s eta 0:00:00\n",
      "Requirement already satisfied: watchdog in c:\\users\\legion\\anaconda3\\lib\\site-packages (from streamlit) (2.1.6)\n",
      "Requirement already satisfied: pillow>=6.2.0 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from streamlit) (9.0.1)\n",
      "Collecting pyarrow>=4.0\n",
      "  Downloading pyarrow-9.0.0-cp39-cp39-win_amd64.whl (19.6 MB)\n",
      "     --------------------------------------- 19.6/19.6 MB 11.1 MB/s eta 0:00:00\n",
      "Requirement already satisfied: importlib-metadata>=1.4 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from streamlit) (4.11.3)\n",
      "Requirement already satisfied: packaging>=14.1 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from streamlit) (21.3)\n",
      "Requirement already satisfied: toml in c:\\users\\legion\\anaconda3\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions>=3.10.0.0 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from streamlit) (4.1.1)\n",
      "Requirement already satisfied: tornado>=5.0 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from streamlit) (6.1)\n",
      "Collecting validators>=0.2\n",
      "  Downloading validators-0.20.0.tar.gz (30 kB)\n",
      "  Preparing metadata (setup.py): started\n",
      "  Preparing metadata (setup.py): finished with status 'done'\n",
      "Collecting tzlocal>=1.1\n",
      "  Downloading tzlocal-4.2-py3-none-any.whl (19 kB)\n",
      "Collecting semver\n",
      "  Downloading semver-2.13.0-py2.py3-none-any.whl (12 kB)\n",
      "Requirement already satisfied: python-dateutil in c:\\users\\legion\\anaconda3\\lib\\site-packages (from streamlit) (2.8.2)\n",
      "Requirement already satisfied: cachetools>=4.0 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from streamlit) (4.2.2)\n",
      "Requirement already satisfied: requests>=2.4 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from streamlit) (2.27.1)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from altair>=3.2.0->streamlit) (4.4.0)\n",
      "Requirement already satisfied: entrypoints in c:\\users\\legion\\anaconda3\\lib\\site-packages (from altair>=3.2.0->streamlit) (0.4)\n",
      "Requirement already satisfied: toolz in c:\\users\\legion\\anaconda3\\lib\\site-packages (from altair>=3.2.0->streamlit) (0.11.2)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from altair>=3.2.0->streamlit) (2.11.3)\n",
      "Requirement already satisfied: colorama in c:\\users\\legion\\anaconda3\\lib\\site-packages (from click>=7.0->streamlit) (0.4.4)\n",
      "Collecting gitdb<5,>=4.0.1\n",
      "  Downloading gitdb-4.0.9-py3-none-any.whl (63 kB)\n",
      "     ---------------------------------------- 63.1/63.1 kB 3.3 MB/s eta 0:00:00\n",
      "Requirement already satisfied: zipp>=0.5 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from importlib-metadata>=1.4->streamlit) (3.7.0)\n",
      "Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from packaging>=14.1->streamlit) (3.0.4)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from pandas>=0.21.0->streamlit) (2021.3)\n",
      "Requirement already satisfied: traitlets>=4.3.2 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from pydeck>=0.1.dev5->streamlit) (5.1.1)\n",
      "Requirement already satisfied: ipywidgets>=7.0.0 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from pydeck>=0.1.dev5->streamlit) (7.6.5)\n",
      "Requirement already satisfied: ipykernel>=5.1.2 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from pydeck>=0.1.dev5->streamlit) (6.9.1)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from python-dateutil->streamlit) (1.16.0)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from requests>=2.4->streamlit) (1.26.9)\n",
      "Requirement already satisfied: charset-normalizer~=2.0.0 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from requests>=2.4->streamlit) (2.0.4)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from requests>=2.4->streamlit) (2021.10.8)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from requests>=2.4->streamlit) (3.3)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.6.0 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from rich>=10.11.0->streamlit) (2.11.2)\n",
      "Collecting commonmark<0.10.0,>=0.9.0\n",
      "  Downloading commonmark-0.9.1-py2.py3-none-any.whl (51 kB)\n",
      "     ---------------------------------------- 51.1/51.1 kB ? eta 0:00:00\n",
      "Collecting pytz-deprecation-shim\n",
      "  Downloading pytz_deprecation_shim-0.1.0.post0-py2.py3-none-any.whl (15 kB)\n",
      "Collecting tzdata\n",
      "  Downloading tzdata-2022.2-py2.py3-none-any.whl (336 kB)\n",
      "     ------------------------------------- 336.4/336.4 kB 10.2 MB/s eta 0:00:00\n",
      "Requirement already satisfied: decorator>=3.4.0 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from validators>=0.2->streamlit) (5.1.1)\n",
      "Collecting smmap<6,>=3.0.1\n",
      "  Downloading smmap-5.0.0-py3-none-any.whl (24 kB)\n",
      "Requirement already satisfied: ipython>=7.23.1 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (8.2.0)\n",
      "Requirement already satisfied: debugpy<2.0,>=1.0.0 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (1.5.1)\n",
      "Requirement already satisfied: jupyter-client<8.0 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (6.1.12)\n",
      "Requirement already satisfied: matplotlib-inline<0.2.0,>=0.1.0 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.1.2)\n",
      "Requirement already satisfied: nest-asyncio in c:\\users\\legion\\anaconda3\\lib\\site-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (1.5.5)\n",
      "Requirement already satisfied: ipython-genutils~=0.2.0 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.2.0)\n",
      "Requirement already satisfied: widgetsnbextension~=3.5.0 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (3.5.2)\n",
      "Requirement already satisfied: jupyterlab-widgets>=1.0.0 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.0.0)\n",
      "Requirement already satisfied: nbformat>=4.2.0 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (5.3.0)\n",
      "Requirement already satisfied: MarkupSafe>=0.23 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from jinja2->altair>=3.2.0->streamlit) (2.0.1)\n",
      "Requirement already satisfied: attrs>=17.4.0 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (21.4.0)\n",
      "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (0.18.0)\n",
      "Requirement already satisfied: pickleshare in c:\\users\\legion\\anaconda3\\lib\\site-packages (from ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.7.5)\n",
      "Requirement already satisfied: jedi>=0.16 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.18.1)\n",
      "Requirement already satisfied: stack-data in c:\\users\\legion\\anaconda3\\lib\\site-packages (from ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.2.0)\n",
      "Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (3.0.20)\n",
      "Requirement already satisfied: setuptools>=18.5 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (61.2.0)\n",
      "Requirement already satisfied: backcall in c:\\users\\legion\\anaconda3\\lib\\site-packages (from ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.2.0)\n",
      "Requirement already satisfied: jupyter-core>=4.6.0 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from jupyter-client<8.0->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (4.9.2)\n",
      "Requirement already satisfied: pyzmq>=13 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from jupyter-client<8.0->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (22.3.0)\n",
      "Requirement already satisfied: fastjsonschema in c:\\users\\legion\\anaconda3\\lib\\site-packages (from nbformat>=4.2.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (2.15.1)\n",
      "Requirement already satisfied: notebook>=4.4.1 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (6.4.8)\n",
      "Requirement already satisfied: parso<0.9.0,>=0.8.0 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from jedi>=0.16->ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.8.3)\n",
      "Requirement already satisfied: pywin32>=1.0 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from jupyter-core>=4.6.0->jupyter-client<8.0->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (302)\n",
      "Requirement already satisfied: prometheus-client in c:\\users\\legion\\anaconda3\\lib\\site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.13.1)\n",
      "Requirement already satisfied: argon2-cffi in c:\\users\\legion\\anaconda3\\lib\\site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (21.3.0)\n",
      "Requirement already satisfied: Send2Trash>=1.8.0 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.8.0)\n",
      "Requirement already satisfied: terminado>=0.8.3 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.13.1)\n",
      "Requirement already satisfied: nbconvert in c:\\users\\legion\\anaconda3\\lib\\site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (6.4.4)\n",
      "Requirement already satisfied: wcwidth in c:\\users\\legion\\anaconda3\\lib\\site-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.2.5)\n",
      "Requirement already satisfied: pure-eval in c:\\users\\legion\\anaconda3\\lib\\site-packages (from stack-data->ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.2.2)\n",
      "Requirement already satisfied: asttokens in c:\\users\\legion\\anaconda3\\lib\\site-packages (from stack-data->ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (2.0.5)\n",
      "Requirement already satisfied: executing in c:\\users\\legion\\anaconda3\\lib\\site-packages (from stack-data->ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.8.3)\n",
      "Requirement already satisfied: pywinpty>=1.1.0 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from terminado>=0.8.3->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (2.0.2)\n",
      "Requirement already satisfied: argon2-cffi-bindings in c:\\users\\legion\\anaconda3\\lib\\site-packages (from argon2-cffi->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (21.2.0)\n",
      "Requirement already satisfied: defusedxml in c:\\users\\legion\\anaconda3\\lib\\site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.7.1)\n",
      "Requirement already satisfied: pandocfilters>=1.4.1 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.5.0)\n",
      "Requirement already satisfied: testpath in c:\\users\\legion\\anaconda3\\lib\\site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.5.0)\n",
      "Requirement already satisfied: beautifulsoup4 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (4.11.1)\n",
      "Requirement already satisfied: mistune<2,>=0.8.1 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.8.4)\n",
      "Requirement already satisfied: bleach in c:\\users\\legion\\anaconda3\\lib\\site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (4.1.0)\n",
      "Requirement already satisfied: nbclient<0.6.0,>=0.5.0 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.5.13)\n",
      "Requirement already satisfied: jupyterlab-pygments in c:\\users\\legion\\anaconda3\\lib\\site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.1.2)\n",
      "Requirement already satisfied: cffi>=1.0.1 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from argon2-cffi-bindings->argon2-cffi->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.15.0)\n",
      "Requirement already satisfied: soupsieve>1.2 in c:\\users\\legion\\anaconda3\\lib\\site-packages (from beautifulsoup4->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (2.3.1)\n",
      "Requirement already satisfied: webencodings in c:\\users\\legion\\anaconda3\\lib\\site-packages (from bleach->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.5.1)\n",
      "Requirement already satisfied: pycparser in c:\\users\\legion\\anaconda3\\lib\\site-packages (from cffi>=1.0.1->argon2-cffi-bindings->argon2-cffi->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (2.21)\n",
      "Building wheels for collected packages: validators\n",
      "  Building wheel for validators (setup.py): started\n",
      "  Building wheel for validators (setup.py): finished with status 'done'\n",
      "  Created wheel for validators: filename=validators-0.20.0-py3-none-any.whl size=19582 sha256=4ec9b8d318b7940f101de5e322b1372a12a991a0e21ae850c9724e047ccc6e97\n",
      "  Stored in directory: c:\\users\\legion\\appdata\\local\\pip\\cache\\wheels\\2d\\f0\\a8\\1094fca7a7e5d0d12ff56e0c64675d72aa5cc81a5fc200e849\n",
      "Successfully built validators\n",
      "Installing collected packages: commonmark, validators, tzdata, smmap, semver, rich, pympler, pyarrow, blinker, pytz-deprecation-shim, gitdb, tzlocal, gitpython, altair, pydeck, streamlit\n",
      "Successfully installed altair-4.2.0 blinker-1.5 commonmark-0.9.1 gitdb-4.0.9 gitpython-3.1.27 pyarrow-9.0.0 pydeck-0.7.1 pympler-1.0.1 pytz-deprecation-shim-0.1.0.post0 rich-12.5.1 semver-2.13.0 smmap-5.0.0 streamlit-1.12.0 tzdata-2022.2 tzlocal-4.2 validators-0.20.0\n",
      "\n",
      "[notice] A new release of pip available: 22.2 -> 22.2.2\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2022-08-17 13:48:00.132 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\Legion\\anaconda3\\lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "!pip install streamlit\n",
    "import streamlit as st\n",
    "from sqlalchemy import create_engine\n",
    "import pandas as pd\n",
    "import pymysql\n",
    "\n",
    "masina = create_engine(\"mysql+pymysql://data-student:u9AB6hWGsNkNcRDm@data.engeto.com:3306/data_academy_04_2022\")\n",
    "\n",
    "data = pd.read_sql(sql='WITH odjezdy AS (SELECT count(`start_station_name`) AS pocet_odjezdu,`start_station_name` AS nazev_stanice FROM edinburgh_bikes GROUP BY `start_station_name` ORDER BY count(`start_station_name`) DESC) SELECT * FROM odjezdy', con=masina)\n",
    "data2 = pd.read_sql(sql='WITH prijezdy AS (SELECT count(`end_station_name`) AS pocet_prijezdu,`end_station_name` AS nazev_stanice FROM edinburgh_bikes GROUP BY `end_station_name` ORDER BY count(`end_station_name`) DESC) SELECT * FROM prijezdy', con=masina)\n",
    "\n",
    "st.title('Python projekt na téma Bike Sharing v Edinburku')\n",
    "\n",
    "stranka = st.sidebar.radio('Vybrat úkol', ['První úkol','Druhý úkol'])\n",
    "\n",
    "if stranka == 'První úkol':\n",
    "    st.write('Zobrazení aktivních a neaktivních stanic')\n",
    "    data_f = pd.DataFrame(data)\n",
    "    data_f = data_f.set_index(['nazev_stanice'])\n",
    "    data_f2 = pd.DataFrame(data2)\n",
    "    data_f2 = data_f2.set_index(['nazev_stanice'])\n",
    "    data_f3 = data_f.join(data_f2, how='right')\n",
    "    data_f3[:10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a2a358c7",
   "metadata": {},
   "outputs": [],
   "source": [
    "if stranka == 'Druhý úkol':\n",
    "    st.write('Načítá se ...')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
