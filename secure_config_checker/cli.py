import argparse
import logging
from .loader import load_and_validate_config


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"      
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate an ML pipeline configuration file."
    )
    
    parser.add_argument(
        "--config",
        required=True,
        help="Path to the pipeline configuration JSON file."
    )
    
    return parser.parse_args()
  
  
def main() -> None:
    """
    Entry point for the secure_config_checker CLI.
    """
    args = parse_args()

    try:
        config = load_and_validate_config(args.config)
        print("SECURITY POLICY PASSED: Pipeline config is compliant.")
        # Optional: print(config) for debugging, but usually remove in CI
        # print(config)
        import sys
        sys.exit(0)

    except Exception as e:
        print("SECURITY POLICY FAILED: Pipeline config is NOT compliant!")
        print(f"Reason: {e}")
        import sys
        sys.exit(1)