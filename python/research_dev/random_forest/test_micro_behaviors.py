import unittest
from unittest import TestCase
from python.research_dev.random_forest.exploit_uri_behaviors import microBehaviors as mb


class TestMicroBehaviors(TestCase):
    # Define a global test list
    uriList = ['/97.exe?1', '/raw',
               '/wp-content/plugins/theme-check/misc.php?34F0103544E2B25192E6AF0913ABE73BC21B0A31B82DC4E8D065CF5E9E55FEA92DB93FE6AEEB312449485E01DC99E4D47932EB53448B09D340AA22EDE68F63A3938F85E00D8EC314F81B2FA6DA02F5F9807B15E9DEFBA2FEA622BBEE35988934E428A133418E0F6B4B11E2918502CB158ABFEAC8D7C77C6542D07AB697F9CDA2EF564892C0B4B680EDB5BB1E6BDB74300CF63F55F4CC39E3E83EE9D8B70685F6D965ED309AF07DDF143D5082AAF0B0D27F422C89DD4F3BFF4CD93A9EBE0A83B5669779E6C050DA4291F89F85727F7EFBFDD96C9149B12C2397F1BA29A7C5CAB5036EB5B02B6ED79379D563C464717B1BE051BA3244EC5F8CE5D5E101F1555486A911A36F546A928CA17CF60FA2FEDEC2F71B2DB6752FC4567112FF797441ECFB6F093FEB8FDF192788AE0FFC9D5662CB88D9F7F8C50576359807C8F8FE4E8AA9965D546DF52000AADC544A03DFFCE596A387D5120254BA0E135ECDB9CB1F1127',
               '/wp-content/plugins/theme-check/misc.php?572A56481F78D91A71F483FAC3626A6F89E2D4AFC98B8E4D38D901CB11D6B924D13EDDCA9E1C27D91D71987B1051AD6B2F9BEA566F4F3045C43796BFEC4C8AF763F838783B32EE6F30599814D4C07EDA1CB04100BE5491A459ED2919E1E7F57FFBF78B983B91D398700387E8A31738D900E2E32075CF665A12BD8AD4718F7B32F695E398862E28B15DE8A44AA7A63AF0648C44373229C87CD8566B3E64F4677A1B79C1DB1C9D9AB52836A8230F62BBCB144F4B8CA8A44BAAC4D35497A512995BC1865425D0F0C5E4380181F73DE7690B7680D4FA05D2A419B66DA62943BDF7276B100B5DC2B1F39D53847F3768053ED3C273A328CEF9BEBBC84D28FDEAB69E114D3DF889E54074029D8232027596623990647E1D01D1D402657382B1F51D05F5B272ED3C7615A7D0CD647F85F1FA10E55F7F1749565525526D227D5941A9867E59E45879712590AACA4336088056A91FF3A3129B1384811DE40F749EB09896F91704F83CB5A347EBE4D3B5D2D45851DF',
               '/index.php']

    # def test_isBase64(self):
    #     self.fail()
    #
    # def test_isUrlEncoded(self):
    #     self.fail()

    def test_max_path_length(self):
        self.assertTrue(mb.max_path_length(self.uriList), 4)

    def test_min_path_length(self):
        self.assertTrue(mb.min_path_length(self.uriList), 1)

    def test_max_length(self):
        self.assertTrue(mb.max_length(self.uriList), 777)

    def test_min_length(self):
        self.assertTrue(mb.min_length(self.uriList), 4)

    def test_max_entropy(self):
        self.assertTrue(mb.max_entropy(self.uriList), 0.536905227321473)

    def test_min_entropy(self):
        self.assertTrue(mb.min_entropy(self.uriList), 0.25)

    def test_base_64_match(self):
        self.assertTrue(mb.base_64_match(self.uriList), 1)
        self.assertTrue(mb.base_64_match(['dGVzdA0K', 'dGVzdDE=', 'dGVzdDI=', 'dGVzdDM=','#&sj.s3']), 4)
        self.assertFalse(mb.isUrlEncoded(""))

    def test_percent_encoding_match(self):
        self.assertIs(mb.percent_encoding_match(self.uriList), 0)
        self.assertTrue(mb.percent_encoding_match(['%34%jd%kl%','12345','%ji.,%,./n3']), 1)

    def test_uri_distinct(self):
        self.assertTrue(mb.uri_distinct(['a','b','a','b']), 2)
        self.assertTrue(mb.uri_distinct(self.uriList), 5)

if __name__ == '__main__':
    unittest.main()