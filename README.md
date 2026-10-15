# 美赛建模 Skill · Python

`mcm-python` 是一套用于 **MCM/ICM 美赛**的 Codex Skill，支持备赛训练、历史题练习、建模求解和论文整理。

默认 **中文讨论、Python 计算、英文论文**。核心流程是：读题拆解 → 数据与假设 → 基线模型 → 求解与验证 → 结果解释 → 论文与提交检查。

## 能做什么

| 阶段 | 工作内容 |
|---|---|
| 读题与选题 | 拆分题目要求，比较数据可得性、团队能力和时间成本 |
| 数据处理 | 保存原始数据，记录来源、单位、缺失处理和建模假设 |
| 建模求解 | 从可解释基线出发，选择机理、优化、预测、评价等适合的方法 |
| 模型验证 | 解析特例、约束检查、留出验证、敏感性和不确定性分析 |
| 论文写作 | 根据实际计算结果组织英文论文、摘要、表格、图和附加材料 |
| 数学排版 | 成品公式使用正常分式、上下标和希腊字母，并检查渲染效果 |
| 提交检查 | 核验当届规则、格式、页数、引用、匿名性和 AI 使用披露 |

它提供工作流程、参考说明和项目模板。具体模型需要结合题目建立；论文结论必须来自可核验的计算。

## 安装

需要支持本地 Skills 的 Codex 环境。Python 用于运行项目脚本；Git 用于克隆仓库。联网查题、获取外部数据、安装依赖和生成 PDF 的能力取决于你的运行环境。

### 方法一：让 Codex 安装

在 Codex 中发送：

```text
使用 $skill-installer，从 https://github.com/wjjmario/mcm-python-skill
安装仓库里的 mcm-python skill（路径：mcm-python）。
```

### 方法二：手动安装到个人目录

先克隆仓库：

```bash
git clone https://github.com/wjjmario/mcm-python-skill.git
cd mcm-python-skill
```

当前官方文档推荐个人技能目录 `~/.agents/skills`。下面的命令只新增目录；目标已存在时停止，避免覆盖你的修改。

**Windows PowerShell：**

```powershell
$skillRoot = Join-Path $env:USERPROFILE '.agents\skills'
$skillTarget = Join-Path $skillRoot 'mcm-python'
if (Test-Path -LiteralPath $skillTarget) { throw 'mcm-python 已存在，请先检查已有版本。' }
New-Item -ItemType Directory -Path $skillRoot -Force | Out-Null
Copy-Item -LiteralPath '.\mcm-python' -Destination $skillTarget -Recurse
```

**macOS / Linux：**

```bash
mkdir -p "$HOME/.agents/skills"
if [ -e "$HOME/.agents/skills/mcm-python" ]; then
  echo 'mcm-python already exists; inspect it before updating.'
else
  cp -R ./mcm-python "$HOME/.agents/skills/mcm-python"
fi
```

也可安装到项目的 `.agents/skills/mcm-python`，使其仅用于该项目。部分已有环境和内置安装器使用 `~/.codex/skills` 或 `$CODEX_HOME/skills`；按你的客户端与安装器实际目录使用，避免在多个目录重复安装同名 skill。

