import torch
import torch.nn as nn

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()

        self.conv=nn.Conv2d(1,1,3,padding=1,bias=True)
        self.conv.weight.data.fill_(0.3)
        self.conv.bias.data.fill_(0.2)


    def forward(self, x):
        x = self.conv(x)
        #tips不支持batchsize的默认 看NOTE：！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        # return x.view(x.size(0),-1)
        return x.view(-1,int(x.numel()//x.size(0)))


model = Model().eval()

x=torch.full((1,1,3,3),1.0)
y=model(x)

torch.onnx.export(
      model,(x,),"Lesson_true.onnx",verbose=True
                  )