# Blockies

An ERC-721 token sample contract for testnets.

If you are looking for an ERC-20 token instead, check out [Buckie](https://buckie.tk/).

### Contracts

The ABI [JSON](Blockies.json) includes a faucet method. You can find and interact with the smart contract using Etherscan.

| Network | Contract Address                                                                                                              |
| ------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Ropsten | [0xE0394f4404182F537AC9F2F9695a4a4CD74a1ea3](https://ropsten.etherscan.io/address/0xE0394f4404182F537AC9F2F9695a4a4CD74a1ea3) |
| Rinkeby | [0xE0394f4404182F537AC9F2F9695a4a4CD74a1ea3](https://rinkeby.etherscan.io/address/0xE0394f4404182F537AC9F2F9695a4a4CD74a1ea3) |
| Kovan   | [0xE0394f4404182F537AC9F2F9695a4a4CD74a1ea3](https://kovan.etherscan.io/address/0xE0394f4404182F537AC9F2F9695a4a4CD74a1ea3)   |
| Goerli  | [0xE0394f4404182F537AC9F2F9695a4a4CD74a1ea3](https://goerli.etherscan.io/address/0xE0394f4404182F537AC9F2F9695a4a4CD74a1ea3)  |

### Source Code

Blockies was written using the (OpenZeppelin)[https://openzeppelin.com/] library.

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
