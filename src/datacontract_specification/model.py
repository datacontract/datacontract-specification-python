import importlib.resources as impresources
import os
from typing import Any, Dict, List

import pydantic as pyd
import yaml

DATACONTRACT_TYPES = [
    "string",
    "text",
    "varchar",
    "number",
    "decimal",
    "numeric",
    "int",
    "integer",
    "long",
    "bigint",
    "float",
    "double",
    "boolean",
    "timestamp",
    "timestamp_tz",
    "timestamp_ntz",
    "date",
    "time",
    "array",
    "map",
    "object",
    "record",
    "struct",
    "bytes",
    "variant",
    "json",
    "null",
]


class Contact(pyd.BaseModel):
    name: str | None = None
    url: str | None = None
    email: str | None = None

    model_config = pyd.ConfigDict(
        extra="allow",
    )


class Policy(pyd.BaseModel):
    type: str | None = None
    description: str | None = None
    url: str | None = None

    model_config = pyd.ConfigDict(
        extra="allow",
    )


class Transformation(pyd.BaseModel):
    type: str | None = None
    subtype: str | None = None
    description: str | None = None
    masking: bool | None = None

    model_config = pyd.ConfigDict(
        extra="allow",
    )


class InputField(pyd.BaseModel):
    namespace: str | None = None
    name: str | None = None
    field: str | None = None
    transformations: List[Transformation] | None = None

    model_config = pyd.ConfigDict(
        extra="allow",
    )


class Lineage(pyd.BaseModel):
    inputFields: List[InputField] | None = None
    transformationDescription: str | None = None
    transformationType: str | None = None

    model_config = pyd.ConfigDict(
        extra="allow",
    )


class ServerRole(pyd.BaseModel):
    name: str | None = None
    description: str | None = None
    model_config = pyd.ConfigDict(
        extra="allow",
    )


class Server(pyd.BaseModel):
    type: str | None = None
    description: str | None = None
    environment: str | None = None
    format: str | None = None
    project: str | None = None
    dataset: str | None = None
    path: str | None = None
    delimiter: str | None = None
    endpointUrl: str | None = None
    location: str | None = None
    account: str | None = None
    database: str | None = None
    schema_: str | None = pyd.Field(default=None, alias="schema")
    host: str | None = None
    port: int | None = None
    catalog: str | None = None
    topic: str | None = None
    http_path: str | None = None  # Use ENV variable
    token: str | None = None  # Use ENV variable
    dataProductId: str | None = None
    outputPortId: str | None = None
    driver: str | None = None
    storageAccount: str | None = None
    roles: List[ServerRole] = None

    model_config = pyd.ConfigDict(
        extra="allow",
    )


class Terms(pyd.BaseModel):
    usage: str | None = None
    limitations: str | None = None
    policies: List[Policy] | None = None
    billing: str | None = None
    noticePeriod: str | None = None
    description: str | None = None

    model_config = pyd.ConfigDict(
        extra="allow",
    )


class Definition(pyd.BaseModel):
    domain: str | None = None
    name: str | None = None
    title: str | None = None
    description: str | None = None
    type: str | None = None
    enum: List[str] = []
    format: str | None = None
    minLength: int | None = None
    maxLength: int | None = None
    pattern: str | None = None
    minimum: int | None = None
    exclusiveMinimum: int | None = None
    maximum: int | None = None
    exclusiveMaximum: int | None = None
    pii: bool | None = None
    classification: str | None = None
    fields: Dict[str, "Field"] = {}
    items: "Field" = None
    tags: List[str] = []
    links: Dict[str, str] = {}
    example: str | None = None
    examples: List[Any] | None = None

    model_config = pyd.ConfigDict(
        extra="allow",
    )


class Quality(pyd.BaseModel):
    type: str | None = None
    description: str | None = None
    metric: str | None = None
    arguments: Dict[str, Any] | None = None
    query: str | None = None
    dialect: str | None = None
    mustBe: float | int | None = None
    mustNotBe: float | int | None = None
    mustBeGreaterThan: float | int | None = None
    mustBeGreaterThanOrEqualTo: float | int | None = pyd.Field(
        default=None,
        deprecated="Removed in Data Contract Specification v1.2.0. Use mustBeGreaterOrEqualTo instead.",
    )
    mustBeGreaterOrEqualTo: float | int | None = None
    mustBeLessThan: float | int | None = None
    mustBeLessOrEqualTo: float | int | None = None
    mustBeGreaterThanOrEqualTo: float | int | None = pyd.Field(
        default=None,
        deprecated="Removed in Data Contract Specification v1.2.1. Use mustBeLessOrEqualTo instead.",
    )
    mustBeBetween: List[float | int] = None
    mustNotBeBetween: List[float | int] = None
    engine: str | None = None
    implementation: str | Dict[str, Any] | None = None

    model_config = pyd.ConfigDict(
        extra="allow",
    )


