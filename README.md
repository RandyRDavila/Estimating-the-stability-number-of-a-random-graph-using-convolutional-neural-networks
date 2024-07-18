# Estimating the Stability Number of a Random Graph Using Convolutional Neural Networks

This repository contains the code and data associated with the paper "Estimating the Stability Number of a Random Graph Using Convolutional Neural Networks" by Randy Davila.

## Abstract

Graph combinatorial optimization problems are widely applicable and notoriously difficult to compute; for example, consider the traveling salesman or facility location problems. In this paper, we explore the feasibility of using convolutional neural networks (CNNs) on graph images to predict the cardinality of combinatorial properties of random graphs and networks. Specifically, we use image representations of modified adjacency matrices of random graphs as training samples for a CNN model to predict the stability number of random graphs; where the stability number is the cardinality of a maximum set of vertices containing no pairwise adjacency. Our approach demonstrates the potential for applying deep learning in combinatorial optimization problems.


### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/CNN_Combinatorial_Optimization.git
    cd CNN_Combinatorial_Optimization
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Notebooks

Explore the Jupyter notebooks in the `notebooks/` directory for detailed walkthroughs of the data generation, model training, and evaluation processes.



## References

If you use this code or dataset in your research, please cite our paper:

Davila, R. (2024). Estimating the stability number of a random graph using convolutional neural networks. *Journal Name*. [Link to the paper]

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please contact Randy Davila at rrd6@rice.com.
