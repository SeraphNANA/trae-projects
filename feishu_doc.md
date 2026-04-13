# AI智能体工具分享：【Trae】安装部署和使用教程

## 一、工具总览：各工具核心用途

在搭建前，先明确工具的核心定位，避免混淆使用场景，精准匹配你的需求：

- Trae：一款集成 AI 能力的轻量 IDE（集成开发环境），主打改写文件、项目管理，支持连接 Github 等文件仓库，可实现文件的克隆、提交、推送等版本控制操作，同时提供 IDE 模式（自主开发）和 SOLO 模式（AI 主导开发），适配各类开发场景，无需复杂配置即可快速上手修改文件开与项目管理工作。


【推荐理由】：Trae 是一款高效的AI 文档处理与可视化工具，能快速帮你处理各类文档、自动改写优化内容，让文本更通顺、结构更清晰。它支持实时预览与可视化编辑，操作简单、响应快，不用复杂设置就能把杂乱内容整理成规范、易读的成品文档，大幅提升写作与整理效率。

同时支持对接 GitHub 仓库，可自动同步操作日志，方便版本追溯、协作管理和流程记录，兼顾易用性与工程化规范。

## 二、详细搭建与使用流程（按工具顺序）

### 工具一：Trae（含 Github 仓库创建与连接）

#### 1. 工具核心用途补充

Trae 支持 Windows、macOS、Linux 全系统，深度集成 Git 功能，无需记忆复杂命令，通过图形化界面即可完成文件版本控制，同时内置智能体和 CUE 智能编程助手，可实现文件（各种格式）补全、修改、跳转等功能，搭配 Github 可实现文件云端备份、团队协作与项目同步，是开发者的高效工具。

#### 2. 前期准备

- 设备要求：Windows 10/11（64位）、macOS 12.0 及以上、Linux（64位 x64/ARM64），确保设备硬盘可用空间≥10GB，内存≥4GB（推荐8GB及以上）。
- 必备账号：手机号或稀土掘金账号（用于登录 Trae）；Github 账号（用于创建仓库、与 Trae 连接，无账号需先注册）。
- 环境准备：安装 Git（Trae 连接 Github 必需，后续步骤会详细说明安装方法）。
#### 3. 搭建步骤（注册+下载+安装+初始化）

##### 步骤1：注册 Trae 账号

