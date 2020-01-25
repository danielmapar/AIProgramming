import torch
import numpy as np
from torch import nn, optim
import torch.nn.functional as F
from torchvision import datasets, transforms, models
from collections import OrderedDict
from PIL import Image

class Util(object):

    @staticmethod
    def load_data(data_dir="./flowers" ):
        train_dir = data_dir + '/train'
        valid_dir = data_dir + '/valid'
        test_dir = data_dir + '/test'

        train_transforms = transforms.Compose([transforms.RandomRotation(50),
                                            transforms.RandomResizedCrop(224),
                                            transforms.RandomHorizontalFlip(),
                                            transforms.ToTensor(),
                                            transforms.Normalize([0.485, 0.456, 0.406],
                                                                    [0.229, 0.224, 0.225])])

        test_transforms = transforms.Compose([transforms.Resize(256),
                                            transforms.CenterCrop(224),
                                            transforms.ToTensor(),
                                            transforms.Normalize([0.485, 0.456, 0.406],
                                                                [0.229, 0.224, 0.225])])

        validation_transforms = transforms.Compose([transforms.Resize(256),
                                                    transforms.CenterCrop(224),
                                                    transforms.ToTensor(),
                                                    transforms.Normalize([0.485, 0.456, 0.406],
                                                                        [0.229, 0.224, 0.225])])

        train_dataset = datasets.ImageFolder(train_dir, transform=train_transforms)
        validation_dataset = datasets.ImageFolder(valid_dir, transform=validation_transforms)
        test_dataset = datasets.ImageFolder(test_dir ,transform = test_transforms)

        train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True)
        validation_loader = torch.utils.data.DataLoader(validation_dataset, batch_size=64, shuffle=True)
        test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=64, shuffle=True)

        return train_loader , validation_loader, test_loader, train_dataset

    @staticmethod
    def model_setup(architecure='vgg16', dropout=0.5, hidden_units=100, learning_rate=0.001, hardware='gpu'):

        architecures = { "vgg16":25088,
                        "inception":2048,
                        "alexnet":9216 }
        
        if architecure == 'vgg16':
            model = models.vgg16(pretrained=True)
        elif architecure == 'inception':
            model = models.inception(pretrained=True)
        elif architecure == 'alexnet':
            model = models.alexnet(pretrained = True)
        else:
            print("I am sorry but {} is not a valid architecure. Did you mean vgg16, inception or alexnet?".format(structure))

        # Freeze parameters so we don't backprop through them
        for param in model.parameters():
            param.requires_grad = False

        from collections import OrderedDict
        classifier = nn.Sequential(OrderedDict([
                                    ('dropout',nn.Dropout(dropout)),
                                    ('inputs', nn.Linear(architecures[architecure], hidden_units)),
                                    ('relu1', nn.ReLU()),
                                    ('hidden_layer_1', nn.Linear(hidden_units, 80)),
                                    ('relu2',nn.ReLU()),
                                    ('hidden_layer_2',nn.Linear(80, 70)),
                                    ('relu3',nn.ReLU()),
                                    ('hidden_layer_3',nn.Linear(70, 102)),
                                    ('output', nn.LogSoftmax(dim=1))
                                ]))

        model.classifier = classifier
        criterion = nn.NLLLoss()
        optimizer = optim.Adam(model.classifier.parameters(), lr=learning_rate)

        if torch.cuda.is_available() and hardware == 'gpu':
            model.cuda()

        return model, criterion, optimizer

    @staticmethod
    def test_accuracy(model, test_loader, hardware="gpu"):
        accuracy = 0

        for ii, (test_inputs, test_labels) in enumerate(test_loader):
            # Move input and label tensors to the GPU (if available)
            if torch.cuda.is_available() and hardware == 'gpu':
                test_inputs, test_labels = test_inputs.to('cuda'), test_labels.to('cuda')

            # Get the class probabilities
            ps = torch.exp(model(test_inputs))
            
            # Make sure the shape is appropriate, we should get 102 class probabilities for 64 examples
            top_p, top_class = ps.topk(1, dim=1)
            
            # Look at the most likely classes for the first 10 examples
            equals = top_class == test_labels.view(*top_class.shape)
            
            accuracy += torch.mean(equals.type(torch.FloatTensor))
            
        accuracy = accuracy / len(test_loader)
        print(f'Accuracy of the network on test images: {accuracy.item()*100}%')

    @staticmethod
    def train_network(train_loader, validation_loader, model, criterion, optimizer, epochs=5, print_every=5, hardware='gpu'):
        steps = 0

        train_losses, validation_losses = [], []
        for e in range(epochs):
            running_loss = 0
            
            for ii, (train_inputs, train_labels) in enumerate(train_loader):
                steps += 1
                # Move input and label tensors to the GPU (if available)
                if torch.cuda.is_available() and hardware == 'gpu':
                    train_inputs, train_labels = train_inputs.to('cuda'), train_labels.to('cuda')
                
                optimizer.zero_grad()

                # Forward and backward passes
                outputs = model.forward(train_inputs)
                loss = criterion(outputs, train_labels)
                loss.backward()
                optimizer.step()
                
                running_loss += loss.item()

                if steps % print_every == 0:
                    # Deactivate dropout
                    model.eval()
                    validation_loss = 0
                    accuracy = 0
                    
                    for ii, (validation_inputs, validation_labels) in enumerate(validation_loader):
                        optimizer.zero_grad()
                        
                        # Move input and label tensors to the GPU (if available)
                        if torch.cuda.is_available() and hardware == 'gpu':
                            validation_inputs, validation_labels = validation_inputs.to('cuda'), validation_labels.to('cuda')
                            model.to('cuda')
                        
                        with torch.no_grad():    
                            outputs = model.forward(validation_inputs)
                            validation_loss = criterion(outputs, validation_labels)
                            ps = torch.exp(outputs).data 
                            equality = (validation_labels.data == ps.max(1)[1])
                            accuracy += equality.type_as(torch.FloatTensor()).mean()
                            
                    validation_loss = validation_loss / len(validation_loader)
                    train_loss = running_loss / len(train_loader)
                    
                    train_losses.append(train_loss)
                    validation_losses.append(validation_loss)
                    
                    accuracy = accuracy / len(validation_loader)
                    
                    print("Epoch: {}/{}... ".format(e+1, epochs),
                        "Training Loss: {:.4f}".format(running_loss/print_every),
                        "Validation Loss {:.4f}".format(validation_loss),
                        "Validation Accuracy: {:.4f}".format(accuracy))
                    
                    running_loss = 0

    @staticmethod
    def save_checkpoint(model, class_to_idx, path='checkpoint.pth', architecture='inception', hidden_units=100, dropout=0.5, learning_rate=0.001, epochs=10):
        model.class_to_idx = class_to_idx
        torch.save({
                'architecture': architecture,
                'hidden_units': hidden_units,
                'dropout': dropout,
                'learning_rate': learning_rate,
                'state_dict': model.state_dict(),
                'class_to_idx': model.class_to_idx,
                'number_of_epochs': epochs},
                'checkpoint.pth')

    @staticmethod
    def load_checkpoint(path='checkpoint.pth', hardware="gpu"):
        checkpoint = torch.load(path)

        architecture = checkpoint['architecture']
        hidden_units = checkpoint['hidden_units']
        dropout = checkpoint['dropout']
        learning_rate=checkpoint['learning_rate']

        model,_,_ = Util.model_setup(architecture, dropout, hidden_units, learning_rate, hardware)
        model.class_to_idx = checkpoint['class_to_idx']
        model.load_state_dict(checkpoint['state_dict'])
        
        return model

    @staticmethod
    def process_image(image_path):

        return transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])(Image.open(image_path))
    
    @staticmethod
    def predict(image_path, model, topk=5, hardware='gpu'):
        if torch.cuda.is_available() and hardware == 'gpu':
            model.to('cuda:0')

        img_torch = Util.process_image(image_path).unsqueeze_(0).float()
        
        if hardware == 'gpu':
            with torch.no_grad():
                output = model.forward(img_torch.cuda())
        else:
            with torch.no_grad():
                output=model.forward(img_torch)
            
        probability = F.softmax(output.data,dim=1)
        
        return probability.topk(topk)
