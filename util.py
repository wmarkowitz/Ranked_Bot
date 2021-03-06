from decimal import Decimal as D

PLAYER_DATA_COLLECTION = "player_data"
CONFIG_COLLECTION = "config"
PENDING_RESULTS_COLLECTION = "pending_results"

ID_KEY = "_id"
POINTS_KEY = "points"

TIERS_KEY = "tiers"
DEFAULT_TIERS = {}

POINTS_GAINED_FORMULA_KEY = "points_gained_formula"
DEFAULT_POINTS_GAINED_FORMULA = "50 + ( -1 * POINT_DIFFERENCE / 8 )"

MIN_POINTS_GAINED_KEY = "min_points_gained"
DEFAULT_MIN_POINTS_GAINED = 1

MAX_POINTS_GAINED_KEY = "max_points_gained"
DEFAULT_MAX_POINTS_GAINED = 100

POINTS_LOST_FORMULA_KEY = "points_lost_formula"
DEFAULT_POINTS_LOST_FORMULA = "50 + ( -1 * POINT_DIFFERENCE / 8 )"

MIN_POINTS_LOST_KEY = "min_points_lost"
DEFAULT_MIN_POINTS_LOST = 1

MAX_POINTS_LOST_KEY = "max_points_lost"
DEFAULT_MAX_POINTS_LOST = 100

COMMAND_PREFIX_KEY = "command_prefix"
DEFAULT_COMMAND_PREFIX = "!"

WINNER_ID_KEY = "winner_id"
WINNER_CONFIRMED_KEY = "winner_confirmed"
LOSER_ID_KEY = "loser_id"
LOSER_CONFIRMED_KEY = "loser_confirmed"

NO_TIER_ROLE_INDEX = -1

INITIAL_CONFIG_FILE = {
    COMMAND_PREFIX_KEY: DEFAULT_COMMAND_PREFIX,
    TIERS_KEY: DEFAULT_TIERS,
    POINTS_GAINED_FORMULA_KEY: DEFAULT_POINTS_GAINED_FORMULA,
    POINTS_LOST_FORMULA_KEY: DEFAULT_POINTS_LOST_FORMULA,
    MIN_POINTS_GAINED_KEY: DEFAULT_MIN_POINTS_GAINED,
    MAX_POINTS_GAINED_KEY: DEFAULT_MAX_POINTS_GAINED,
    MIN_POINTS_LOST_KEY: DEFAULT_MIN_POINTS_LOST,
    MAX_POINTS_LOST_KEY: DEFAULT_MAX_POINTS_LOST,
}


def getIDFromMention(mention):
    userId = ""
    for char in mention:
        if char.isdigit():
            userId += char
    return userId


def userHasAdminRole(user):
    return user.guild_permissions.administrator
