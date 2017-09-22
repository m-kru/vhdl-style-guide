
import unittest
import sys
sys.path.append('modules')

from modules.rules import rule_whitespace
from modules import vhdlFile
from modules import line


class testRuleWhitespaceMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = rule_whitespace.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '001')

        oFile = vhdlFile.vhdlFile('tests/rule_whitespace/whitespace_test_input.txt')

        dExpected = [2,4]
        oFile.lines.append(line.line('  This is a test of ending whitespace'))
        oFile.lines.append(line.line('  This is a test of ending whitespace '))
        oFile.lines.append(line.line('  This is a test of ending whitespace'))
        oFile.lines.append(line.line('  This is a test of ending whitespace  '))
        oFile.lines.append(line.line('  This is a test of ending whitespace'))
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = rule_whitespace.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '002')

        oFile = vhdlFile.vhdlFile('tests/rule_whitespace/whitespace_test_input.txt')

        dExpected = [1,2,5]
        oFile.lines.append(line.line('  This is a test of tabs\t'))
        oFile.lines.append(line.line('\tThis is a test of tabs'))
        oFile.lines.append(line.line('  This is a test of tabs'))
        oFile.lines.append(line.line('  This is a test of tabs'))
        oFile.lines.append(line.line('  This is a \t test of tabs'))
        oFile.lines.append(line.line('  This is a test of tabs'))
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003(self):
        oRule = rule_whitespace.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '003')

        oFile = vhdlFile.vhdlFile('tests/rule_whitespace/whitespace_test_input.txt')

        dExpected = [2,4,6]
        oFile.lines.append(line.line('  This is a test of tabs;'))
        oFile.lines.append(line.line('  This is a test of tabs ;'))
        oFile.lines.append(line.line('  This is a test of tabs;'))
        oFile.lines.append(line.line('  This is a test of tabs    ;'))
        oFile.lines.append(line.line('  This is a test; of tabs'))
        oFile.lines.append(line.line('  This is a test ; of tabs'))
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004(self):
        oRule = rule_whitespace.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '004')

        oFile = vhdlFile.vhdlFile('tests/rule_whitespace/whitespace_test_input.txt')

        dExpected = [2,4,6]
        oFile.lines.append(line.line('  This is a test of tabs,'))
        oFile.lines.append(line.line('  This is a test of tabs ,'))
        oFile.lines.append(line.line('  This is a test of tabs,'))
        oFile.lines.append(line.line('  This is a test of tabs    ,'))
        oFile.lines.append(line.line('  This is a test, of tabs'))
        oFile.lines.append(line.line('  This is a test , of tabs'))
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005(self):
        oRule = rule_whitespace.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '005')

        oFile = vhdlFile.vhdlFile('tests/rule_whitespace/whitespace_test_input.txt')

        dExpected = [1,3]
        oFile.lines.append(line.line('  This is a test of parenthesis ( failure'))
        oFile.lines.append(line.line('  This is a test of parenthesis (pass'))
        oFile.lines.append(line.line('  This is a test of parentehsis (  failure'))
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006(self):
        oRule = rule_whitespace.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '006')

        oFile = vhdlFile.vhdlFile('tests/rule_whitespace/whitespace_test_input.txt')

        dExpected = [1,3]
        oFile.lines.append(line.line('  This is a test of parenthesis (failure )'))
        oFile.lines.append(line.line('  This is a test of parenthesis (pass)'))
        oFile.lines.append(line.line('  This is a test of parentehsis (failure   )'))
        oFile.lines.append(line.line('   ) pass'))
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007(self):
        oRule = rule_whitespace.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '007')

        oFile = vhdlFile.vhdlFile('tests/rule_whitespace/whitespace_test_input.txt')

        dExpected = [1,3]
        oFile.lines.append(line.line('  This is a test,of commas (failure )'))
        oFile.lines.append(line.line('  This is a test, of commas (pass)'))
        oFile.lines.append(line.line('  This is a test of commas,(failure   )'))
        oFile.lines.append(line.line('   ) pass'))
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)



if __name__ == '__main__':
    unittest.main()
