from typing import TypedDict, Literal, List
from enum import Enum
import requests


class ChainDetails(TypedDict):
    chainId: str
    productRangeId: str
    chainPartNumber: str
    chainSize: str
    strandCount: int
    strandCofiguration: str
    pitch: str
    isIsoBreakingLoad: bool
    weight: str
    bearingArea: str


class DamageEvent(TypedDict):
    hours: int
    description: str
    type: int


class WorkingLifeDetails(TypedDict):
    workingLifeHours: str
    numberOfCycles: str
    minimumAcceptableWorkingLifeHours: int
    maximumDisplayableWorkingLifeHours: int
    damageEvents: List[DamageEvent]
    workingLifeHoursIsGreaterThanMaximumDisplayableWorkingLifeHours: bool


class CalculatedValues(TypedDict):
    inputPower: str
    inputSpeed: str
    chainLinearVelocity: str
    torque: str
    staticForce: str
    dynamicForce: str
    centrifugalForce: str
    totalForce: str
    bearingPressure: str
    breakingLoad: str
    length: str
    staticSafetyFactor: str
    dynamicSafetyFactor: str
    recommendedLubrication: str


class ApplicationDetails(TypedDict):
    numberOfLinks: str
    drivingSprocketTeeth: int
    drivingSprocketLoadingClassification: str
    drivingSprocketPitchDiameter: str
    drivenSprocketTeeth: int
    drivenSprocketLoadingClassification: str
    drivenSprocketPitchDiameter: str
    sprocketRatio: str
    environmentCondition: str
    environmentDomain: str
    lubricationRegime: str
    centreDistance: str
    numberOfLinksNotes: str
    centreDistanceNotes: str


class Units(TypedDict):
    inputPowerUnit: str
    inputSpeedUnit: str
    chainLinearVelocityUnit: str
    torqueUnit: str
    staticForceUnit: str
    dynamicForceUnit: str
    centrifugalForceUnit: str
    totalForceUnit: str
    normalisedTotalForceUnit: str
    bearingPressureUnit: str
    pitchUnit: str
    breakingLoadUnit: str
    fatigueLimitUnit: str
    bearingAreaUnit: str
    weightUnit: str
    lengthUnit: str
    centreDistanceUnit: str
    pitchDiameterUnit: str


class ChainOption(TypedDict):
    chainDetails: ChainDetails
    workingLifeDetails: WorkingLifeDetails
    calculatedValues: CalculatedValues
    extendedCalculatedValues: any
    applicationDetails: ApplicationDetails
    units: Units
    bearingPressureLimitCheckStatus: Literal["Ok"] | str
    linearChainVelocityLimitCheckStatus: Literal["Ok"] | str


class ChainOptionsResponse(TypedDict):
    status: (
        Literal[
            "ChainsAvailable",
            "NoChainsChainNotLongEnough",
            "NoChainsConditionsTooHarsh",
        ]
        | str
    )
    recommendations: List[ChainOption]


class ProductRange(Enum):
    SYNERGY = "ba1d2ddf-90b0-430e-9ac0-87a3a6c17f21"
    A_AND_S = "4bb164c1-57e1-48cb-91c9-21976be42686"
    RENOLD = "05162c4b-2e1d-42af-8d24-c015a8800564"
    RENOLD_HYDRO_SERVICE = "b6d55166-7bd8-448d-9444-e9d58c8cc6e2"
    RENOLD_SOVEREIGN = "e34a716a-07f7-48d6-af17-55e1561c314c"
    RENOLD_STAINLESS_STEEL = "4707b9e7-352d-4538-a2b7-540436912a04"
    RENOLD_SYNO_NICKEL_PLATED = "9f82d5b0-f760-4a2e-b7c8-0adbfc9b1e51"
    RENOLD_SYNO_POLYMER_BUSH = "496ae054-8404-438d-9fc0-4100774b1cfb"


class Standard(Enum):
    BRITISH = "b658ec94-ed00-452a-8d41-b2863a3677a1"
    AMERICAN = "3cfa4589-df43-4e26-9e28-84d8fb744d82"


class ChainCriteria(TypedDict):
    """
    The criteria needed by the chain selector.
    """

    power_value_type: Literal["InputPower", "WorkingLoad", "Torque"]
    power_value: int
    speed_value_type: Literal["InputSpeed", "ChainLinearVelocity"]
    speed_value: int
    start_speed: int
    finish_speed: int
    speed_increment: int
    target_working_life: int
    working_life_tolerance: int
    driving_sprocket_teeth: int
    driven_sprocket_teeth: int
    centre_distance_rounding_mode: Literal[
        "EvenNumberOfLinks", "OddNumberOfLinks", "FixedValue", "None"
    ]
    centre_distance: int
    number_of_links: int
    user_supplied_number_of_links: bool
    driving_machine_characteristics: Literal[
        "SmoothingRunning", "SlightShocks", "ModerateShocks"
    ]
    driven_machine_characteristics: Literal[
        "SligthShocks", "ModerateShocks", "HeavyShocks"
    ]
    lubrication_regime: Literal[
        "DryRunning",
        "Insufficient",
        "Recommended",
        "MaintenanceFreeLubrication",
        "RegularRelubrication",
        "BetterThanRecommended",
    ]
    environment_condition: Literal["Normal", "Abrasive"]
    environment_domain: Literal["Indoor", "Outdoor"]
    product_range_id: ProductRange
    chain_standard_id: Standard
    unit: Literal["Metric", "Imperial"]


def get_chain_options(chain_options: ChainCriteria):

    url = "https://www.renoldchainselector.com/ChainSelector/FindRecommendations?"
    url_params = dict()
    for key, val in chain_options.items():
        if isinstance(val, Enum):
            url_params[to_lower_camel_case(key)] = val.value
        else:
            url_params[to_lower_camel_case(key)] = val
    url_params["chainSelectionMode"] = "Automatic"
    url_params["customMinimumAcceptableWorkingLifeHours"] = "0"
    url_params["customFatigueLimitCorrectionFactor"] = "0"
    url_params["customFatigueLimit"] = "0"
    url_params["customBreakingLoad"] = "0"
    url_params["customWearFactor"] = "0"
    url_params["noCache"] = "0"
    url_params["outputMode"] = "Json"
    url_params["manualChainSelectionSize"] = ""
    url_params["manualChainSelectionStrandCount"] = "NaN"

    return requests.get(
        url=url, params=url_params, headers={"User-Agent": "Mozilla/5.0"}
    )


def to_camel_case(snake_str):
    return "".join(x.capitalize() for x in snake_str.lower().split("_"))


def to_lower_camel_case(snake_str):
    camel_str = to_camel_case(snake_str)
    return snake_str[0].lower() + camel_str[1:]
