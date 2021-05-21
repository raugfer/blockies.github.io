# Blockies

An ERC-721 token sample contract for testnets.

If you are looking for an ERC-20 token instead, check out [Buckie](https://buckie.tk/).

### Contracts

The ABI [JSON](Blockies.json) includes a faucet method. You can interact with the smart contract using Etherscan and a [Web3](https://web3js.readthedocs.io/) compatible wallet.

Ethereum:

| Network (ID)      | Contract Address                                                                                                                        |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| ropsten (3)       | [0x46bEF163D6C470a4774f9585F3500Ae3b642e751](https://ropsten.etherscan.io/address/0x46bEF163D6C470a4774f9585F3500Ae3b642e751)           |
| rinkeby (4)       | [0x46bEF163D6C470a4774f9585F3500Ae3b642e751](https://rinkeby.etherscan.io/address/0x46bEF163D6C470a4774f9585F3500Ae3b642e751)           |
| kovan (42)        | [0x46bEF163D6C470a4774f9585F3500Ae3b642e751](https://kovan.etherscan.io/address/0x46bEF163D6C470a4774f9585F3500Ae3b642e751)             |
| goerli (5)        | [0x46bEF163D6C470a4774f9585F3500Ae3b642e751](https://goerli.etherscan.io/address/0x46bEF163D6C470a4774f9585F3500Ae3b642e751)            |

Binance Smart Chain:

| Network (ID)      | Contract Address                                                                                                                        |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| bsctest (97)      | [0x46bEF163D6C470a4774f9585F3500Ae3b642e751](https://testnet.bscscan.com/address/0x46bEF163D6C470a4774f9585F3500Ae3b642e751)            |

Fantom Network:

| Network (ID)      | Contract Address                                                                                                                        |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| ftmtest (4002)    | [0x46bEF163D6C470a4774f9585F3500Ae3b642e751](https://testnet.ftmscan.com/address/0x46bEF163D6C470a4774f9585F3500Ae3b642e751)            |

Polygon Matic:

| Network (ID)      | Contract Address                                                                                                                        |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| matictest (80001) | [0x46bEF163D6C470a4774f9585F3500Ae3b642e751](https://explorer-mumbai.maticvigil.com/address/0x46bEF163D6C470a4774f9585F3500Ae3b642e751) |

### Source Code

Blockies was written using the [OpenZeppelin](https://openzeppelin.com/) library.

```solidity
// Blockies
// SPDX-License-Identifier: GPL-3.0-only
pragma solidity ^0.6.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract Blockies is ERC721
{
	constructor () ERC721("Blockies", "KIE") public
	{
		_setBaseURI("https://blockies.tk/");
	}

	function faucet() public
	{
		address _target = msg.sender;
		uint256 _tokenId = totalSupply() + 1;
		_safeMint(_target, _tokenId);
	}
}
```

### Credits

Blockies metadata images are provided by [Lorem Picsum](https://picsum.photos/) and textual descriptions are generated from [Bacon Ipsum](https://baconipsum.com/).

### Support

If you would like to support this page download [Brave Browser](https://brave.com/blo536). Your BAT contributions are welcome!
