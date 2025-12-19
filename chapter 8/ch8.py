# Problem 1: NumPy Operations

 import numpy as np
   
  arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
   
  mean_val = np.mean(arr)
  median_val = np.median(arr)
  std_val = np.std(arr)
   
  print(f"Mean: {mean_val}")
 print(f"Median: {median_val}")
 print(f"Standard Deviation: {std_val:.3f}")


# Problem 2: Pandas Filtering

import pandas as pd
   
  data = {
      'Name': ['Ali', 'Mona', 'Omar', 'Sara'],
      'Age': [20, 22, 21, 23],
      'Score': [85, 92, 78, 95]
  }
   
  df = pd.DataFrame(data)
 high_scorers = df[df['Score'] > 80]
 print(high_scorers)


# Problem 3: Visualization with Matplotlib

 import matplotlib.pyplot as plt
   
  x = [1, 2, 3, 4, 5]
  y = [1, 4, 9, 16, 25]
   
  plt.plot(x, y)
  plt.xlabel('X values')
  plt.ylabel('Y values')
  plt.title('Square Function Graph')
 plt.show()
  




# Problem 4: Flask Application

from flask import Flask
   
  app = Flask(__name__)
   
  @app.route('/hello')
  def hello():
      return "Hello, Advanced Python!"
   
  if __name__ == '__main__':
     app.run(debug=True)
 



# Problem 5: PyTorch Tensor Operations
 import torch
   
  tensor1 = torch.tensor([1, 2, 3])
  tensor2 = torch.tensor([4, 5, 6])
   
  dot_product = torch.dot(tensor1, tensor2)
  elementwise_mul = tensor1 * tensor2
   
 print(f"Dot Product: {dot_product}")
 print(f"Element-wise Multiplication: {elementwise_mul}")
