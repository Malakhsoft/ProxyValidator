# Proxy Validator

This Python script validates a list of proxy servers from a CSV file (`Free_Proxy_List.csv`). It checks each proxy's connectivity and determines whether it is valid or not. Valid proxies are printed to the console, and the user has the option to save them to a new CSV file (`MalakhProxy.csv`).

## Usage

1. Place your list of proxy servers in a CSV file named `Free_Proxy_List.csv` in the same directory as the script.

2. Run the `Proxy.py` script.

3. The script will clear the console, load the proxies, and start validating them. Progress will be shown using a progress bar.

4. Once validation is complete, valid proxies will be displayed in the console.

5. You will be prompted to save the valid proxies to a new CSV file named `MalakhProxy.csv`. Respond with "yes" or "no" accordingly.

## Requirements

- Python 3.x
- `tqdm` library (for progress bar visualization)

## File Structure

- `Proxy.py`: The main Python script for proxy validation.
- `Free_Proxy_List.csv`: Input CSV file containing the list of proxy servers.
- `MalakhProxy.csv`: Output CSV file to save the valid proxies.
- `README.md`: This README file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
