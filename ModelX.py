import torch.nn as nn
import torch.nn.functional as F
import torch
from torchvision import models


class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.model_ft = models.vgg16(pretrained=True)
        self.classifier = nn.Sequential(
            nn.Linear(512 * 7 * 7 + 3, 4096),
            nn.ReLU(True),
            nn.Dropout(),
            nn.Linear(4096, 4096),
            nn.ReLU(True),
            nn.Dropout(),
            nn.Linear(4096, 3),
        )
        self.prediction = nn.Sigmoid()

    def forward(self, x):
        indices = torch.LongTensor(range(0, 512 * 7 * 7))
        txt_indices = torch.LongTensor(range(512 * 7 * 7, 512 * 7 * 7 + 3))
        ix = torch.index_select(x, 0, indices)
        tx = torch.index_select(x, 0, txt_indices)

        ix = ix.view(-1, 3, 227, 227)
        ix = self.model_ft.features(ix)

        ix = ix.view(ix.size(0), -1)
        x = torch.cat(ix, tx)
        x = self.classifier(x)
        x = self.prediction(x)
        return x
