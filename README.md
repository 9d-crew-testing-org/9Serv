# 9Serv
A WebTV Server based on [WTV-FRAMEWORK](https://github.com/SachaTending/wtv-framework/) by SachaTending.  
Currently incomplete, see todo list below.
## Why?
[minisrv](https://github.com/zefie/zefie_wtvp_minisrv), while an amazing project, is built on node.js and may be unappealing to those who want a server that's lightweight and easy to tinker with.  
9Serv aims to provide a mostly functioning WebTV server with less complexity and a pure Python codebase, hopefully making hosting a custom WebTV Server easier are more accessible.
## Quick Start
Clone the repository, and run `main.py` in any current version of [Python](https://www.python.org/).
## Todo List
- MAME/Real Box Support.
- HTTP/HTTPS Proxy, needed for real units to brows the internet and for any HTTPS websites to work.
- Unlocking the OPTIONS panel on login. (wtv-framework doesn't but it's newer cousin [pysrv](https://github.com/SachaTending/webtv_pysrv/tree/main) does, need to look into.)
- General improvements to the base WTV-FRAMEWORK engine.
