import json
import logging
import hashlib
import sys
from pydantic import ValidationError

from secure_config_checker.config_schema import PipelineConfig 
# import the schema from same package


def compute_hash(file_path: str) -> str:
    """ 
    Compute a SHA-256 hash of the given file.
    
    This is used to detect tampering or unexpected changes to the config
    """
    sha256 = hashlib.sha256()
    
    # Open in binary mode and read in chunks (good practice for large files)
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()
  

def load_and_validate_config(path: str) -> PipelineConfig:
    """
    Load a JSON config file, validate it against PipelineConfig,
    and log the SHA-256 hash.
    
    Returns a validated PipelineConfig object on success.
    Exits with code 1 on validation failure.
    """
    logging.info(f"Loading config file from: {path}")
    
    with open(path, "r") as f:
        raw_data = json.load(f)
        
    logging.info("Raw config loaded, validating schema...")
    
    try:
        config = PipelineConfig(**raw_data)
        logging.info("Config validation SUCCESS")
        
        # Security Policy Enforcement
        if not config.enable_encryption:
            raise ValueError(
                "Security Policy Violation: 'enable_encryption' must be True."
                "(HIPPA / HITRUST baseline requirement)"
            )
        
        # Compute and log SHA-256 hash
        file_hash = compute_hash(path)
        logging.info(f"SHA-256 hash of config file: {file_hash}")
        
        return config
      
    except (ValidationError, ValueError) as e:
        logging.error("Config validation FAILED!!!")
        print(str(e))
        sys.exit(1)
  