安装后在技能列表中确认 `mcm-python`。如果没有出现，重新打开聊天或重启 Codex。安装目录与调用方式见 [OpenAI 官方 Skills 文档](https://learn.chatgpt.com/docs/build-skills)。

## 怎么用

在支持 `$skill-name` 的 Codex 输入框中直接提及 `$mcm-python`；有技能选择器的客户端，也可选择“美赛建模 · Python”。随后给出题目与数据，或者要求寻找官方历史题。

### 从一道历史题开始

```text
使用 $mcm-python，找一道官方美赛历史题做训练。
请先解释题目、拆解要求，再用 Python 建模、运行和验证，
最后整理英文论文与中文复盘。没有实测数据时明确列出假设。
```

### 处理自己的题目

```text
使用 $mcm-python，处理附件中的美赛题目和数据。
这是历史题训练，团队使用 Python。
先列出每个问题需要的数据、输出和候选模型，然后完成基线并实际运行。
保留数据来源、运行记录、结果和 AI 使用记录。
```

正式参赛时说明年份、题号、当前阶段和剩余时间，要求核验当届规则。历史训练与正式比赛的规则不能混用。

### 只做某一个环节

```text
使用 $mcm-python，检查当前模型的假设、变量单位和代码是否一致，
做关键参数敏感性分析，解释结果是否支持论文结论。
```

```text
使用 $mcm-python，根据已有结果整理英文摘要和模型章节。
数字必须来自结果文件，公式要正常排版，引用必须经过核验。
```

### 继续已有项目

```text
使用 $mcm-python，继续当前建模项目。
先读取 notes/status.md、题目要求和最近结果，再推进尚未完成的工作。
```

## 初始化一个 Python 项目

不需要先安装 skill，也可以从仓库根目录创建项目：

```bash
python mcm-python/scripts/init_project.py ./my-mcm-project
cd my-mcm-project
python -m venv .venv
```

脚本拒绝覆盖已有目标目录。

**Windows：**

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe src/main.py --config config.json
```

**macOS / Linux：**

```bash
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python src/main.py --config config.json
```

生成的 `src/main.py` 是合成数据回归演示，用于检查项目运行、基线比较和图表导出。**它不是美赛解题模型，演示数字不能放进赛题论文。** 实际建模时让 Codex 按题目替换代码，并更新所需依赖。

项目包含：

```text
my-mcm-project/
├── config.json          参数和随机种子
├── requirements.txt     当前模型依赖
├── data/raw/            原始数据
├── data/processed/      派生数据
├── src/                 建模与求解代码
├── results/             机器可读结果
├── figures/             图表
├── paper/               论文与结果登记表
└── notes/               要求映射、状态、来源、AI 使用记录
```

## 仓库结构

```text
mcm-python-skill/
├── README.md
└── mcm-python/
    ├── SKILL.md                     skill 入口与工作闭环
    ├── agents/openai.yaml           技能名称与默认调用提示
    ├── scripts/init_project.py      项目初始化工具
    ├── assets/project/             Python 项目模板
    └── references/
        ├── modeling.md             模型选择与验证
        ├── python.md               Python 工程约定
        ├── paper.md                英文论文与数学排版
        └── contest-rules.md        官方规则来源与 AI 披露
```

## 实题试跑情况

创建时用 **2023 MCM A：Drought-Stricken Plant Communities** 做过一次全流程历史题试跑，完成了群落动力学模型、七种情景、数值检验和八页英文训练报告。

这次试跑的生态参数是明确标记的假设参数，没有实测数据校准。一个重要发现是：混合群落优于随机单物种，但最佳耐旱单物种可能更好。因此需要检查基线、保留反例，不能把“物种数量增加”自动解释为因果收益。

本仓库发布通用 skill 与模板。上述独立试跑报告及 COMAP 题目 PDF 不随包分发。官方历史题可从 [COMAP 2023 题目归档](https://www.contest.comap.com/undergraduate/contests/mcm/contests/2023/problems/) 获取。

模板验证包括：拒绝覆盖、种子复现、指标独立复算、无噪声解析关系恢复、非法输入拒绝和图表导出。一次机理题试跑不代表已验证所有题型。

## 使用边界

- 规则参考包含带日期的核验快照；正式比赛每次重查当届官方要求。
- 保存并披露实际 AI 使用，核验生成内容和引用，不能伪造数据、结果或对话记录。
- 未运行的代码标记为未验证；实际生成 PDF 后检查公式、表图和分页。
- 无实测数据时只能报告假设模型和情景结论，不能声称经验预测准确性。
- 团队自行判断方案与完成最终提交；skill 不保证奖项。

官方规则：[COMAP MCM/ICM Instructions](https://contest.comap.com/undergraduate/contests/mcm/instructions.html)。
