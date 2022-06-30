import unittest
import CTD_functions as CTD


class TestFeaturesInputMethods(unittest.TestCase):

    def test_readListFile(self):
        # Input
        inputFile = "/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/unittest/Input_genesList.tsv"
        expectedOutputFile = "/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/unittest/OutputExpected_TestFeaturesInputMethods.tsv"
        # Parameters
        expectedOutput = []
        # Run function
        with open(inputFile, 'r') as inputFileHandler:
            outputList = CTD.readListFile(listFile=inputFileHandler)
        with open(expectedOutputFile, 'r') as expectedOutputHandler:
            for line in expectedOutputHandler:
                expectedOutput.append(line.rstrip())
        # Compare
        self.assertEqual(outputList, expectedOutput)

    def test_readCTDFile(self):
        # Input
        inputFile = "/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/unittest/Input_CTDFile.tsv"
        expectedOutputFile = "/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/unittest/OutputExpected_TestFeaturesInputMethods.tsv"
        # Parameters
        expectedOutputList = []
        expectedOutputDict = {}
        # Run function
        with open(inputFile, 'r') as inputFileHandler:
            outputDict = CTD.readCTDFile(CTDFile=inputFileHandler, nbPub=2)
        for i in outputDict:
            outputDict[i] = outputDict[i].sort()
        with open(expectedOutputFile, 'r') as expectedOutputHandler:
            for line in expectedOutputHandler:
                expectedOutputList.append(line.rstrip())
        expectedOutputDict['D014801'] = expectedOutputList.sort()
        # Compare
        self.assertEqual(outputDict, expectedOutputDict)

    def test_targetExtraction(self):
        # Input
        inputFile = "/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/unittest/Input_factorsList.tsv"
        outputFile = '/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/unittest/'
        expectedOutputFile = '/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/unittest/CTD_request_D014801.tsv'
        # Run function
        with open(inputFile, 'r') as inputFileHandler:
            outputDict = CTD.targetExtraction(CTDFile=inputFileHandler, directAssociations=False, outputPath=outputFile, nbPub=2)
        with open(expectedOutputFile, 'r') as expectedFileHandler:
            expectedOutputDict = CTD.readCTDFile(CTDFile=expectedFileHandler, nbPub=2)
        # Compare
        self.assertEqual(outputDict, expectedOutputDict)


if __name__ == '__main__':
    unittest.main()


