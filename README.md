Certainly! Here's a revised version of the README for the `EpicChainSmartContractKit`:

---

<p align="center">
  <img src="/.github/resources/images/logo.png" width="200px;">
</p>

<p align="center">
  <b>EpicChain Smart Contract Kit</b>
  <br/> A Python toolkit for developing smart contracts on the EpicChain blockchain.
</p>

<p align="center">  
  <a href="https://github.com/epicchainlabs/EpicChainSmartContractKit"><strong>EpicChainSmartContractKit</strong></a> · <a href="https://github.com/epicchainlabs/EpicChainSmartContractKit">EpicChainSmartContractKit</a>
</p>

<p align="center">
  <a href="https://circleci.com/gh/CityOfZion/epicchain-boa/tree/master">
    <img src="https://circleci.com/gh/CityOfZion/epicchain-boa.svg?style=shield" alt="CircleCI">
  </a>
  <a href="https://coveralls.io/github/CityOfZion/epicchain-boa?branch=master">
    <img src="https://coveralls.io/repos/github/CityOfZion/epicchain-boa/badge.svg?branch=master" alt="Coverage Status">
  </a>
  <a href="https://pypi.org/project/epicchain-boa/">
    <img src="https://img.shields.io/pypi/v/epicchain-boa.svg" alt="PyPI">
  </a>
  <a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2FCityOfZion%2Fepicchain-boa%2Fmaster%2Fpyproject.toml" alt="Python Version">
  </a>
  <a href="https://opensource.org/licenses/Apache-2.0">
    <img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License">
  </a>
</p>

<br/>

> **Note:** The latest release (v0.14.0) includes breaking changes for contracts written using previous versions. Please refer to our [migration guide](/docs/migration-guide-v0.14.0.md) to update your smart contracts.

## Overview

EpicChain Smart Contract Kit is a Python toolkit for creating smart contracts on the EpicChain blockchain. It compiles `.py` files to `.nef` and `.manifest.json` formats for usage and enabling the execution of contracts on the [EpicChain Blockchain](https://github.com/epicchainlabs/epicchain/).

The kit is part of the EpicChain Python Framework, designed to facilitate the development of decentralized applications (dApps) using Python exclusively.

## Quickstart

Installation requires Python 3.10 or later.

### Installation

#### Pip (Recommended)

Install EpicChain Smart Contract Kit using Pip:

```shell
$ pip install epicchain-boa
```

#### Build from Source (Optional)

If EpicChain Smart Contract Kit is not available via pip, you can run it from source.

1. Clone the repository:
   ```shell
   $ git clone https://github.com/epicchainlabs/EpicChainSmartContractKit.git
   ```
2. Install project dependencies:
   ```shell
   $ pip install wheel
   $ pip install -e .
   ```


## Reference Examples

Explore our extensive collection of examples:
- [Smart contract examples](/boa3_test/examples)
- [Features tests](/boa3_test/test_sc)

## EpicChain Python Suite Projects

- **[EpicChainSmartContractKit](https://github.com/epicchainlabs/EpicChainSmartContractKit)**: Python smart contracts compiler.
- [EpicChainSmartContractKit](https://github.com/epicchainlabs/EpicChainSmartContractKit): Python SDK for interacting with EpicChain.

## Contributing

Please refer to our [contributing guidelines](CONTRIBUTING.md) to learn how you can contribute to our project.

## License

The EpicChain Smart Contract Kit is open-source and licensed under the [Apache 2.0 License](https://github.com/epicchainlabs/EpicChainSmartContractKit/blob/master/LICENSE).
