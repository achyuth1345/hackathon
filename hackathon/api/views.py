import copy

import xlrd as xlrd
import pandas as pd
from os.path import dirname as up
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
import pandas as pd
import numpy as np
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from setuptools import glob

from .serializers import ApiSerializer
from .models import CartItem
from django.conf import settings
import os
def index(request):
    return HttpResponse("Hello world!")
StepsJsonData = {
        "title": "New Step",
        "description": '<p style=\\"text-align: left;\\">Description</p>',
        "questions": [],
        "associatedAnimationIndex": 0,#-----------------change this from excell-----------------
        "cameraMatrix": [],
        "cameraPosition": {},
        "cameraTarget": {}
    }
AnimationJsonData = {
        "title": "New Animation 1",
        "frameCount": 0,
        "timeSequence": [
            0,
            1
        ],
        "nodes": {},
        "startType": "initial",
        "parentStepIndex": 0   #--------------------have to cange after anjali says---------------

    }
LabelsJsonData = {
        "connectedModelComponentTitle": "sample",
        "connectionModelCompId": -1943580584,
        "startPositionVector": {
            "x": 0,
            "y": 0,
            "z": 0
        },
        "endPositionVector": {
            "x": 0,
            "y": 0,
            "z": 0
        },
        "label": "Label 1",
        "startPositionVectorLocal": {
            "x": 0,
            "y": 0,
            "z": 0
        },
        "endPositionVectorLocal": {
            "x": 0,
            "y": 0,
            "z": 0
        }
    }
cardsData=   {
                        "id": 0,  #---------------change----------------------------
                        "description": "<p style=\"text-align: left;\">Description</p>",#---------------change this------------------
                        "title": "New Step 1", #-------------change---------------------------------------
                        "animationIndex": 0, #------------change------------------------------------
                        "cameraPosition":{},
                        "cameraMatrix": [],
                        "cameraTarget": {},
                        "hiddenParts": []
                    }

