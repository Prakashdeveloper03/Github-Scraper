# Github Scraper
![made-with-python](https://img.shields.io/badge/Made%20with-Python-0078D4.svg)
![pandas](https://img.shields.io/badge/Pandas-2C2D72?logo=pandas&logoColor=white)
![streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=Windows%20terminal&logoColor=white)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?&logo=visual%20studio%20code&logoColor=white)

Github scraper app is used to scrape public data for a specific github user profile. You can download the scraped data in `csv`, `json` and pandas profiling `html` report formats.

## Installation
Open command prompt and create new environment
```
conda create -n your_env_name python=<version>
```
Then Activate the newly created environment
```
conda activate your_env_name
```
Clone the repository using `git`
```
git clone https://github.com/Prakashdeveloper03/Github-Scraper.git
```
Change to the cloned directory
```
cd <directory_name>
```
Then install all requirement packages for the app
```
pip install -r requirements.txt
```
Then, Run the `app.py` script
```
streamlit run app.py
```