class Field(pyd.BaseModel):
    ref: str = pyd.Field(default=None, alias="$ref")
    title: str | None = None
    type: str | None = None
    format: str | None = None
    required: bool | None = None
    primary: bool = pyd.Field(
        default=None,
        deprecated="Removed in Data Contract Specification v1.1.0. Use primaryKey instead.",
    )
    primaryKey: bool | None = None
    unique: bool | None = None
    references: str | None = None
    description: str | None = None
    pii: bool | None = None
    classification: str | None = None
    pattern: str | None = None
    minLength: int | None = None
    maxLength: int | None = None
    minimum: float | int | None = None
    exclusiveMinimum: float | int | None = None
    maximum: float | int | None = None
    exclusiveMaximum: float | int | None = None
    enum: List[str] | None = []
    tags: List[str] | None = []
    links: Dict[str, str] = {}
    fields: Dict[str, "Field"] = {}
    items: "Field" = None
    keys: "Field" = None
    values: "Field" = None
    precision: int | None = None
    scale: int | None = None
    example: Any | None = pyd.Field(
        default=None,
        deprecated="Removed in Data Contract Specification v1.1.0. Use examples instead.",
    )
    examples: List[Any] | None = None
    quality: List[Quality] | None = []
    lineage: Lineage | None = None
    config: Dict[str, Any] | None = None

    model_config = pyd.ConfigDict(
        extra="allow",
    )


class Model(pyd.BaseModel):
    description: str | None = None
    type: str | None = None
    namespace: str | None = None
    title: str | None = None
    fields: Dict[str, Field] = {}
    quality: List[Quality] | None = []
    primaryKey: List[str] | None = []
    examples: List[Any] | None = None
    additionalFields: bool | None = None
    config: Dict[str, Any] = None
    tags: List[str] | None = None

    model_config = pyd.ConfigDict(
        extra="allow",
    )


class Info(pyd.BaseModel):
    title: str | None = None
    version: str | None = None
    status: str | None = None
    description: str | None = None
    owner: str | None = None
    contact: Contact | None = None

    model_config = pyd.ConfigDict(
        extra="allow",
    )


class Example(pyd.BaseModel):
    type: str | None = None
    description: str | None = None
    model: str | None = None
    data: str | object = None


# Deprecated Quality class
class DeprecatedQuality(pyd.BaseModel):
    type: str | None = None
    specification: str | object = None


class Availability(pyd.BaseModel):
    description: str | None = None
    percentage: str | None = None


class Retention(pyd.BaseModel):
    description: str | None = None
    period: str | None = None
    unlimited: bool | None = None
    timestampField: str | None = None


class Latency(pyd.BaseModel):
    description: str | None = None
    threshold: str | None = None
    sourceTimestampField: str | None = None
    processedTimestampField: str | None = None


class Freshness(pyd.BaseModel):
    description: str | None = None
    threshold: str | None = None
    timestampField: str | None = None


class Frequency(pyd.BaseModel):
    description: str | None = None
    type: str | None = None
    interval: str | None = None
    cron: str | None = None


class Support(pyd.BaseModel):
    description: str | None = None
    time: str | None = None
    responseTime: str | None = None


class Backup(pyd.BaseModel):
    description: str | None = None
    interval: str | None = None
    cron: str | None = None
    recoveryTime: str | None = None
    recoveryPoint: str | None = None


class ServiceLevel(pyd.BaseModel):
    availability: Availability | None = None
    retention: Retention | None = None
    latency: Latency | None = None
    freshness: Freshness | None = None
    frequency: Frequency | None = None
    support: Support | None = None
    backup: Backup | None = None


class DataContractSpecification(pyd.BaseModel):
    dataContractSpecification: str | None = None
    id: str | None = None
    info: Info | None = None
    servers: Dict[str, Server] = {}
    terms: Terms | None = None
    models: Dict[str, Model] = {}
    definitions: Dict[str, Definition] = {}
    examples: List[Example] = pyd.Field(
        default_factory=list,
        deprecated="Removed in Data Contract Specification " "v1.1.0. Use models.examples instead.",
    )
    quality: DeprecatedQuality | None = pyd.Field(
        default=None,
        deprecated="Removed in Data Contract Specification v1.1.0. Use " "model-level and field-level quality instead.",
    )
    servicelevels: ServiceLevel | None = None
    links: Dict[str, str] = {}
    tags: List[str] = []

    def to_yaml(self) -> str:
        return yaml.dump(
            self.model_dump(exclude_defaults=True, exclude_none=True,
                            by_alias=True),
            sort_keys=False,
            allow_unicode=True,
        )

    @classmethod
    def from_file(cls, file_path: str) -> "DataContractSpecification":
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")
        with open(file_path, "r", encoding="utf-8") as file:
            file_content = file.read()
        return cls.from_string(file_content)

    @classmethod
    def from_string(cls, data_contract_str: str) -> "DataContractSpecification":
        data = yaml.safe_load(data_contract_str)
        return cls(**data)

    @classmethod
    def json_schema(cls):
        package_name = __package__
        json_schema = "schema.json"
        with impresources.open_text(package_name,
                                    json_schema) as file:
            return file.read()
