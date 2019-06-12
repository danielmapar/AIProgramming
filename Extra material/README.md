# Short Answer Grader

* Basics of Netural Networks

    * Videos
        * What are neural networks: https://www.youtube.com/watch?v=aircAruvnKk
        * How neural networks learn: https://www.youtube.com/watch?v=IHZwWFHWa-w
        * More on the basics of neural networks: https://www.youtube.com/watch?v=UNmqTiOnRfg

    * Gradient descent
        * Look at surroundings and choose path with highest descent 
        * A derivative to calculate the distance between where we are and where we wanna go
        * Works with continuos values
    
    * Minimize error
        * Minimize incorrect classification

    * Types of data
        * Discrete Data
            * Can only take certain values
        * Continuos Data
            * Can take any value (within a range)
    
    * Logistic Regression
        * Penalize miss classification points
        * Error function is sum of all penalizations 
            * Minimize error 
    
    * Activation function
        * Normalize data from 0 to 1 (sigmoid)
            * Calculate weight using the sigmoid function so we get activations between 0 and 1
            * ![sigmoid](./images/sigmoid.png)
                * People use `ReLU(a) = max(0, a)` now a days (0 to a)
            * ![activation](./images/activation.png)
                * How positive is this number?
            * ![bias](./images/bias.png) 
                * Only activate meaningfully when weighted sum > 10
            * ![matrix-multiplication](./images/matrix-multiplication.png) 
            * ![basic-feedfoward](./images/basic-feedfoward.png) 

    * Probability of all 4 of them happening (the points are on those colors)
        * Maximum likelihood
        * ![probability](./images/probability.png)   
        * ![probability2](./images/probability2.png)  
        * ![probability2](./images/probability3.png) 
            * That is gonna be the penalty / the error function
                * Every log is a penalization 
            * This is logistic regression 
                
    * Neural Network
        * ![neural-network](./images/neural-network.png) 
            * Combining regions 
            * You can give a higher weight to a region compared to another one
                * Linear combination of two areas
                * ![neural-network2](./images/neural-network2.png)  
                * ![neural-network3](./images/neural-network3.png)  
                * ![neural-network4](./images/neural-network4.png)    
                * ![neural-network5](./images/neural-network5.png)    
                * ![neural-network6](./images/neural-network6.png)   
                * ![deep-nn](./images/deep-nn.png)   
    
    * How Neural Networks learn
        * Initialize weights and biases totally randomly 
            * After running the neural network, the output will be trash
        * With that output, we will run a `cost` function
            * ![cost-function](./images/cost-function.png)
            * ![cost-function2](./images/cost-function2.png)
            * Add up the square of the differences (what we outputted vs what we want)
            * This will give us the cost of a single training example
        * ![cost-function3](./images/cost-function3.png)
            * This sum is small when the network confidently classifies the image correctly 
                * ![cost-function4](./images/cost-function4.png) 
            * It will be large when the network does not know what it is doing
        * We then run this cost for the tens of thousants training entries examples at our disposal 
            * This average cost of all training data will tell us how lousy the network is
            * For each set of `inputs + weights + biases` we will have a `cost`
                * ![cost-function0](./images/cost-function0.png)
                * ![cost-function00](./images/cost-function00.png)
                    * Lets simplify the input to be a single weight
                * We must find a set of inputs that minimizes the value of this function (that is where calculus comes to play)
                * Which direction should I step to make that output lower (gradiant descent)
                    * ![gradiant-descent](./images/gradiant-descent.png) 
                    * Finding the slope (inclination) of a function (vertical change between two points)
                        * The slope is defined as the ratio of the vertical change between two points, the rise, to the horizontal change between the same two points, the run.
                        * Shift to the left if that slope is positive 
                            * ![slope1](./images/slope1.png) 
                        * Shift to the right if that slope is negative 
                            * ![slope2](./images/slope2.png) 
                    * If you do this repeatedly, at each point checking the new slope and taking the appropriate step, you are gonna approach some local minimum of the function
                        * In mathematical analysis, the maxima and minima (the respective plurals of maximum and minimum) of a function, known collectively as extrema (the plural of extremum), are the largest and smallest value of the function, either within a given range (the local or relative extrema) or on the entire domain of a function (the global or absolute extrema).
                    * There are many possible values you could land in, depending on the random input you start at (weights and biases)
                        * Depending on the random input you start with, we may face a different `cost`, and because of that a different `slope`
                        * ![slope3](./images/slope3.png) 
                    
                    * **Their is no guarantee that the local minimum you land-in is gonna be the smallest possible value of the `cost` function**
                        * Local minimum = Doable
                        * Global minimum = Crazy hard
                    
                    * Also, if you make your step sizes proportional to the slop, then when the slop is flattening out towards the minimum, your steps gets smaller and smaller. That kind of helps you from over-shooting
                        * ![step2](./images/step2.png) 
                        * ![step1](./images/step1.png)
                    
                    * Thinking about a deeper input space (2 or more inputs/weights and one output), we can imagine a 3d environemnt and we need to determine which weight should we change in order to minimize the `cost`. Forget about the slope, and try to imagine which direction should you move in order to minimize `cost` (downhill direction)
                        * The downhill direction (like a ball falling downhill)
                            * ![downhill](./images/downhill.png) 
                            * That is multi-variable calculus (gradiant of a function)
                                * Direction of `steepest ascent and descent`. `cost` should be zero
                                * ![gradient](./images/gradient.png)
                            * For calculus go to (khanacademy.com)
                    * ![calculate-gradient](./images/calculate-gradient.png) 
                    * ![calculate-gradient2](./images/calculate-gradient2.png) 
                        * A continuos process of calculating the `cost`, the gradient, and subtracting it by each weight related to the input. That will leave us with a new weight value that we can again calculate the `cost` and the gradiant again. We will do this till we achieve local minimum to that input
                        * The gradient is just a vector that we will subtract with our current vector of weights.
                            * We are decresing the `cost` function by taking the gradient
                        * This `cost` function involves an average of all training data
                            * So if we minimize it, it impacts all of those samples
                    
                    * The algorithm for computing this gradient efficiently, which is essentially the earth of how a neural networks learns its called back propagation.
                    * This is why artificial neurals have continuos ranging activations, rather than being simply active or inactive (binary way). The way biological neurons are.
                        * This process of repeatedly nudging an input of a function by some mulitple of negative gradient is called `gradient descent`.
                    * The pictures in this document are two inputs because nudges in a thirteen thousand dimensional input space are a little hard to wrap your mind around, but there is actually a nice non-spatial way to think about this.
                        * ![gradient-descent](./images/gradient-descent1.png)  
                        * ![gradient-descent](./images/gradient-descent2.png)
                            * The gradient also shows us which of the weights are more important to be updated
                        * ![steepest-ascent](./images/steepest-ascent.png) 
                        * ![steepest-ascent](./images/steepest-ascent2.png)  
    
    * Back propagation
        * An algorithm for computing that crazy complicated gradient 

        * ![backpropagation](./images/backpropagation.png)

        * Which weights give you more "ban for you buck"

        * Increase the weights to neurons with high activation
            * `w0a0 + w1a1 + ... + w5a5`
            * If `a0` has a higher activation value, we should play with its weight `w0` in order to achieve the activations of number `2`
                * ![backprop-example](./images/backprop-example.png)  
        

        * The algorithm for determining how a single training example would like to nudge the weights and biases, not just in terms of wheter they should go up or down, but in terms of what relative proportions to those changes cause the most rapid decrease to the cost.

        * Here, the biggest increases to weights, the biggest strengthening of connections, happens between neurons which are the most active, and the ones which we wish to become more active.

        * We could also change the previous layer, and give a stronger activation value to the neurons with strong weights. Example (a0 = 2, but its weight is 10).

            * Just as with the last layer, it's helpfull to just keep a note of what those desired changes are.
            * But keep in mind, zooming out one step here, this is only what that digit 2 output neuron wants.
                * ![backprop-example2](./images/backprop-example2.png)
            * Remember, we also want all of the other neurons in the last layer to become less active, and each of those other output neurons has its own thoughts about what should happen to that second-to-last layer (we could output from 0 to 9)
            * So, the desire of this digit 2 neuron is added together with the desires of all the other output neurons for what should happen to this second-to-last layer. Again, in proportion to the corresponding weights. 
                * ![backprop-example3](./images/backprop-example3.png) 
            
            * ![backprop-example4](./images/backprop-example4.png)  
                * We will do back prop on various instances, and average over all training data
                * This loosely speaking is the negative gradient mentioned before
                    * ![backprop-example5](./images/backprop-example5.png) 

    * Extra notes
        * https://machinelearningmastery.com/difference-between-a-batch-and-an-epoch/

        * The batch size is a number of samples processed before the model is updated.

        * The number of epochs is the number of complete passes through the training dataset.

            * Assume you have a dataset with 200 samples (rows of data) and you choose a batch size of 5 and 1,000 epochs.

            * This means that the dataset will be divided into 40 batches, each with five samples. The model weights will be updated after each batch of five samples.

            * This also means that one epoch will involve 40 batches or 40 updates to the model.

            * With 1,000 epochs, the model will be exposed to or pass through the whole dataset 1,000 times. That is a total of 40,000 batches during the entire training process.

        * Stochastic (randomly determined) gradient descent is a learning algorithm that has a number of hyperparameters.

        * Two hyperparameters that often confuse beginners are the batch size and number of epochs. They are both integer values and seem to do the same thing.

        * The batch size is a hyperparameter of gradient descent that controls the number of training samples to work through **before the model’s internal parameters are updated**.
            * When all training samples are used to create one batch, the learning algorithm is called batch gradient descent. When the batch is the size of one sample, the learning algorithm is called stochastic gradient descent. When the batch size is more than one sample and less than the size of the training dataset, the learning algorithm is called mini-batch gradient descent.
        
        * The number of epochs is a hyperparameter of gradient descent that controls the number of complete passes through the training dataset.


