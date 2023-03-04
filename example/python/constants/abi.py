HONEYPOT_CHECKER_ABI = [
    {
        "inputs": [],
        "stateMutability": "nonpayable",
        "type": "constructor",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "newOwner",
                "type": "address",
            },
        ],
        "name": "OwnershipTransferred",
        "type": "event",
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "dexRouter",
                "type": "address",
            },
            {
                "internalType": "address[]",
                "name": "path",
                "type": "address[]",
            },
        ],
        "name": "check",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "buyGas",
                        "type": "uint256",
                    },
                    {
                        "internalType": "uint256",
                        "name": "sellGas",
                        "type": "uint256",
                    },
                    {
                        "internalType": "uint256",
                        "name": "estimatedBuy",
                        "type": "uint256",
                    },
                    {
                        "internalType": "uint256",
                        "name": "exactBuy",
                        "type": "uint256",
                    },
                    {
                        "internalType": "uint256",
                        "name": "estimatedSell",
                        "type": "uint256",
                    },
                    {
                        "internalType": "uint256",
                        "name": "exactSell",
                        "type": "uint256",
                    },
                ],
                "internalType": "struct HoneypotChecker.CheckerResponse",
                "name": "",
                "type": "tuple",
            },
        ],
        "stateMutability": "payable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "destroy",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address",
            },
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newOwner",
                "type": "address",
            },
        ],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
]

SIMPLE_BEP20 = [
    {
        "inputs": [],
        "name": "symbol",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string",
            }
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "name",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string",
            }
        ],
        "stateMutability": "view",
        "type": "function",
    },
]
