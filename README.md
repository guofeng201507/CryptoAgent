[![Multi-Modality](agorabanner.png)](https://discord.com/servers/agora-999382051935506503)

# CryptoAgent: Real-Time Cryptocurrency Data Analysis Agent

[![Join our Discord](https://img.shields.io/badge/Discord-Join%20our%20server-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/agora-999382051935506503) [![Subscribe on YouTube](https://img.shields.io/badge/YouTube-Subscribe-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@kyegomez3242) [![Connect on LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kye-g-38759a207/) [![Follow on X.com](https://img.shields.io/badge/X.com-Follow-1DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://x.com/kyegomezb)


CryptoAgent is a professional, enterprise-grade solution designed to fetch, analyze, and summarize real-time cryptocurrency data. It integrates with CoinGecko's API to retrieve the latest crypto metrics and leverages OpenAI's advanced language model to generate insightful, concise reports tailored for crypto investors and financial analysts.

## Key Features

- **Real-Time Data Fetching**: Retrieves live cryptocurrency data, including current price, market capitalization, trading volume, supply details, and recent price changes.
- **Advanced Analysis**: Summarizes complex crypto data into clear, actionable insights, allowing users to stay informed on key market trends.
- **Enterprise-Grade Reliability**: Built with robust error handling, retries, and logging to ensure uninterrupted data retrieval and analysis.
- **Customizable Reports**: Designed to provide tailored insights based on user requirements, making it suitable for investors, traders, and analysts.

## Use Cases

- **Market Monitoring**: Track real-time prices and key metrics for any cryptocurrency.
- **Investment Research**: Generate comprehensive reports on specific coins, including trends, market sentiment, and price changes.
- **Financial Analysis**: Use CryptoAgent to analyze large volumes of crypto data, summarize trends, and provide strategic insights.

## Installation

    ```

## Components Overview

### 1. **CryptoTool**
`CryptoTool` integrates with CoinGecko's API to fetch real-time cryptocurrency data. It provides detailed information such as:

- Current price
- Market capitalization
- 24-hour trading volume
- Circulating and total supply
- Price changes over 24 hours

Example of fetching data for a cryptocurrency:

```python
crypto_tool = CryptoTool()
crypto_data = crypto_tool.get_crypto_data("bitcoin")
```

### 2. **CryptoAnalysisAgent**
`CryptoAnalysisAgent` is the core component that combines data fetching with advanced analysis. It generates custom prompts for OpenAI's GPT-4 model, enabling deeper insights into the fetched data.

Example of running the agent:

```python
agent = CryptoAnalysisAgent(
    agent_name="Crypto-Analysis-Agent",
    system_prompt=CRYPTO_AGENT_SYS_PROMPT,
    llm=model
)

# Fetch and analyze Bitcoin data
response = agent.run("Analyze the recent price changes and trends of Bitcoin.", "bitcoin")
print(response)
```

### 3. **Loguru for Logging**
The `loguru` library is integrated for real-time logging, making it easy to trace operations, handle errors, and ensure transparency in the data pipeline.

Example of error handling:

```python
try:
    response = requests.get(self.api_url, params=params)
    response.raise_for_status()
except requests.RequestException as e:
    logger.error(f"Error fetching crypto data: {e}")
```

## System Architecture

CryptoAgent follows a modular architecture:

- **CryptoTool** handles all interactions with the CoinGecko API.
- **CryptoAnalysisAgent** performs the crypto analysis by combining data fetched from the API with OpenAI's powerful language models.
- **Agent Framework**: The agent architecture, powered by `swarms`, ensures flexibility, scalability, and reliability for enterprise deployments.

## Enterprise-Grade Features

- **Scalability**: Easily integrates into larger infrastructures for monitoring hundreds of cryptocurrencies simultaneously.
- **Error Handling and Retries**: Built-in mechanisms for handling API failures and retrying failed requests ensure uninterrupted service.
- **Customization**: Modify the system prompt to tailor the analysis to specific use cases, whether it’s for a hedge fund, a financial institution, or individual investors.
- **Security**: Sensitive API keys and environment variables are securely managed via `.env` and best practices for API management.

## Getting Started

1. **Prerequisites**: Ensure you have Python 3.8+ installed.
2. **API Access**: You’ll need an OpenAI API key to interact with the model.
3. **Run the Agent**: Follow the instructions in the [Installation](#installation) section to set up and run CryptoAgent.

## Sample Output

```text
Coin: Bitcoin (BTC)
Current Price: $45,320.12
Market Cap: $853,000,000,000
24h Trading Volume: $32,000,000,000
Circulating Supply: 18,700,000 BTC
Total Supply: N/A
Price Change (24h): +4.2%

Analysis: Bitcoin has seen a significant price increase of 4.2% over the past 24 hours, driven by increased trading volume. The market cap remains strong, reflecting continued investor confidence.
```

## Future Enhancements

- **Multi-Coin Analysis**: Enable simultaneous analysis of multiple cryptocurrencies for portfolio managers.
- **Sentiment Analysis**: Incorporate social media and news sentiment analysis into the crypto reports.
- **Predictive Analytics**: Add a layer of predictive insights using historical data to forecast market trends.
  
## Contributing

We welcome contributions from the community! Please follow our [contribution guidelines](CONTRIBUTING.md) and submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For enterprise inquiries, custom deployments, or support, please contact [support@cryptoagent.io](mailto:support@cryptoagent.io).
