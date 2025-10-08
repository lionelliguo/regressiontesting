# RegressionTesting
# Copyright (c) 2025 Lionel Guo
# Author: Lionel Guo
# Email: lionelliguo@gmail.com
# GitHub: https://github.com/lionelliguo/regressiontesting

from regressiontesting import RegressionTesting
import json

def load_settings():
    """Load settings from a JSON file."""
    try:
        with open('settings.json', 'r') as f:
            settings = json.load(f)
        return settings
    except Exception as e:
        print(f"Error loading settings: {e}")
        return {}

if __name__ == "__main__":
    settings = load_settings()

    regression_test = RegressionTesting(
        spreadsheet_url=settings.get("SPREADSHEET_URL", ""),
        service_account_file=settings.get("SERVICE_ACCOUNT_FILE", ""),
        sleep_seconds=settings.get("SLEEP_SECONDS", 1.0),
        ignore_case=settings.get("IGNORE_CASE", True),
        output_batch_size=settings.get("OUTPUT_BATCH_SIZE", 0),
        copy_batch_size=settings.get("COPY_BATCH_SIZE", 0)
    )
    
    selection_rule_1, selection_rule_2, comparison_rule = regression_test.load_config_rules()

    new_sheet = regression_test.create_new_sheet_with_current_datetime()
    
    if new_sheet is not None:
        regression_test.process_sheet(new_sheet, selection_rule_1, selection_rule_2, comparison_rule)
        print("All rows processed.")
    else:
        print("Sheet creation failed. Exiting.")