FinalJson = {
        "model": {
            "workInstructionId": "be92219f-d378-481a-84f2-bfa5fabaaf1a",
            "organizationId": "c0dfc9c6-9771-4573-9da9-dca8c5ecb48e",
            "fileInfo": {
                "schemaVersion": 1,
                "studioVersion": 1,
                "projectName": "Untitled",
                "createdOn": "11/28/2022, 12:26:18 PM",
                "modifiedOn": "11/28/2022, 12:26:18 PM",
                "author": "cds",
                "cad": {
                    "models": [
                        {
                            "id": 1,
                            "name": "A48497_ASM_QA_ZGGGGGHHH",
                            "url": "https://api2.cdsvisual.net/v1/files/e93fd265-83aa-456c-9fbd-09207c75d960",
                            "gltfId": "3f92630b-3621-49dc-8550-e6c099322a4a",
                            "gltfName": "A48497_ASM_QA_ZGGGGGHHH.gltf",
                            "gltf_path": "https://api2.cdsvisual.net/v1/files/3f92630b-3621-49dc-8550-e6c099322a4a",
                            "visibility": True,
                            "matrix": [
                                1,
                                0,
                                0,
                                0,
                                0,
                                1,
                                0,
                                0,
                                0,
                                0,
                                1,
                                0,
                                0,
                                0,
                                0,
                                1
                            ],
                            "suppressedParts": [],
                            "onLoadReplaceableParts": {}
                        }
                    ]
                },
                "scene": {
                    "envMap": {},
                    "background": {
                        "type": "",
                        "data": ""
                    },
                    "defaultCamera": [
                        1,
                        0,
                        0,
                        0,
                        0,
                        1,
                        0,
                        0,
                        0,
                        0,
                        1,
                        0,
                        0,
                        0,
                        0,
                        1
                    ]
                },
                "extras": {
                    "enableAxisTriad": False,
                    "enableShadow": False,
                    "enableContinuousRotateOnLoad": False,
                    "enableCameraUpDown": False,
                    "hotspotOverlayDisplayType": "Document"
                }
            }
        },
        "procedure": {
            "procedureId": "dda344bc-285d-4830-97c0-abfb554ec001",
            "explosions": {},
            "materials": {},
            "lights": {}
        },
        "task": {
            "animations": [],
            "explosions": {},
            "annotations": {
                "annotationData": []
            },
            "hotspots": {},
            "tools": {
                "toolData": [],
                "uploadedToolData": []
            },
            "views": {},
            "materials": {},
            "audio": {},
            "cuttingPlanes": {},
            "mediaReferences": [],
            "workInstructions": {
                "cameraFront": {
                    "x": 42.54672152755957,
                    "y": 48.36742889952191,
                    "z": -32.644889614856446
                },
                "cardsData": [
                    {
                        "id": 0,
                        "description": "<p style=\"text-align: left;\">Description</p>",
                        "title": "New Step 1",
                        "animationIndex": 0,
                        "cameraPosition": {
                            "x": 1121.710472212005,
                            "y": 96.29844139072685,
                            "z": -53.74795021075377
                        },
                        "cameraMatrix": [
                            -0.01848756578625288,
                            0,
                            -0.9998290903505953,
                            0,
                            -0.0419455988095509,
                            0.9991195950325719,
                            0.0007756045757414502,
                            0,
                            0.9989488358528715,
                            0.04195276894258243,
                            -0.01847128924149888,
                            0,
                            1121.710472212005,
                            96.29844139072685,
                            -53.74795021075377,
                            1
                        ],
                        "cameraTarget": {
                            "x": -19.637574932096314,
                            "y": 48.36539437039825,
                            "z": -32.64351643861787
                        },
                        "hiddenParts": []
                    },
                    {
                        "id": 1,
                        "description": "<p style=\"text-align: left;\">Description</p>",
                        "title": "New Step 2",
                        "animationIndex": 1,
                        "cameraPosition": {
                            "x": 1100.8188927498902,
                            "y": 240.1010131131415,
                            "z": 81.06367494907425
                        },
                        "cameraMatrix": [
                            0.10096904333552625,
                            1.3877787807814457e-17,
                            -0.9948895678857572,
                            0,
                            -0.16696805228671957,
                            0.9858166815646714,
                            -0.01694520181050091,
                            0,
                            0.980778732336447,
                            0.16782571420619466,
                            0.09953696724178795,
                            0,
                            1100.8188927498902,
                            240.1010131131415,
                            81.06367494907425,
                            1
                        ],
                        "cameraTarget": {
                            "x": -19.640987880085657,
                            "y": 48.37380022652036,
                            "z": -32.64918984887431
                        },
                        "hiddenParts": []
                    },
                    {
                        "id": 2,
                        "description": "<p style=\"text-align: left;\">Description 33</p>",
                        "title": "New Step 3",
                        "animationIndex": 1,
                        "cameraPosition": {
                            "x": 1100.8188927498902,
                            "y": 240.1010131131415,
                            "z": 81.06367494907425
                        },
                        "cameraMatrix": [
                            0.10096904333552625,
                            1.3877787807814457e-17,
                            -0.9948895678857572,
                            0,
                            -0.16696805228671957,
                            0.9858166815646714,
                            -0.01694520181050091,
                            0,
                            0.980778732336447,
                            0.16782571420619466,
                            0.09953696724178795,
                            0,
                            1100.8188927498902,
                            240.1010131131415,
                            81.06367494907425,
                            1
                        ],
                        "cameraTarget": {
                            "x": -19.640987880085657,
                            "y": 48.37380022652036,
                            "z": -32.64918984887431
                        },
                        "hiddenParts": []
                    }
                ],
                "instructions": [],
                "blinkColor": []
            }
        }
    }



