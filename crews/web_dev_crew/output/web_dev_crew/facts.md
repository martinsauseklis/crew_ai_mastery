# 100 AI Concept Facts for Interactive Learning Flashcards

## Fundamental AI Concepts (1-15)

1. **What is Artificial Intelligence?** - AI is a set of technologies that empowers computers to learn, reason, and perform tasks that traditionally required human intelligence, such as understanding language, analyzing data, and making decisions.

2. **Machine Learning Definition** - Machine Learning is a subfield of AI that gives computers the ability to learn from data and improve their performance without being explicitly programmed for every task.

3. **Deep Learning Explained** - Deep learning is a subset of machine learning that uses artificial neural networks with multiple layers to mimic the learning process of the human brain.

4. **AI vs ML vs DL Relationship** - AI is the broadest concept, Machine Learning is a subset of AI, and Deep Learning is a subset of Machine Learning that uses neural networks with many layers.

5. **The Four Types of AI** - According to current classification: Reactive machines, Limited memory, Theory of mind, and Self-aware AI (the last two are not yet scientifically possible).

6. **Supervised Learning** - A type of machine learning where the model learns from labeled data, with input-output pairs provided during training.

7. **Unsupervised Learning** - Machine learning approach where the model finds patterns in unlabeled data without predefined outputs or labels.

8. **Reinforcement Learning** - A learning paradigm where an agent learns to make decisions by taking actions in an environment to maximize cumulative reward.

9. **Semi-Supervised Learning** - A hybrid approach that uses a small amount of labeled data combined with a large amount of unlabeled data for training.

10. **Neural Network Definition** - A computational model inspired by biological neural networks, consisting of interconnected nodes (neurons) organized in layers.

11. **Training Data** - The dataset used to teach a machine learning model to make predictions or decisions by learning patterns and relationships.

12. **Test Data** - A separate dataset used to evaluate the performance and generalization ability of a trained model on unseen data.

13. **Validation Data** - Data used during model development to tune hyperparameters and make decisions about model architecture without touching the test set.

14. **Feature Engineering** - The process of selecting, creating, and transforming raw data into features that better represent the underlying problem to machine learning models.

15. **Model Generalization** - The ability of a machine learning model to perform well on new, unseen data rather than just memorizing the training data.

## Neural Network Architecture (16-30)

16. **Artificial Neural Network (ANN)** - The basic form of neural networks with an input layer, one or more hidden layers, and an output layer, connected by weighted edges.

17. **Input Layer** - The first layer of a neural network that receives the initial data and passes it to subsequent layers for processing.

18. **Hidden Layers** - Intermediate layers between input and output layers where the actual learning and feature extraction occurs through non-linear transformations.

19. **Output Layer** - The final layer of a neural network that produces the prediction, classification, or other desired output.

20. **Weights in Neural Networks** - Numerical parameters that determine the strength of connections between neurons, adjusted during training to minimize error.

21. **Bias in Neural Networks** - An additional parameter in neurons that allows the activation function to be shifted, helping the model fit the data better.

22. **Neuron/Node** - The basic computational unit in a neural network that receives inputs, applies weights, adds bias, and passes the result through an activation function.

23. **Forward Propagation** - The process of passing input data through the network layers from input to output to generate predictions.

24. **Backpropagation** - The algorithm used to train neural networks by calculating gradients of the loss function and propagating them backward through the network.

25. **Epoch** - One complete pass through the entire training dataset during the training process.

26. **Batch** - A subset of the training data processed together before updating model weights.

27. **Batch Size** - The number of training examples used in one iteration of model training.

28. **Learning Rate** - A hyperparameter that controls how much the model weights are adjusted during training in response to the calculated error.

29. **Loss Function** - A mathematical function that measures how well the model's predictions match the actual values, guiding the optimization process.

30. **Gradient Descent** - An optimization algorithm that iteratively adjusts model parameters to minimize the loss function by moving in the direction of steepest descent.

## Activation Functions (31-40)

31. **Activation Function Purpose** - Mathematical functions applied to neuron outputs to introduce non-linearity, enabling neural networks to learn complex patterns.

32. **ReLU (Rectified Linear Unit)** - Activation function defined as f(x) = max(0, x), which outputs the input if positive, otherwise zero. Most popular due to computational efficiency.