* Recurrent Neural Networks

    * https://www.youtube.com/watch?v=WCUNPb-5EYI&t=692s

    * One hot encoding (vectors of 0s with only one value as 1)

    * The output generated by the network servers as its own input
        * https://www.youtube.com/watch?v=UNmqTiOnRfg
        * https://www.youtube.com/watch?v=WCUNPb-5EYI&t=47s
        * ![rnn](./images/rnn.png)
    
    * Useful when your data is sequential
        * The next data points depends a lot on the previous ones 
        * Stock prediction 
        * Text Generation (trying to guess the next word)
        * Voice recognition (depends a lot on the previous words)
    
    * Training with gradient descent 

    * Squashing function - Hyperbolic tangent

        * You take all of your votes coming out and you subject them to this squashing function. For instance if something received a total vote of 0.5 you draw a vertical line up where it crosses the function you draw a horizontal line over to the y-axis and there is your squashed version out.

        * ![squash](./images/squash.png)

            * No matter what your start with, the answer stays between -1 and 1.
        
        * ![squash2](./images/squash2.png)
    
    * ![rnn2](./images/rnn2.png)

        * If something got voted for twice (multiplied by 2), in that case it would get twice as big everytime.

        * By ensuring that it is always -1 to 1, you can multiply as much as you want (Negative feedback)
    
    * Because predictions look just to the previous input (previous prediction) it has really short term memory, then it does not use the information from further back.

    * ![rnn3](./images/rnn3.png) 

    * ![plus-sign](./images/plus-sign.png)
        * Look at the graph again. We are adding memory to the network feedback loop

    * ![multiplication-sign](./images/multiplication-sign.png)
        * This is gating 
        * We have a signal (can be anything) and gating vector. If that we can let that signal come all in, or maybe just part of it.
            * Open gate is 1, and a closed one is 0
        * In order to do gatting we need to introduce another squashing function
            * ![squash4](./images/squash4.png) 
    
    * ![rnn3](./images/rnn3.png) 

        * Basically a prediction is made
        * We run a squashing function from -1 to 1 in order to balance the feedback loop
        * A copy of those predictions is held on too for the next time step, the next pass through the network
            * Some of them are forgotten (gating) and some of them are remembered
            * The ones that are remembered are added back to the prediction 
        * Prediction + memories we have accumulated (the ones we decided to maintain)
        * We have a separate neural network that learns when to forget what 
    
    * ![rnn5](./images/rnn5.png) 

        * We may not want to release those memories out as new predictions every time.

        * We want a little filter in order to keep our memories inside and let out predictions get out

        * A selection of memories (has its own NN and voting process)
            * What should be kept internal, and what should be released as a prediction
        
        * We have squashing functions all over because the additions / multiplications may inflate the values to over 1

    
    * One NN for predictions, another for forgetting memories, and a final one for selecting memories to influence the prediction

        * ![rnn6](./images/rnn6.png) 

            * Ignore things that are not immediatly relevant. So they sat aside and dont cloud the prediction moving forward 
        
        * Sequential patterns works really well