class ApiViews(APIView):

    def replaceCArdsSteps(self,dataframe,data1):
        list_data = []
        for i in range(dataframe.index.start, dataframe.index.stop):
            data=copy.deepcopy(data1)
            data['title'] = dataframe.get('Title')[i]
            str = '<p style=\\"text-align: left;\\">'
            str += dataframe['Description'][i] + '</p>'
            data['description'] = str
            data['animationIndex'] = dataframe.get('Animation Index')[i]
            data['id'] = dataframe.get('Step Id')[i]
            list_data.append(data)
        return list_data
    def replaceTitleInSteps(self,dataframe, data1):
        list_data = []
        for i in range(dataframe.index.start, dataframe.index.stop):
            data = copy.deepcopy(data1)
            data['title'] = dataframe.get('Title')[i]
            str = '<p style=\\"text-align: left;\\">'
            str += dataframe['Description'][i] + '</p>'
            data['description'] = str
            data['associatedAnimationIndex']=dataframe.get('Animation Index')[i]
            list_data.append(data)
        return list_data
    def replaceTitleInAnimations(self,dataframe, data1):
        list_data = []
        for i in range(dataframe.index.start, dataframe.index.stop):
            data = copy.deepcopy(data1)
            data['title'] = dataframe.get('Title for Animation')[i]
            data['startType'] = dataframe['Start Type'][i]
            list_data.append(data)
        return list_data
    def replaceTitleInLabels(self,dataframe, data1):
        list_data = []
        for i in range(dataframe.index.start, dataframe.index.stop):
            data = copy.deepcopy(data1)
            data['connectedModelComponentTitle'] = dataframe.get('Component Label')[i]
            data['connectionModelCompId'] = dataframe['connectedModelComponentTitle'][i]
            list_data.append(data)
        return list_data
    def getLatestExport(self):
        dir = str(up(up(up(__file__))))
        search_dir = dir + "\\hackathon\\hackathon\\excel\\*"
        list_of_files = glob.glob(search_dir)  # * means all if need specific format then *.csv
        latest_file = max(list_of_files, key=os.path.getctime)
        # print(latest_file)
        return latest_file
    def main(self,df,df1):
        print('main')
        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                if df.iat[row, col] == 'Steps':
                    row_steps = row

                if df.iat[row, col] == 'Animations':
                    row_animation = row
                    break
        Labels = df.iloc[1:row_steps - 2]
        Labels.columns = ['Serial Number', 'connectedModelComponentTitle', 'Component Label']
        Animations = df.iloc[row_animation + 2:]
        Animations.columns = ['Animation Index', 'Title for Animation', 'Start Type']
        Steps = df1.iloc[row_steps + 2:row_animation - 2]
        Steps.columns = ['Step Id', 'Title', 'Description', 'Animation Index']
        StepsJson = self.replaceTitleInSteps(Steps, StepsJsonData)
        animateJson = self.replaceTitleInAnimations(Animations, AnimationJsonData)
        cardsJson=self.replaceCArdsSteps(Steps,cardsData)
        print(cardsJson)
        FinalJson['task']['animations'] = animateJson
        labelsJson = self.replaceTitleInLabels(Labels, LabelsJsonData)
        FinalJson['task']['annotations']['annotationData'] = labelsJson
        FinalJson['task']['workInstructions']['cardsData']=cardsJson
        FinalJson['task']['workInstructions']['instructions'] = StepsJson
        return FinalJson
        # print('Final Json:', FinalJson)
    def post(self, request):
        serializer = ApiSerializer(data=request.data)
        if(serializer.is_valid()):
            file=request.data['excel']
            path = default_storage.save('hackathon/excel/PrinterModel.xlsx', ContentFile(file.read()))
            print('file saved in directory')
            filepath=self.getLatestExport()
            df = pd.read_excel(filepath, sheet_name='PrinterDisAssembly', usecols='A:C')
            df1 = pd.read_excel(filepath, sheet_name='PrinterDisAssembly', usecols='A:D')
            finalJson = self.main(df,df1)
            print(finalJson)
            # df=pd.read_excel('hackathon/excel/PrinterModel.xlsx')
            # finaljson=main()
            return Response({"data":finalJson}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "check the request body"}, status=status.HTTP_400_BAD_REQUEST)



    def helloworld(self):
        print('helloworlds')