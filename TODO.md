# TODO List

**from_protein score 太大会报错**

- 复现
  1. 执行命令 `python herbiv-cli.py --function protein --proteins ENSP00000381588 --score 990`
  2. compute line 214 ValueError: max() arg is an empty sequence

**SettingWithCopyWarning**

- 复现
  1. 执行命令 `python herbiv-cli.py --function tcm_protein --tcms HVM0367 HVM1695 --proteins ENSP00000043402 --path result`
  2. 警告 SettingWithCopyWarning

**pydoc 格式不统一**

**Future Warning**
已解决
原因：在 get_chem_protein_links 时，需要将 Combined_score 映射为小数，与原始 int 类型不兼容
解决：提前将 Combined_score 的类型修改为 float
