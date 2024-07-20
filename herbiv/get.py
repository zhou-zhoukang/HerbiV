import pandas as pd
import os

data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')


def get_something(table_name: str, by: str, items: list[str], drop_dup: list[str] = None) -> pd.DataFrame:
    try:
        # 读取 HerbiV_formula 数据集
        something_all = pd.read_csv(os.path.join(data_path, table_name))
    except FileNotFoundError:
        something_all = pd.DataFrame()

    # 在数据集中获取 items 中复方的信息
    try:
        if drop_dup is not None:
            something = something_all[something_all[by].isin(items)].drop_duplicates(subset=drop_dup)
        else:
            something = something_all[something_all[by].isin(items)]
        # 重新设置索引
        something.index = range(something.shape[0])
    except KeyError:
        something = pd.DataFrame()
    return something


def get_formula(by: str, items: list[str]) -> pd.DataFrame:
    """
    读取 HerbiV_formula.csv，返回 items 中复方的信息。
    Read the HerbiV_formula dataset and return the formula(s) information in items.

    Args:
        by (str): 数据集中与 items 相匹配的列的列名。Column name of the column in the dataset that matches items.
        items (collections.abc.Iterable): 要查询的复方。Formula(s) to be queried.

    Returns:
        formula: items中复方的信息。Formula(s) information in items.
        数据文件不存在，读取失败，找不到对应 item，返回空的 DataFrame

    Examples:
        >>> get_formula('HVPID', ['HVP1625'])  # 获取 HVPID 为 HVP1625 的复方（小柴胡汤）的信息
             HVPID  ... Source Document
        0  HVP1625  ...   shang han lun
        [1 rows x 6 columns]
    """
    return get_something('HerbiV_formula.csv', by, items)


def get_formula_tcm_links(by: str, items: list[str]) -> pd.DataFrame:
    """
    读取HerbiV_formula_tcm_links数据集，返回items中复方/中药的复方-中药连接信息。
    Read the HerbiV_formula_tcm_links dataset
    and return the formula(s)-TCM connection information of formula(s)/TCM in items.
    Args:
        by (str):数据集中与items相匹配的列的列名。Column name of the column in the dataset that matches items.
        items (collections.abc.Iterable): 要查询的复方/中药。Formula(s)/TCM to be queried.
    Returns:
        formula_tcm_links(pandas.DataFrame): items中复方/中药的复方-中药连接信息。
        Formula(s)-TCM connection information of formula(s)/TCM in items.
    Examples:
        >>> get_formula_tcm_links('HVPID', ['HVP1625'])# 获取HVPID为HVP1625的复方（小柴胡汤）的复方-中药连接信息
             HVPID    HVMID
        0  HVP1625  HVM0367
        1  HVP1625  HVM0735
        2  HVP1625  HVM0766
        3  HVP1625  HVM1695
        4  HVP1625  HVM3203
        5  HVP1625  HVM4463
    """
    return get_something('HerbiV_formula_tcm_links.csv', by, items)


def get_tcm(by: str, items: list[str]) -> pd.DataFrame:
    """
    读取HerbiV_tcm数据集，返回items中中药的信息。
    Read the HerbiV_tcm dataset and return the TCM information in items.

    Args:
        by (str): 数据集中与items相匹配的列的列名。Column name of the column in the dataset that matches items.
        items (collections.abc.Iterable): 要查询的中药。TCM to be queried.

    Returns:
        pandas.DataFrame: items中中药的信息。TCM information in items.

    Examples:
        >>> get_tcm('cn_name', ['柴胡', '黄芩'])  # 获取cn_name（中文名）为柴胡和黄芩的中药的信息（不建议使用中文名检索）
             HVMID cn_name pinyin_name  ... TCM_ID_id SymMap_id TCMSP_id
        0  HVM0367      柴胡     CHAI HU  ...    3396.0      58.0     80.0
        1  HVM1695      黄芩   HUANG QIN  ...    6700.0     188.0    371.0
        [2 rows x 19 columns]
    """
    return get_something('HerbiV_tcm.csv', by, items)


def get_tcm_chem_links(by: str, items: list[str]) -> pd.DataFrame:
    """
        读取HerbiV_tcm_chemical_links数据集，返回items中中药/化合物的中药-成分（化合物）连接信息。
        Read the HerbiV_tcm_chemical_links dataset and
        return the TCM-ingredient(s)(chemical(s)) information of TCM/chemical(s) in items.

        Args:
            by (str): 数据集中与items相匹配的列的列名。Column name of the column in the dataset that matches items.
            items (collections.abc.Iterable): 要查询的中药/化合物。TCM/chemical(s) to be queried.

        Returns:
            pandas.DataFrame: items中中药/化合物的中药-成分连接信息。TCM-ingredient(s) information of TCM/chemical(s) in items.

        Examples:
            >>> get_tcm_chem_links('HVMID', ['HVM0367'])  # 获取HVMID为HVM0367的中药（柴胡）的中药-成分连接信息
                   HVMID    HVCID
            0    HVM0367  HVC0284
            1    HVM0367  HVC3018
            2    HVM0367  HVC0396
            3    HVM0367  HVC1371
            4    HVM0367  HVC1045
            ..       ...      ...
            311  HVM0367  HVC2149
            312  HVM0367  HVC0465
            313  HVM0367  HVC0941
            314  HVM0367  HVC0936
            315  HVM0367  HVC1279
            [316 rows x 2 columns]
    """
    return get_something('HerbiV_tcm_chemical_links.csv', by, items)


