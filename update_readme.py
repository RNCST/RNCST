import feedparser

url = "https://rrrrrrrrrnnn.tistory.com/feed"
rss_feed = feedparser.parse(url)

MAX_POST_NUM = 10 
latest_blog_post_list = "" 
MAX_POST_NUM = 10 
for idx, feed in enumerate(rss_feed['entries']):
   if idx > MAX_POST_NUM: 
     break 
     
     feed_date = feed['published_parsed'] 

     latest_blog_post_list += f"[{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']}) <br>\n" 

     markdown_text = """
     <h1 title="rncst title"> Hey 👋, I'm Sehyeon Oh</h1>

<h3> below my linkedin/github/blog/instagram/webportfolio  </h3> 
<br>

<a href="https://www.linkedin.com/in/%EC%84%B8%ED%98%84-%EC%98%A4-1438721b9/?originalSubdomain=in#%20add%20your%20Linkedin%20handle">
  <img align="left" alt="osh's LinkedIn" width="24px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />
</a>
<a href="https://github.com/RNCST">
  <img align="left" alt="osh's github" width="24px" src="https://cdn.jsdelivr.net/npm/simple-icons@3.13.0/icons/github.svg" />
</a>
<a href="https://rncst.github.io/">
  <img align="left" alt="osh's Facebook" width="24px" src="https://cdn.jsdelivr.net/npm/simple-icons@3.13.0/icons/blogger.svg" />
</a>
<a href="https://www.instagram.com/ddbbosh/">
  <img align="left" alt="osh's LinkedIn" width="24px" src="https://cdn.jsdelivr.net/npm/simple-icons@3.13.0/icons/instagram.svg" >
</a>
<a href="https://rncstportfolio.netlify.app/">
  <img align="left" alt="osh's web portfolio" width="24px" src="https://cdn.jsdelivr.net/npm/simple-icons@3.13.0/icons/pagerduty.svg" >
</a>





<br/>
<h2> </h2>

Want To Be **WEB-APP JUNIOR DEVELOPMENT** ***Enthusiast*** 🚀.
 

<!--   <img align="right" alt="GIF" src="https://i.pinimg.com/originals/e4/26/70/e426702edf874b181aced1e2fa5c6cde.gif" /> -->
  
<img align="right" alt="GIF" height="250px" src="https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif"/>



**About Me!**

- 👨🏽‍💻 I’m Studying about WEB-APP DEVELOP
- 🤔 My interest lies in front-end web development
- 💬 Contact me about anything! 
- 💪🏼 Future Goals: Learn more technologies
- 📫 Email me at [rk51320928@gmail.com](mailto:rk51320928@gmail.com). 


**Try to Use Languages and Tools:**  

![Java](http://img.shields.io/badge/-Java-5B4638?style=flat&-square&logo=java&logoColor=ffffff)
![Nodejs](https://img.shields.io/badge/-Nodejs-339933?style=fla&t-square&logo=Node.js&logoColor=ffffff)
<!-- ![C](http://img.shields.io/badge/-C-A8B9CC?style=flat-square&logo=c&logoColor=ffffff) -->
![HTML5](https://img.shields.io/badge/-HTML5-%23E44D27?style=flat&-square&logo=html5&logoColor=ffffff)
![CSS3](https://img.shields.io/badge/-CSS3-%231572B6?style=flat&-square&logo=css3)
![Sass](https://img.shields.io/badge/-Sass-%23CC6699?style=flat&-square&logo=sass&logoColor=ffffff)
![Bootstrap](https://img.shields.io/badge/-Bootstrap-563D7C?style=flat&-square&logo=Bootstrap)

![JavaScript](https://img.shields.io/badge/-JavaScript-%23F7DF1C?style=flat&-square&logo=javascript&logoColor=000000&labelColor=%23F7DF1C&color=%23FFCE5A)
![TypeScript](http://img.shields.io/badge/-TypeScript-3776AB?style=flat&-square&logo=TypeScript&logoColor=ffffff)
![Vue](https://img.shields.io/badge/-Vue-4FC08D?style=flat&-square&logo=Vue.js&logoColor=ffffff)
<!-- ![React](https://img.shields.io/badge/-React-61DAFB?style=flat-square&logo=react&logoColor=ffffff) -->

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
![Figma](https://img.shields.io/badge/-Figma-F24E1E?style=flat&-square&logo=Figma&logoColor=ffffff)
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
  <img align="center" src="https://github-readme-stats.vercel.app/api/top-langs/?username=rncst&theme=midnight-purple&langs_count=8&bg_color=0D1117&hide_border=true" />
</a>
</p>
</details>
<br>

----

## Latest Blog Post 

     """ 

     readme_text = f"{markdown_text}{latest_blog_post_list}" 
     
     with open("README.md", 'w', encoding='utf-8') as f:
         f.write(readme_text)