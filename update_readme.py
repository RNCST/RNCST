import feedparser

url = "https://rrrrrrrrrnnn.tistory.com/rss"
rss_feed = feedparser.parse(url)

MAX_POST_NUM = 10

latest_blog_post_list = ""

MAX_POST_NUM = 10

for idx, feed in enumerate(rss_feed['entries']):
    if idx > MAX_POST_NUM:
        break
    feed_date = feed['published_parsed']
#     latest_blog_post_list += f"[{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']}) <br>\n"
    latest_blog_post_list += f"[{feed['title']}]({feed['link']}) <br>\n"

markdown_text = """[resume]: https://img.shields.io/static/v1?style=plastic&logoWidth=30&color=000000&logoColor=ffffff&label=&message=Resume&logo=notion&#000000
[blog]: https://img.shields.io/static/v1?style=plastic&logoWidth=30&color=00c7b7&logoColor=ffffff&label=&message=Blog&logo=blogger&#00C7B7
[linkedin]: https://img.shields.io/static/v1?style=plastic&logoWidth=30&color=0077b5&logoColor=ffffff&label=&message=LinkedIn&logo=linkedin&#0077B5
[WebPortfolio]: https://img.shields.io/static/v1?style=plastic&logoWidth=30e&color=6236FF&logoColor=ffffff&label=&message=WebPortfolio&logo=Netlify&#6236FF
[gmail]: https://img.shields.io/static/v1?style=plastic&logoWidth=30e&color=FE9700&logoColor=ffffff&label=&message=gmail&logo=gmail&#6236FF


<h1 title="rncst title"> Hey 👋, I'm Sehyeon Oh</h1>

[![gmail]](mailto:rk51320928@gmail.com)
[![Resume]](https://www.notion.so/5aa790d2f44340049e03b17ecca4477d)
[![Blog]](https://rrrrrrrrrnnn.tistory.com/)
[![LinkedIn]](https://www.linkedin.com/in/%EC%84%B8%ED%98%84-%EC%98%A4-1438721b9/?originalSubdomain=in#%20add%20your%20Linkedin%20handle)
[![WebPortfolio]](https://rncstportfolio.netlify.app/)

<!--<a href="https://solved.ac/rk51320">
    <img align="right"  height="auto" src="http://mazassumnida.wtf/api/v2/generate_badge?boj=rk51320"/>
</a> -->

<a href="https://leetcode.com/RNCST/">
    <img align="right" height= "150" src="https://leetcode-stats-six.vercel.app/api?username=RNCST&theme=dark"/>
</a>
<!-- <img align="right" alt="GIF" height="250px" src="https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif"/> -->

- 🎯 Goal(2021): Start & Work In IT
- 🎯 Goal(2022): Study Algorithm, Front-End & Move to Front-End
- 🎯 Goal(20xx): Reliable Developer 


**Try to Use Languages and Tools:**  

![Java](http://img.shields.io/badge/-Java-5B4638?style=flat&-square&logo=java&logoColor=ffffff)
![JavaScript](https://img.shields.io/badge/-JavaScript-%23F7DF1C?style=flat&-square&logo=javascript&logoColor=000000&labelColor=%23F7DF1C&color=%23FFCE5A)
![Bootstrap](https://img.shields.io/badge/-Bootstrap-563D7C?style=flat&-square&logo=Bootstrap)
![Vue](https://img.shields.io/badge/-Vue-4FC08D?style=flat&-square&logo=Vue.js&logoColor=ffffff)

<!-- ![Nodejs](https://img.shields.io/badge/-Nodejs-339933?style=fla&t-square&logo=Node.js&logoColor=ffffff)
![HTML5](https://img.shields.io/badge/-HTML5-%23E44D27?style=flat&-square&logo=html5&logoColor=ffffff)
![CSS3](https://img.shields.io/badge/-CSS3-%231572B6?style=flat&-square&logo=css3)
![Sass](https://img.shields.io/badge/-Sass-%23CC6699?style=flat&-square&logo=sass&logoColor=ffffff)
![TypeScript](http://img.shields.io/badge/-TypeScript-3776AB?style=flat&-square&logo=TypeScript&logoColor=ffffff)
![React](https://img.shields.io/badge/-React-61DAFB?style=flat-square&logo=react&logoColor=ffffff)
![Excel](http://img.shields.io/badge/-Excel-217346?style=flat&-square&logo=MicrosoftExcel&logoColor=ffffff)
![GoogleSheets](http://img.shields.io/badge/-GoogleSheets-34A853?style=flat&-square&logo=GoogleSheets&logoColor=ffffff)
![R](http://img.shields.io/badge/-R-276DC3?style=flat&-square&logo=R&logoColor=ffffff)
![Python](https://img.shields.io/badge/-Python-61DAFB?style=flat-square&logo=Python&logoColor=ffffff)
![PostgreSQL](http://img.shields.io/badge/-PostgreSQL-4169E1?style=flat&-square&logo=PostgreSQL&logoColor=ffffff)
![DBeaver](http://img.shields.io/badge/-DBeaver-362722?style=flat&-square&logoColor=ffffff)
![Npm](https://img.shields.io/badge/-npm-CB3837?style=flat&-square&logo=npm)
![Oracle](https://img.shields.io/badge/-Oracle-F80000?style=flat&-square&logo=Oracle)
![ApacheTomcat](https://img.shields.io/badge/-Apache_Tomcat-F8DC75?style=flat&-square&logo=apache-tomcat&logoColor=181717)
![Git](https://img.shields.io/badge/-Git-%23F05032?style=flat&-square&logo=git&logoColor=%23ffffff)
![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat&-square&logo=github)
![GitLab](https://img.shields.io/badge/-GitLab-FCA121?style=flat&-square&logo=gitlab)
![VS Code](http://img.shields.io/badge/-VS%20Code-007ACC?style=flat&-square&logo=visual-studio-code&logoColor=ffffff)
![Eclipse-IDE](http://img.shields.io/badge/-Eclipse-2C2255?style=flat&-square&logo=eclipse&logoColor=ffffff)
![IntelliJ-IDEA](http://img.shields.io/badge/-intelliJ(Community)-2C2255?style=flat&-square&logo=IntelliJ%20IDEA&logoColor=ffffff)
![Powershell](http://img.shields.io/badge/-Powershell-5391FE?style=flat&-square&logo=powershell&logoColor=ffffff)
![cmd](http://img.shields.io/badge/-cmder-5391FE?style=flat&-square&logo=powershell&logoColor=ffffff)
![SLACK](https://img.shields.io/badge/-SLACK-4A154B?style=flat&-square&logo=Slack)
![NOTION](https://img.shields.io/badge/-Notion-000000?style=flat&-square&logo=Notion)
![CodePen](https://img.shields.io/badge/-CodePen-000000?style=flat&-square&logo=CodePen)
![Figma](https://img.shields.io/badge/-Figma-F24E1E?style=flat&-square&logo=Figma&logoColor=ffffff) -->
<!-- Search icon here https://simpleicons.org/?q=IntelliJ%20IDEA -->





<details open="">
<summary>
  <g-emoji class="g-emoji" alias="chart_with_upwards_trend" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f4c8.png">📈</g-emoji> 
  <strong>Github Stats : </strong>
</summary>
<br>
  
<p align="center">
<a href="https://github.com/RNCST">
  <img width=450 height=170 align="center" src="https://github-readme-stats.vercel.app/api?username=rncst&theme=midnight-purple&show_icons=true&bg_color=0D1117&hide_border=true" />
</a>
<a href="https://github.com/RNCST">
  <img align="center" src="https://github-readme-stats.vercel.app/api/top-langs/?username=rncst&exclude_repo=RNCST.github.io,awesome-devteam,k80proj_0525-0719&theme=midnight-purple&langs_count=6&layout=compact&hide=css,html,scss&bg_color=0D1117&hide_border=true" />
</a>
</p>
</details>
<br>

<div align="center">
  
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FRNCST&count_bg=%234FC08D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

</div>
 
----

## Latest Blog Post 
""" 

readme_text = f"{markdown_text}{latest_blog_post_list}"

with open("README.md", 'w', encoding='utf-8') as f:
  f.write(readme_text)