33. **Sigmoid Function** - Activation function that squashes input values to range (0, 1), defined as f(x) = 1/(1 + e^(-x)). Often used in binary classification output layers.

34. **Tanh Function** - Hyperbolic tangent activation function that maps inputs to range (-1, 1), providing zero-centered outputs unlike sigmoid.

35. **Softmax Function** - Activation function used in output layers for multi-class classification, converting raw scores into probability distribution summing to 1.

36. **Leaky ReLU** - Variant of ReLU that allows small negative values (f(x) = x if x > 0, else αx where α is small), preventing dying neuron problem.

37. **Vanishing Gradient Problem** - Issue where gradients become extremely small during backpropagation, making it difficult to train deep networks, especially with sigmoid/tanh.

38. **Exploding Gradient Problem** - Opposite of vanishing gradients, where gradients become extremely large, causing unstable training and numerical overflow.

39. **Dying ReLU Problem** - Issue where neurons using ReLU activation can get stuck outputting zero for all inputs, stopping learning completely.

40. **ELU (Exponential Linear Unit)** - Activation function that smoothly handles negative values, reducing bias shift and bringing mean activations closer to zero.

## Convolutional Neural Networks (41-50)

41. **Convolutional Neural Network (CNN)** - A type of neural network specialized for processing grid-like data such as images, using convolutional layers to detect spatial patterns.

42. **Convolution Operation** - Mathematical operation that applies a filter/kernel to input data by sliding it across and computing dot products to extract features.

43. **Filter/Kernel** - Small matrix of weights that slides across input data in CNNs to detect specific features like edges, textures, or patterns.

44. **Feature Map** - The output produced by applying a convolutional filter to input data, highlighting where specific features are detected.

45. **Pooling Layer** - Layer in CNNs that reduces spatial dimensions of feature maps, decreasing computational load while retaining important information.

46. **Max Pooling** - Pooling operation that selects the maximum value from each region, preserving the strongest activations.

47. **Average Pooling** - Pooling operation that computes the average value in each region, providing a smoother down-sampling.

48. **Stride** - The number of pixels by which the filter moves across the input during convolution or pooling operations.

49. **Padding** - Adding extra pixels (usually zeros) around the input borders to control output size and preserve edge information.

50. **Computer Vision** - AI field focused on enabling computers to interpret and understand visual information from images and videos.

## Recurrent Neural Networks (51-60)

51. **Recurrent Neural Network (RNN)** - Neural network architecture designed for sequential data, maintaining hidden states that capture information from previous time steps.

52. **Sequential Data** - Data where order matters, such as time series, text, speech, or video, where context from previous elements influences current predictions.

53. **Hidden State** - Internal memory in RNNs that carries information from previous time steps, allowing the network to maintain context.

54. **LSTM (Long Short-Term Memory)** - Advanced RNN architecture with gates (forget, input, output) that better capture long-term dependencies and mitigate vanishing gradient issues.

55. **GRU (Gated Recurrent Unit)** - Simplified version of LSTM with fewer gates (reset and update), offering similar performance with reduced computational complexity.

56. **Forget Gate** - Component in LSTM that decides what information to discard from the cell state.

57. **Input Gate** - Component in LSTM that determines what new information to add to the cell state.

58. **Output Gate** - Component in LSTM that controls what information from the cell state to output.

59. **Sequence-to-Sequence Models** - Neural network architectures that transform one sequence into another, commonly used in translation and text generation.

60. **Bidirectional RNN** - RNN that processes sequences in both forward and backward directions, capturing context from both past and future.

## Transformers and Attention (61-70)

61. **Transformer Architecture** - Modern neural network architecture based on self-attention mechanisms, enabling parallel processing and long-range dependencies without recurrence.

62. **Attention Mechanism** - Method allowing models to focus on relevant parts of input when making predictions, weighing importance of different elements.

63. **Self-Attention** - Attention mechanism where a sequence attends to itself, computing relationships between all positions to understand context.

64. **Multi-Head Attention** - Extension of attention using multiple attention mechanisms in parallel, allowing the model to capture different types of relationships.

65. **Query, Key, and Value** - Three vectors in attention mechanisms: query (what we're looking for), key (what we're comparing against), value (actual information to retrieve).

66. **Positional Encoding** - Additional information added to transformer inputs to provide sequence order information, since transformers don't inherently process sequences sequentially.

