import torch.nn as nn
import torch.nn.functional as F
from torchvision import models

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
	
	#self.model_ft = models.vgg19_bn(pretrained=True)
	self.model_ft = models.densenet201(pretrained=True)
	
        #self.model_ft = models.resnet50(pretrained=True)
        #for param in self.model_ft.parameters():
        #    param.requires_grad = False

        #self.transition = nn.Conv2d(2048, 2048, kernel_size=3, padding=1, stride=1, bias=False)
        #self.globalPool = nn.MaxPool2d(32)
        #self.prediction = nn.Sequential(nn.Linear(2048, 8), nn.Sigmoid())

	#numm_ftrs = self.model_ft.fc.in_features
	#self.model_ft.fc = nn.Linear(num_ftrs, 8)
	
	
	#self.fc = nn.Sequential(
        #    nn.Linear(512 * 7 * 7, 4096),
        #    nn.ReLU(True),
        #    nn.Dropout(),
        #    nn.Linear(4096, 4096),
        #    nn.ReLU(True),
        #    nn.Dropout(),
        #    nn.Linear(4096, 1),
        #)
	#self.fc = nn.Linear(num_ftrs, 1)
	#self.fc = nn.Linear(4096,1)
	
	self.classifier = nn.Linear(1920, 8)
	self.prediction = nn.Sigmoid()



    def forward(self, x):
	#x = self.model_ft.features(x)
        #x = x.view(x.size(0), -1)
        #x = self.fc(x)
	#x = self.prediction(x)
        #x = self.model_ft.bn1(x)
        #x = self.model_ft.relu(x)
        #x = self.model_ft.maxpool(x)

        #x = self.model_ft.layer1(x)
        #x = self.model_ft.layer2(x)
        #x = self.model_ft.layer3(x)
        #x = self.model_ft.layer4(x)


        #x = self.transition(x)
        #x = self.globalPool(x)
        #x = x.view(x.size(0), -1)
        #x = self.prediction(x)#14
	#x = self.model_ft(x)
	#x = self.prediction(x)
        
	
	features = self.model_ft.features(x)
        out = F.relu(features, inplace=True)
        out = F.avg_pool2d(out, kernel_size=7, stride=1).view(features.size(0), -1)
        #print(out)
	x = self.classifier(out)
	return x

