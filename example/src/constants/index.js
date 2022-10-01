const testnetConfig = {
  RPC: "https://data-seed-prebsc-1-s1.binance.org:8545/",
  PANCAKE_SWAP_ROUTER_ADDRESS: "0x9Ac64Cc6e4415144C455BD8E4837Fea55603e5c3",
  WBNB_ADDRESS: "0xae13d989daC2f0dEbFf460aC112a837C89BAa7cd",
  HONEYPOT_CHECKER_ADDRESS: "", // deploy your self
};

const mainnetConfig = {
  RPC: "https://bsc-dataseed.binance.org/",
  PANCAKE_SWAP_ROUTER_ADDRESS: "0x10ED43C718714eb63d5aA57B78B54704E256024E",
  WBNB_ADDRESS: "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c",
  HONEYPOT_CHECKER_ADDRESS: "0x18E1D9d91D4ad5D05eCE0122257A5F88FE8E3e33",
};

module.exports = (ENV) => {
  return ENV === "MAINNET" ? mainnetConfig : testnetConfig;
};
