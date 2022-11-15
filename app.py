import requests
import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# setting app's title, icon & layout
st.set_page_config(page_title="Github Scraper", page_icon="🎯")


def scrape_data(user_name):
    url = f"https://github.com/{user_name}?tab=repositories"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    info = {"name": soup.find(class_="vcard-fullname").get_text()}
    info["image_url"] = soup.find(class_="avatar-user")["src"]
    info["followers"] = (
        soup.select_one("a[href*=followers]").get_text().strip().split("\n")[0]
    )
    info["following"] = (
        soup.select_one("a[href*=following]").get_text().strip().split("\n")[0]
    )

    try:
        info["location"] = soup.select_one("li[itemprop*=home]").get_text().strip()
    except Exception:
        info["location"] = ""

    try:
        info["url"] = soup.select_one("li[itemprop*=url]").get_text().strip()
    except Exception:
        info["url"] = ""

    repositories = soup.find_all(class_="source")
    repo_info = []
    for repo in repositories:
        try:
            name = repo.select_one("a[itemprop*=codeRepository]").get_text().strip()
            link = f"https://github.com/{user_name}/{name}"
        except Exception:
            name = ""
            link = ""

        try:
            updated = repo.find("relative-time").get_text()
        except Exception:
            updated = ""

        try:
            language = repo.select_one("span[itemprop*=programmingLanguage]").get_text()
        except Exception:
            language = ""

        try:
            description = repo.select_one("p[itemprop*=description]").get_text().strip()
        except Exception:
            description = ""

        repo_info.append(
            {
                "name": name,
                "link": link,
                "updated ": updated,
                "language": language,
                "description": description,
            }
        )
    repo_info = pd.DataFrame(repo_info)
    return info, repo_info


def main():
    # display app header
    st.header("Github Scraper")
    if username := st.text_input("Enter your github username : "):
        try:
            info, repo_info = scrape_data(username)

            for key, value in info.items():
                if key != "image_url":
                    st.sidebar.write(
                        """
                        {} : {}
                        """.format(
                            key, value
                        )
                    )
                else:
                    st.sidebar.image(value)
            st.subheader("Recent Repositories")
            with st.expander("CSV Format"):
                st.dataframe(repo_info)
                st.download_button(
                    label="Download data as CSV",
                    data=repo_info.to_csv(),
                    file_name="df.csv",
                    mime="text/csv",
                )
            with st.expander("JSON Format"):
                st.json(repo_info.to_json())
                st.download_button(
                    label="Download data as JSON",
                    data=repo_info.to_csv(),
                    file_name="df.json",
                    mime="text/json",
                )
            with st.expander("HTML Report"):
                report = ProfileReport(repo_info)
                st_profile_report(report)
                st.download_button(
                    label="Download HTML report",
                    data=report.to_html(),
                    file_name="df_report.html",
                    mime="text/html",
                )
        except Exception:
            st.subheader("User doesn't exist")
    else:
        st.info("Please, Enter a github profile username...")


if __name__ == "__main__":
    main()  # calls the main() first