1. 打开浏览器，访问 Trae 官网（https://docs.trae.cn/），点击右上角「下载 IDE」旁的「登录/注册」按钮。
![图片](https://open.feishu.cn/open-apis/docx/v1/images/MbUyb4UWZodyPjx9sQ3c0u8UnDc/download)

1. 选择注册方式：支持「手机号注册」或「稀土掘金账号登录」（推荐手机号注册，更便捷）。
1. 手机号注册：输入手机号，获取验证码，设置登录密码，勾选用户协议，点击「注册并登录」；掘金账号登录：点击「掘金登录」，跳转后授权即可完成登录（无需额外注册）。
##### 步骤2：下载并安装 Trae

1. 登录后，官网会自动识别你的设备系统，点击「下载 IDE」，下载对应系统的安装包（Windows 为 .exe 文件，macOS 为 .dmg 文件，Linux 为 .deb 或 .rpm 文件）。
1. 安装 Trae
- Windows：找到下载的 .exe 安装包，双击运行，选择安装路径（建议默认路径，避免中文路径），点击「下一步」，直至安装完成，桌面会生成快捷方式。
- macOS：双击 .dmg 文件，将 Trae 图标拖入「应用程序」文件夹，完成安装；若提示“无法打开，Apple 无法检查其是否包含恶意软件”，前往「系统设置→隐私与安全」，在安全性栏点击「仍要打开」完成授权。
- Linux：根据系统类型，使用对应命令安装（如 Ubuntu 系统，终端输入 sudo dpkg -i 安装包名称.deb，按提示完成操作）。
##### 步骤3：Trae 初始化配置

1. 双击打开 Trae 客户端，使用刚才注册的账号（手机号/掘金账号）登录。
1. 跟随界面指引完成初始设置：
- 选择主题（浅色/深色）和界面语言（默认中文，可按需调整）。
- 可选：从 VS Code 或 Cursor 导入已有配置（无相关配置可点击「跳过」）。
（此步骤新手可以跳过，大多数同学之前没有使用过 VS Code 或 Cursor，这一步是方便同步在此两款工具上的配置同步。）

- 添加 Trae 命令行（默认自动添加，点击「确认」即可）。
1. 初始化完成后，进入 Trae 主界面，左侧为活动栏（包含文件、源代码管理等功能），中间为编辑区，底部为终端面板，至此 Trae 基础搭建完成。
![图片](https://open.feishu.cn/open-apis/docx/v1/images/I8Jtbo990oeXp0xQnT9ciatXnDf/download)

##### 步骤4：安装并配置 Git（连接 Github 必需）

1. 检查 Git 是否已安装：打开 Trae 底部的终端面板（如没有可点击右上角红框处呼出面板），输入命令 git --version，按回车。若显示 Git 版本号（如 git version 2.43.0），说明已安装；若未显示，需先下载安装。
![图片](https://open.feishu.cn/open-apis/docx/v1/images/YQ4nbDajXoGoyTxZjPKciV4vnGh/download)

1. 下载安装 Git：
- 访问 Git 官网（https://git-scm.com/），点击「Downloads」，下载对应系统的安装包。
- 安装时全程点击「下一步」，默认配置即可（建议勾选「Add Git to PATH」，方便后续在终端使用 Git 命令）。
1. 如何克隆Git仓库：
1. 打开Trae主界面，直接点击面板中的「克隆Git仓库」按钮，弹出克隆窗口，窗口会直接提示填写「仓库URL或选择仓库源」。此时需要Github仓库的URL链接，先放在这，我们先去创建Github账号和仓库。
![图片](https://open.feishu.cn/open-apis/docx/v1/images/LxXHbJx4VoaQ8Rx6lJmcrsSBnLb/download)

1. 创建Github账号（无账号需先操作）：
*此时有VPN会更快操作完成，直接访问也可以，但经常会卡顿或无法链接，需要多尝试几次。
打开浏览器，访问Github官网（https://github.com/signup），点击“Accept”接受；

![图片](https://open.feishu.cn/open-apis/docx/v1/images/HMMFb0bLRocJsLxIMWycy7aCnO8/download)

![图片](https://open.feishu.cn/open-apis/docx/v1/images/KtVZbQzeAo1HFSx1ooqcDQ2unfe/download)

1. 输入常用邮箱（最好是有Google邮箱，直接点击“Continue with Google”）、设置登录密码（建议包含字母、数字和特殊符号，提升安全性）、自定义Github用户名（简洁易记，避免中文和特殊符号），填写信息后点击黑框“Create account”创建账户。
1. 完成邮箱验证：Github会向填写的邮箱发送验证邮件，打开邮件点击验证链接，即可完成账号注册并登录。
1. 创建Github仓库（获取仓库URL的前提）：
       登录Github后，点击右上角的「+」图标，选择「New repository」（新建仓库）。
![图片](https://open.feishu.cn/open-apis/docx/v1/images/B47fbjVB9oO6qMx0Z3PcCvGGnEg/download)

1. 填写仓库基础信息：
Repository name（仓库名称）：输入简洁易记的名称，建议与后续Trae项目名称一致（如“trae-test-project”），禁止中文和特殊符号。
1. Description（仓库描述，可选）：简要填写仓库用途（如“Trae测试项目，用于学习Trae与Github连接”）。
1. Visibility（仓库可见性）：新手推荐选择「Public」（公开），方便测试；若需隐私保护，可选择「Private」（私有）。
1. 勾选「Add a README file」（添加说明文件，便于后续管理），其他选项默认不勾选。
1. 点击页面底部「Create repository」，即可完成Github仓库创建，自动跳转至仓库详情页。
![图片](https://open.feishu.cn/open-apis/docx/v1/images/ILkLbHhhLorGDMxlMxMcLAZ7nLc/download)

1. 获取Github仓库URL（回填至Trae克隆窗口）：
      刚创建好的Github仓库，会直接进入此页面，红框中即为你要获取的URL的位置，但注意，默认是HTTPS，需要手动点选「SSH」选项（后续配置SSH密钥后可实现免密连接），点击URL旁的「复制」图标，即可复制仓库SSH URL（格式为git@github.com:用户名/仓库名.git）

*如不小心跳转到了你的Github主页，如图

![图片](https://open.feishu.cn/open-apis/docx/v1/images/K9U3bVuqAocQ20xMCvycIesOnHc/download)

你可以在这里看到你已经创建的仓库，找到对应的仓库点击标题进去，点绿色的「Code」按钮，弹出下拉菜单。

你依然可以获取到SSH链接。



##### 步骤5：Trae 连接（克隆）Github 仓库

克隆仓库即把 Github 云端的仓库复制到 Trae 本地，方便在 Trae 中编辑文件内容、提交修改，有两种方式，新手推荐图形化方式，无需输入命令。回到你的Trae界面，点击克隆Git仓库，弹出弹窗，回填你刚复制的URL。

![图片](https://open.feishu.cn/open-apis/docx/v1/images/ZHrqbrIPBooMGgxcBZRcaAY2nuh/download)

点击“从Github克隆”这条👆，会让你选择你刚创建的仓库👇

![图片](https://open.feishu.cn/open-apis/docx/v1/images/GCInbBw2Xo2PeExxNYNc92BDnre/download)

点选你新创建的仓库名条目👆，会弹出弹窗，让你存储库目标位置👇

![图片](https://open.feishu.cn/open-apis/docx/v1/images/DTeMb889so6IUcx6rBzcCO0zn1g/download)

此时创建一个新建文件夹，与你的Github仓库同名即可，新建完成后，点选“选择为存储库目标”，创建完成后Trae页面会弹出弹窗👇，点击是，我信任此作者。

![图片](https://open.feishu.cn/open-apis/docx/v1/images/BQJ6b16nYoPuOHx47excJSfqn0f/download)

此时创建完成，你已经进入了你的本地仓库，随便创建一个任务，在右下默认为@Builder 这个agent，和他用自然语言对话即可。👇

![图片](https://open.feishu.cn/open-apis/docx/v1/images/AyBabZECzoPMvDxHlR8cJU6Fnhb/download)



当任务执行完成后，会在“编码区”中间的框内，显示你的文件内容，可进行编辑，两个地方都可以选择“保留”或“全部保留”，区别是，编码区内的保留可以圈选部分内容保留，一般选择全部保留即可。

![图片](https://open.feishu.cn/open-apis/docx/v1/images/QGWnbQrfDo3qzwxJvPjcpW16nYO/download)

然后点选上图中红圈⭕️的位置👆，【源代码管理】功能，左侧框会出现👇，“红方框”你的本次修改记录日志，点击“提交”，即会将这次历史版本文件同步到你的Github对应的仓库中。

![图片](https://open.feishu.cn/open-apis/docx/v1/images/Q22XbovhKoVcjnxSWqAc43i2n1b/download)



这一步操作的核心目的是，在你每次修改任务后，Trae都会形成一个工作日志，你提交到GitHub仓库进行保存，方便在你执行错误，或者需要找回历史版本时，可以直接调取Github仓库中的这段日志记录，挽回错误操作。



#### 4. Trae 核心使用流程（含 Github 仓库操作）

##### （1）基础操作：打开/新建项目

- 打开已有项目：点击 Trae 顶部「文件→打开文件夹」，选择本地项目文件夹（或克隆后的 Github 仓库文件夹），即可打开。
- 新建项目：点击「文件→新建文件夹」，命名项目文件夹，然后在 Trae 中打开该文件夹，点击左侧「源代码内容管理→初始化仓库」，即可创建本地 Git 仓库，后续可关联到 Github 云端仓库。
##### （2）模式切换：IDE 模式与 SOLO 模式

- IDE 模式（默认）：传统开发模式，全程自主控制文件编辑、修改、提交，适合有开发基础的用户，可手动编写文件、调试程序。
- SOLO 模式：AI 主导开发模式，点击 Trae 左上角「模式切换」按钮，切换到 SOLO 模式，输入需求（如“编写一个简单的 Python 计算器程序”），AI 会自动规划任务、生成代码文件、测试程序，适合新手快速完成开发任务。
##### （3）Github 仓库关联与文件提交/推送（核心操作）

当在 Trae 中修改文件后，需将修改同步到 Github 云端仓库，步骤如下：

1. 暂存修改：在 Trae 左侧「源代码管理」面板，会显示修改后的文件，点击文件旁的「+」号，将修改的内容暂存（暂存即告诉 Git“我要提交这些修改”）。
1. 提交修改：在面板下方的「消息」输入框中，输入提交信息（简要描述修改内容，如“修改 README.md 文件，添加项目说明”），也可点击输入框旁的「AI 图标」，让 Trae 自动生成规范的提交信息。
1. 推送修改：点击「提交」按钮右侧的「推送」按钮（或输入命令 git push），将本地修改同步到 Github 云端仓库。
1. 拉取修改：若 Github 仓库有其他人的修改，需同步到本地，点击「拉取」按钮（或输入命令 git pull），即可将云端修改同步到 Trae 本地。
##### 



## 📖 写在最后：

### 关于Trae自带的4个Agent：

一句话速览（先记结论），常用Builder，如觉得任务比较复杂，也可用Solo Coder先进行任务规划。

---

### 关于基础操作：

-可参考：

 https://www.xiaohongshu.com/discovery/item/67c97498000000001203d613?source=webshare&xhsshare=pc_web&xsec_token=CB7dsJyjlc3ikRk1dP5iCOuaAojqS3DfyHhudEaNTstsg=&xsec_source=pc_share



