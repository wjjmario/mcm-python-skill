# Python 工程

优先 NumPy、pandas、SciPy、Matplotlib，按任务引入 scikit-learn、NetworkX 或优化求解器。使用项目虚拟环境，只安装实际所需依赖，不修改其他环境。

目录：`data/raw` 原始数据，`data/processed` 派生数据，`src` 代码，`results` 数值，`figures` 图，`paper` 论文，`notes` 状态/来源/AI记录。路径基于项目根目录或入口参数，不硬编码机器路径。

```text
python -m venv .venv
<venv-python> -m pip install -r requirements.txt
<venv-python> src/main.py --config config.json
<venv-python> -m pip freeze > environment-lock.txt
```

使用系统对应的 venv Python，不默认修改 PowerShell 执行策略。模板依赖仅支持演示，不代表全部竞赛方法或锁定环境；按实际建模更新依赖并保存 Python/包版本、系统、命令。

每个模型有可复跑入口，参数集中管理，保存 CSV/JSON 结果、种子、数据哈希、配置及求解状态。禁止 eval 配置、静默吞异常或将失败写成成功。检查输入列、单位、有限值、重复记录、形状和边界。测试针对守恒、可行性、解析特例等真实性质。

演示程序用合成数据；输出不能进入赛题论文。没有运行条件时明确限制，不把语法通过称为求解成功。

图表使用英文轴标签、单位、图例及色盲友好配色，导出矢量图或高分辨率 PNG，每张图关联结果文件。不要连接无序类别制造趋势，注明合成数据和不确定性。最终 PDF 中检查字号、裁切和可读性。
