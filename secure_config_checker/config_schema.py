from pydantic import BaseModel, Field, field_validator


class PipelineConfig(BaseModel):
    """
    Schema for our ML pipeline configuration
    """
  
    project_name: str = Field(..., min_length=3)
    author: str
    version: str
    model_type: str
    training_data_path: str
    output_dir: str
  
    # REQUIRED: must be present and must be True
    enable_encryption: bool = Field(...)
  
    @field_validator("enable_encryption")
    def encryption_must_be_true(cls, value: bool) -> bool:
        if value is not True:
            raise ValueError("enable_encryption MUST be set to true.")
        return value
    