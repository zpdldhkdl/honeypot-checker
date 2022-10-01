const { honeypotCheckerAbi } = require("./ABI");

module.exports = class HoneypotCheckerCaller {
  constructor(web3, checkerContract) {
    this.web3 = web3;

    /**
     * always use
     * 4000000 GAS LIMIT,
     * 10 gwei gasPrice,
     * 1 BNB Value
     * for simulation
     */
    this.gasLimit = 4000000;
    this.gasPrice = this.web3.utils.toWei("10", "gwei");
    this.value = this.web3.utils.toWei("1");

    this.honeypotCheckerContract = new web3.eth.Contract(
      honeypotCheckerAbi,
      checkerContract
    );
  }

  async check(routerAddress, path) {
    const result = await this.honeypotCheckerContract.methods
      .check(routerAddress, path)
      .call({
        value: this.value,
        gasLimit: this.gasLimit,
        gasPrice: this.gasPrice,
      });

    return result;
  }

  calculateTaxFee(estimatedPrice, exactPrice) {
    return (((estimatedPrice - exactPrice) / estimatedPrice) * 100).toFixed(1);
  }
};
