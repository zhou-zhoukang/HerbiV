import unittest

import numpy as np

from herbiv import *


class TestHerbiv(unittest.TestCase):
    def test_get_formula(self):
        formula1 = get_formula('HVPID', ['HVP1625'])
        self.assertEqual(formula1.shape, (1, 6))
        self.assertEqual(formula1['HVPID'][0], "HVP1625")

        formula2 = get_formula('HVPID', ['HVP1625', 'HVP3000'])
        self.assertEqual(formula2.shape, (2, 6))
        self.assertEqual(formula2['HVPID'][0], 'HVP1625')
        self.assertEqual(formula2['HVPID'][1], 'HVP3000')

        formula3 = get_formula('HVPID', ['strange'])
        self.assertEqual(formula3.shape, (0, 6))

        formula_tcm_links1 = get_formula_tcm_links('HVPID', ['HVP1625'])
        self.assertEqual(formula_tcm_links1.shape, (6, 2))
        self.assertEqual(formula_tcm_links1['HVPID'][0], 'HVP1625')
        self.assertEqual(formula_tcm_links1['HVMID'][0], 'HVM0367')

        formula_tcm_links2 = get_formula_tcm_links('HVPID', formula1["HVPID"])
        self.assertTrue(formula_tcm_links1.equals(formula_tcm_links2))

        tcm1 = get_tcm('cn_name', ['柴胡', '黄芩'])
        self.assertEqual(tcm1.shape, (2, 19))
        self.assertEqual(tcm1['cn_name'][0], '柴胡')

        tcm_chem_links1 = get_tcm_chem_links('HVMID', ['HVM0367'])
        self.assertEqual(tcm_chem_links1.shape, (316, 2))

        chai_hu = get_tcm_chem_links('HVMID', ['HVM0367'])
        tcm2 = get_chemicals('HVCID', chai_hu['HVCID'])
        self.assertEqual(tcm2.shape, (258, 8))
        self.assertEqual(tcm2['STITCH_id'][1], "CIDm00000206")

        chem_protein_links1 = get_chem_protein_links('Ensembl_ID', ['ENSP00000335062'], 200)
        print(chem_protein_links1)
        self.assertEqual(chem_protein_links1.shape, (2, 3))

        return

    def test_version(self):
        print(np.version.version)
