# HCOMB-2-CA ReadME

HCOMB-2-CA is an innovative software tool designed to translate lattice representations of protein structures into carbon alpha (CA)-only backbone structures. It is a complementary counterpart to [PDB2Lattice](https://github.com/ahabegger/PDB-2-Lattice), focusing on converting simplified lattice models into detailed yet streamlined CA backbone structures suitable for extensive biological analysis. 

This program addresses the need for reconstructing detailed protein structures from their simplified forms, facilitating a deeper understanding of protein folding and function. Lattice2Backbone is particularly valuable in structural biology and bioinformatics, enabling researchers to efficiently bridge the gap between highly abstracted lattice models and more detailed, biologically relevant CA backbone structures.

## References

The "References" section in the `README.md` file provides important links related to the project:

- [3.8 A](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3892923/): This is a link to a scientific article or resource that is relevant to the project. The exact content of this link is not specified, but it's likely to provide some background or context for the project.

- [PULCHRA article](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2692024/): This is a link to a scientific article about PULCHRA, a program used for protein structure reconstruction. This article can provide more information about how PULCHRA works and why it's used in this project.

- [Download PULCHRA](https://cssb.biology.gatech.edu/skolnick/files/PULCHRA/pulchra304.tgz): This is a direct link to download the PULCHRA program. As PULCHRA is used in this project, users will need to download and install it.

- [PULCHRA Documentation](https://cssb.biology.gatech.edu/skolnick/files/PULCHRA/README.PULCHRA): This is a link to the documentation for PULCHRA. It can provide more detailed information about how to use PULCHRA and its various features.

- [Quantum-Protein-Lattice-Folding](https://github.com/ahabegger/Quantum-Protein-Lattice-Folding): This is a link to another GitHub repository. The program in this project is used to interpret the results from the Quantum-Protein-Lattice-Folding project. This link can provide more context about how the two projects are related.

## Requirements

- pip~=22.3.1
- numpy~=1.26.3
- pandas~=2.1.4

## Usage

The program can be run from the command line with the following arguments:

- `csv`: The csv file that contains the xyz coordinates of structure simplification.
- `-a`, `--add-output`: Add the output to the ML dataset.

Example:

```bash
python main.py input.csv -a output.csv
```

## License

This project is licensed under the MIT License.

## Acknowledgements

Dr. Khodakhast Bibak advised at each step of the development of this project, and his guidance was invaluable.

## Contact

I can be contacted by email at my university email habeggaj (at sign) miamioh (dot) edu.