# Warp Cloner

Simple Python script that can clone [Warp Plus](https://1.1.1.1/) keys.

With this script you will be able to clone 12 PB keys in large amounts.

## Installation

1. Clone this repository
2. Install [Python 3.11](https://www.python.org/downloads/) or higher
3. Install dependencies using `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and fill variables (see next section)
5. Launch script using `python -u src/main.py`
6. Wait for results in console.

## Configuration

- `BASE_KEYS` (not required) - keys to clone divided by comma, if none then default keys will be used (script may not work with default keys)
- `THREADS_COUNT` (default: 1) - amount of threads.
- `PROXY_URL` (not required) - proxy urls divided by comma, if none then script will be launched in proxyless mode.
- `DELAY` (default: 25) - seconds to sleep after key clone

## Notes

Script doesn't output any kind of errors (including rate limit errors or proxy errors) for better readability of output.

You can use ipv6 proxy as far as ipv4 proxy if they don't block Warp API endpoint.

## Contributing

I will support this project as far as I can, but issues and pull requests are always welcome!

## License

This project licensed under MIT License.

## Support me

You can support my further developments or support this project by buying me a coffee or pizza.

[![Buy Me A Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/totoroterror)