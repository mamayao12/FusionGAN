import torch
print(torch.cuda.is_available())        # True 表示 GPU 可用
print(torch.version.cuda)               # PyTorch 使用的 CUDA 版本
print(torch.cuda.get_device_name(0))    # GPU 型号