def get_chemicals(by: str, items: list[str]) -> pd.DataFrame:
    """
        读取HerbiV_chemicals数据集，返回items中化合物的信息。
        Read the HerbiV_chemicals dataset and return the chemical(s) information in items.

        Args:
            by (str): 数据集中与items相匹配的列的列名。Column name of the column in the dataset that matches items.
            items (collections.abc.Iterable): 要查询的化合物。Chemical(s) to be queried.

        Returns:
            pandas.DataFrame: items中化合物的信息。Chemical(s) information in items.

        Examples:
            >>> chai_hu = get_tcm_chem_links('HVMID', ['HVM0367'])# 获取HVMID为HVM0367的中药（柴胡）的中药-成分连接信息
            >>> get_chemicals('HVCID', chai_hu['HVCID'])# 获取柴胡的成分的信息
                   HVCID                                     Name  ...     STITCH_id     HERB_id
            0    HVC0034                                allantoin  ...  CIDm00000204  HBIN015193
            1    HVC0036                                  glucose  ...  CIDm00000206  HBIN001003
            2    HVC0046                             benzaldehyde  ...  CIDm00000240  HBIN017734
            3    HVC0071                                 coumarin  ...  CIDm00000323  HBIN021605
            4    HVC0073                            cuminaldehyde  ...  CIDm00000326  HBIN010591
            ..       ...                                      ...  ...           ...         ...
            253  HVC6045                        8-hydroxydaidzein  ...  CIDm05466139  HBIN012955
            254  HVC6054                                narcissin  ...  CIDm05481663  HBIN031161
            255  HVC6156  stigmasterol-3-O-beta-D-glucopyranoside  ...  CIDm06440962  HBIN015690
            256  HVC6183                           beta-gurjunene  ...  CIDm06450812  HBIN018138
            257  HVC6204                         geraniol acetate  ...  CIDm06850714  HBIN027529
            [258 rows x 8 columns]
    """
    return get_something('HerbiV_chemicals.csv', by, items, ['HVCID'])


def get_chem_protein_links(by: str, items: list[str], score=900) -> pd.DataFrame:
    """
    读取 HerbiV_chemical_protein_links 数据集，
    返回 items 中化合物/蛋白的化合物-靶点（蛋白）连接的 combined_score(s) 大于等于 score 的连接信息。
    Read the HerbiV_chemical_protein_links dataset and
    return chemical(s)-target(s)(protein(s)) connection information
    for which the combined_score of the chemical(s)/protein(s) in items is no less than the score.

    Args:
        by (str): 数据集中与items相匹配的列的列名。Column name of the column in the dataset that matches items.
        items (collections.abc.Iterable): 要查询的化合物/蛋白。Chemical(s)/protein(s) to be queried.
        score (int): 仅 combined_score 大于等于 score 的记录会被筛选出，默认为 900，最大为 1000，最小为 0。
        score (s) with combined_score no less than score will be filtered out, 900 by default.

    Returns:
        pandas.DataFrame: items 中化合物/蛋白的化合物-靶点（蛋白）连接的 combined_score 大于等于 score 的连接信息。
        Chemical(s)-target(s)(protein(s)) connection information for which
        the combined_score of the chemical(s)/protein(s) is no less than the score in items.

    Examples:
        >>> # 获取 Ensembl ID 为 ENSP00000335062 的蛋白（PDCD1）的化合物-靶点连接信息
        >>> get_chem_protein_links('Ensembl_ID', ['ENSP00000335062'], 200)
             HVCID       Ensembl_ID  Combined_score
        0  HVC5134  ENSP00000335062           0.202
        1  HVC0159  ENSP00000335062           0.795
    """
    # 读取HerbiV_chemical_protein_links数据集
    chem_protein_links_all = pd.read_csv(os.path.join(data_path, "HerbiV_chemical_protein_links.csv"))
    # 在数据集中获取items中化合物/蛋白的化合物-靶点（蛋白）连接的combined_score大于等于score的连接信息
    chem_protein_links = chem_protein_links_all[
        (chem_protein_links_all[by].isin(items)) & (chem_protein_links_all['Combined_score'] >= score)
    ]
    # 将Combined_score变换为0-1的浮点数
    copy = chem_protein_links.copy()
    copy['Combined_score'] = copy['Combined_score'].astype(float)
    copy['Combined_score'] = copy['Combined_score'].apply(lambda x: x / 1000)
    chem_protein_links = copy.copy()
    # 重新设置索引
    chem_protein_links.index = range(chem_protein_links.shape[0])
    return chem_protein_links


def get_proteins(by: str, items: list[str]) -> pd.DataFrame:
    """
        读取HerbiV_proteins数据集，返回items中蛋白的信息。
        Read the HerbiV_proteins dataset and return the protein(s) information in items.

        Args:
            by (str): 数据集中与items相匹配的列的列名。Column name of the column in the dataset that matches items.
            items (collections.abc.Iterable): 要查询的蛋白。Protein(s) to be queried.

        Returns:
            pandas.DataFrame: items中蛋白的信息。Protein information in items.

        Examples:
            >>> get_proteins('gene_name', ['PDCD1 PD1'])  # 获取gene_name（基因名）为PDCD1 PD1的蛋白的信息（不建议使用名称检索）
                    Ensembl_ID  ...  gene_name
            0  ENSP00000335062  ...  PDCD1 PD1
    """
    return get_something('HerbiV_proteins.csv', by, items, ['Ensembl_ID'])