67. **BERT (Bidirectional Encoder Representations from Transformers)** - Transformer-based model that understands context bidirectionally, revolutionizing natural language understanding tasks.

68. **GPT (Generative Pre-trained Transformer)** - Autoregressive transformer model trained to predict next tokens, capable of generating coherent text and few-shot learning.

69. **Encoder-Decoder Architecture** - Transformer structure with an encoder processing input and decoder generating output, used in translation and summarization.

70. **Pre-training and Fine-tuning** - Two-stage process where models are first trained on large general datasets, then adapted to specific tasks with smaller datasets.

## Natural Language Processing (71-78)

71. **Natural Language Processing (NLP)** - Branch of AI focused on enabling computers to understand, interpret, and generate human language.

72. **Tokenization** - Process of breaking text into smaller units (tokens) such as words, subwords, or characters for processing by NLP models.

73. **Word Embeddings** - Dense vector representations of words that capture semantic meaning, where similar words have similar vectors.

74. **Word2Vec** - Popular technique for creating word embeddings using shallow neural networks, capturing word relationships through context.

75. **Sentiment Analysis** - NLP task of determining emotional tone or opinion expressed in text (positive, negative, neutral).

76. **Named Entity Recognition (NER)** - Task of identifying and classifying named entities (people, organizations, locations, dates) in text.

77. **Part-of-Speech Tagging** - Labeling each word in text with its grammatical category (noun, verb, adjective, etc.).

78. **Machine Translation** - Automatic translation of text from one language to another using machine learning models.

## Generative AI (79-85)

79. **Generative AI** - AI systems that can create new content (text, images, audio, video) based on patterns learned from training data.

80. **Generative Adversarial Network (GAN)** - Architecture with two networks: generator creates fake samples, discriminator distinguishes real from fake, improving through competition.

81. **Generator Network** - Part of GAN that creates synthetic data samples attempting to fool the discriminator.

82. **Discriminator Network** - Part of GAN that evaluates whether samples are real (from training data) or fake (from generator).

83. **Variational Autoencoder (VAE)** - Generative model that learns to encode data into latent space and decode back, enabling generation of new similar samples.

84. **Diffusion Models** - Generative models that learn to reverse a gradual noising process, creating high-quality images and other content.

85. **Prompt Engineering** - Craft of designing effective text prompts to guide language models toward desired outputs.

## Model Evaluation and Metrics (86-95)

86. **Accuracy** - Percentage of correct predictions out of total predictions: (TP + TN) / (TP + TN + FP + FN).

87. **Precision** - Of all positive predictions, what fraction were correct: TP / (TP + FP). Important when false positives are costly.

88. **Recall (Sensitivity)** - Of all actual positives, what fraction were correctly identified: TP / (TP + FN). Important when missing positives is costly.

89. **F1 Score** - Harmonic mean of precision and recall: 2 × (Precision × Recall) / (Precision + Recall), balancing both metrics.

90. **Confusion Matrix** - Table showing true positives, true negatives, false positives, and false negatives for classification evaluation.

91. **ROC Curve** - Plot of true positive rate vs false positive rate at various classification thresholds, visualizing model performance.

92. **AUC (Area Under Curve)** - Area under ROC curve, measuring overall classification performance across all thresholds (0 to 1, higher is better).

93. **Overfitting** - Model learns training data too well, including noise, performing poorly on new data due to lack of generalization.

94. **Underfitting** - Model is too simple to capture underlying patterns in data, performing poorly on both training and test data.

95. **Cross-Validation** - Technique dividing data into folds, training on some and validating on others, rotating to assess model reliability.

## Regularization and Optimization (96-100)

96. **Regularization** - Techniques to prevent overfitting by adding constraints or penalties to model complexity (L1, L2, dropout).

97. **Dropout** - Regularization technique randomly deactivating neurons during training, forcing network to learn redundant representations and improving generalization.

98. **Batch Normalization** - Technique normalizing layer inputs to have zero mean and unit variance, stabilizing training and allowing higher learning rates.

99. **Transfer Learning** - Using knowledge from a model trained on one task to improve learning on a related but different task, reducing training time and data requirements.

100. **Hyperparameter Tuning** - Process of optimizing model configuration parameters (learning rate, batch size, number of layers) not learned during training, typically using grid search, random search, or Bayesian optimization.