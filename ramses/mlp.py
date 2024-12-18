import torch

class Mlp_3(torch.nn.Module):
    
    def __init__(self, diminit=32, dimint=128, dimsal=5):
        super().__init__()
        self.capa_1 = torch.nn.Linear(in_features=diminit, out_features=dimint)
        self.capa_2 = torch.nn.Linear(in_features=dimint, out_features=dimint)
        self.capa_3 = torch.nn.Linear(in_features=dimint, out_features=dimsal)

    def forward(self, x):

        x = self.capa_1(x)
        x = torch.nn.functional.relu(x)
        x = self.capa_2(x)
        x = torch.nn.functional.relu(x)
        x = self.capa_3(x)
        x = torch.nn.functional.log_softmax(x, dim=-1)

        return x.reshape(1,1,-1)
    
    

    



