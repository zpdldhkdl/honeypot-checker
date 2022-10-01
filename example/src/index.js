const Web3 = require("web3");
require("dotenv").config();

const {
  RPC,
  PANCAKE_SWAP_ROUTER_ADDRESS,
  WBNB_ADDRESS,
  HONEYPOT_CHECKER_ADDRESS,
} = require("./constants")(process.env.ENV);

const { bep20Abi } = require("./ABI");

const HoneypotCheckerCaller = require("./HoneypotCheckerCaller");

const web3 = new Web3(RPC);

web3.eth.accounts.wallet.add(process.env.PRIVATE_KEY);

const main = async () => {
  try {
    const honeypotCheckerCaller = new HoneypotCheckerCaller(
        web3,
        HONEYPOT_CHECKER_ADDRESS
      ),
      baseTokenAddress = WBNB_ADDRESS,
      targetTokenAddress = "TARGET_TOKEN_ADDRESS";

    const {
      buyGas,
      sellGas,
      estimatedBuy,
      exactBuy,
      estimatedSell,
      exactSell,
    } = await honeypotCheckerCaller.check(PANCAKE_SWAP_ROUTER_ADDRESS, [
      baseTokenAddress,
      targetTokenAddress,
    ]);

    const [buyTax, sellTax] = [
      honeypotCheckerCaller.calculateTaxFee(estimatedBuy, exactBuy),
      honeypotCheckerCaller.calculateTaxFee(estimatedSell, exactSell),
    ];

    /**
     * get symbol & token name
     */
    const targetTokenContract = new web3.eth.Contract(
      bep20Abi,
      targetTokenAddress
    );

    const tokenSymbol = await targetTokenContract.methods.symbol().call(),
      tokenName = await targetTokenContract.methods.name().call();

    console.log(`
  ===============================================
                name: ${tokenName}
              symbol: ${tokenSymbol}
    used gas for buy: ${buyGas}
            for sell: ${sellGas}
         buy tax fee: ${buyTax} %
        sell tax fee: ${sellTax} %
  ===============================================
    `);
  } catch (e) {
    console.log(e);
    console.log(`
    honeypot or lp doesn't exist
    `);
  }
};

main();
