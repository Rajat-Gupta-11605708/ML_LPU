from numpy import *

def sigmoid(x):
    return 1/(1+exp((-x)))

def derivative_sigmoid(x):
    return x*(1-x)


x = array([[1,0,1,0],[1,0,1,1],[0,1,0,1]])
y = array([[1],[1],[0]])


#Variable Initialization
epoch = 5000        #Set training iterations
lr = 0.51            #Set learning rate
input_layer_neurons = x.shape[1]
# print(input_layer_neurons)
hidden_layer_neuron = 3
output_neuron = 1

wh = random.uniform(size=(input_layer_neurons, hidden_layer_neuron))
bh = random.uniform(size=(1,hidden_layer_neuron))
wout = random.uniform(size=(hidden_layer_neuron, output_neuron))
bout = random.uniform(size=(1,output_neuron))


for i in range (epoch):
    # forward propogation
    print("Epoch : ",i)
    hidden_layer_input1 = dot(x,wh)
    hidden_layer_input = hidden_layer_input1 + bh
    hidden_layer_activation = sigmoid(hidden_layer_input)

    output_layer_input1 = dot(hidden_layer_activation,wout)
    output_layer_input = output_layer_input1 + bout
    output = sigmoid(output_layer_input)

    #back Propogation

    E = y-output
    slope_output_layer = derivative_sigmoid(output)
    slope_hidden_layer = derivative_sigmoid(hidden_layer_activation)
    d_output = E*slope_output_layer

    Error_at_hidden_layer = d_output.dot(wout.T)
    d_hidden_layer = Error_at_hidden_layer * slope_hidden_layer
    wout += hidden_layer_activation.T.dot(d_output)*lr
    bout += sum(d_output, axis=0, keepdims=True)
    wh += x.T.dot(d_hidden_layer)*lr
    bh += sum(d_hidden_layer, axis=0, keepdims=True)

print("Target Values :\n",y)
print("\nOutput Values :\n",output)
print("\nE = Target - Output :\n", E)
print("\n")