# HONEYPOT-CHECKER-CONTRACT-CALLER-EXAMPLE

![img](https://user-images.githubusercontent.com/49149450/193416379-b1e9d249-f041-4f81-b64a-aa3c057c2394.png)

- if the token is a `honeypot` or `the liquidity pool for the pair does not exist`, an exception is raised in the main function.

- if the base token is not WBNB, it is displayed through the swap process of `wbnb` -> `base token` -> `target` token.

- since correct results can be obtained only when the LP pool exists, logic to check the existence of the lp pool is required in actual use.

## BSC MAINNET

`npm run start:mainnet`

## BSC TESTNET

- need to modify `HONEYPOT_CHECKER_ADDRESS` of constants before use.

`npm run start:testnet`
