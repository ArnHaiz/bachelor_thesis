# List of preprint servers
PRE_PRINT_SERVERS = ["https://api.biorxiv.org/details/biorxiv", "https://api.medrxiv.org/details/medrxiv", "https://export.arxiv.org/api/"]
unusable_licenses = [] # TODO complete this list

# Start dates are decided to have a comparison of the situation not too long before the changes. Determined subjectively
STANDARD_START_DATE = '2021-01-01'
BIORXIV_START_DATE = "2021-01-01"

MEDRXIV_START_DATE = "2021-01-01"

ARXIV_OAI_URL = "https://oaipmh.arxiv.org/oai?"
ARXIV_START_DATE = "2021-01-01"
arxiv_namespace = {'ns': 'http://www.openarchives.org/OAI/2.0/'}


# List of banned words slightly modified from the original, word combos separated by '+' or 'and' have been removed for
# ease of use. This can be changed later if time and availability are in stock.
#
# This decision is my temporary answer to the problem of detecting when these words are considered to be used
# "together". Some ideas of how to circumvent this might be to make a dictionary (or a set of strings and arrays
# if possible) instead of an array where the val is an array with the words that go together and check if in the same
# sentence the two are used. I do not know if this would be a complete solution or not.
BANNED_LIST = ["accessible", "activism", "activists", "advocacy", "advocate", "advocates", "affirming care",
                   "all-inclusive", "allyship", "anti-racism", "antiracist", "assigned at birth",
                   "assigned female at birth", "assigned male at birth", "at risk", "barrier", "barriers", "belong",
                   "bias", "biased", "biased toward", "biases", "biases towards", "biologically female",
                   "biologically male", "BIPOC", "Black", "clean energy", "climate crisis", "climate science",
                   "commercial sex worker", "community diversity", "community equity", "confirmation bias",
                   "cultural competence", "cultural differences", "cultural heritage", "cultural sensitivity",
                   "culturally appropriate", "culturally responsive", "DEI", "DEIA", "DEIAB", "DEIJ",
                   "disabilities", "disability", "discriminated", "discrimination", "discriminatory", "disparity",
                   "diverse", "diverse backgrounds", "diverse communities", "diverse community", "diverse group",
                   "diverse groups", "diversified", "diversify", "diversifying", "diversity", "enhance the diversity",
                   "enhancing diversity", "environmental quality", "equal opportunity", "equality", "equitable",
                   "equitableness", "equity", "ethnicity", "excluded", "exclusion", "expression", "female",
                   "females", "feminism", "fostering inclusivity", "GBV", "gender", "gender based",
                   "gender based violence", "gender diversity", "gender identity", "gender ideology",
                   "gender-affirming care", "genders", "Gulf of Mexico", "hate speech", "health disparity",
                   "health equity", "hispanic minority", "historically", "identity", "immigrants", "implicit bias",
                   "implicit biases", "inclusion", "inclusive", "inclusive leadership", "inclusiveness",
                   "inclusivity", "increase diversity", "increase the diversity", "indigenous community",
                   "inequalities", "inequality", "inequitable", "inequities", "inequity", "injustice",
                   "institutional", "intersectional", "intersectionality", "key groups", "key people",
                   "key populations", "Latinx", "LGBT", "LGBTQ", "marginalize", "marginalized",
                   "men who have sex with men", "mental health", "minorities", "minority", "most risk", "MSM",
                   "multicultural", "Mx", "Native American", "non-binary", "nonbinary", "oppression", "oppressive",
                   "orientation", "people-centered care", "person-centered", "person-centered care",
                   "polarization", "political", "pollution", "pregnant people", "pregnant person", "pregnant persons",
                   "prejudice", "privilege", "privileges", "promote diversity", "promoting diversity", "pronoun",
                   "pronouns", "prostitute", "race", "racial", "racial diversity",
                   "racial identity", "racial inequality", "racial justice", "racially", "racism", "segregation",
                   "sense of belonging", "sex", "sexual preferences", "sexuality", "social justice", "sociocultural",
                   "socioeconomic", "status", "stereotype", "stereotypes", "systemic", "systemically", "they/them",
                   "trans", "transgender", "transsexual", "trauma", "traumatic", "tribal", "unconscious bias",
                   "underappreciated", "underprivileged", "underrepresentation", "underrepresented", "underserved",
                   "undervalued", "victim", "victims", "vulnerable populations", "women"]







# List as given in NYT
# BANNED_LIST = ["accessible", "activism", "activists", "advocacy", "advocate", "advocates", "affirming care",
#                    "all-inclusive", "allyship", "anti-racism", "antiracist", "assigned at birth",
#                    "assigned female at birth", "assigned male at birth", "at risk", "barrier", "barriers", "belong",
#                    "bias", "biased", "biased toward", "biases", "biases towards", "biologically female",
#                    "biologically male", "BIPOC", "Black", "breastfeed + people", "breastfeed + person",
#                    "chestfeed + people", "chestfeed + person", "clean energy", "climate crisis", "climate science",
#                    "commercial sex worker", "community diversity", "community equity", "confirmation bias",
#                    "cultural competence", "cultural differences", "cultural heritage", "cultural sensitivity",
#                    "culturally appropriate", "culturally responsive", "DEI", "DEIA", "DEIAB", "DEIJ",
#                    "disabilities", "disability", "discriminated", "discrimination", "discriminatory", "disparity",
#                    "diverse", "diverse backgrounds", "diverse communities", "diverse community", "diverse group",
#                    "diverse groups", "diversified", "diversify", "diversifying", "diversity", "enhance the diversity",
#                    "enhancing diversity", "environmental quality", "equal opportunity", "equality", "equitable",
#                    "equitableness", "equity", "ethnicity", "excluded", "exclusion", "expression", "female",
#                    "females", "feminism", "fostering inclusivity", "GBV", "gender", "gender based",
#                    "gender based violence", "gender diversity", "gender identity", "gender ideology",
#                    "gender-affirming care", "genders", "Gulf of Mexico", "hate speech", "health disparity",
#                    "health equity", "hispanic minority", "historically", "identity", "immigrants", "implicit bias",
#                    "implicit biases", "inclusion", "inclusive", "inclusive leadership", "inclusiveness",
#                    "inclusivity", "increase diversity", "increase the diversity", "indigenous community",
#                    "inequalities", "inequality", "inequitable", "inequities", "inequity", "injustice",
#                    "institutional", "intersectional", "intersectionality", "key groups", "key people",
#                    "key populations", "Latinx", "LGBT", "LGBTQ", "marginalize", "marginalized",
#                    "men who have sex with men", "mental health", "minorities", "minority", "most risk", "MSM",
#                    "multicultural", "Mx", "Native American", "non-binary", "nonbinary", "oppression", "oppressive",
#                    "orientation", "people + uterus", "people-centered care", "person-centered", "person-centered care",
#                    "polarization", "political", "pollution", "pregnant people", "pregnant person", "pregnant persons",
#                    "prejudice", "privilege", "privileges", "promote diversity", "promoting diversity", "pronoun",
#                    "pronouns", "prostitute", "race", "race and ethnicity", "racial", "racial diversity",
#                    "racial identity", "racial inequality", "racial justice", "racially", "racism", "segregation",
#                    "sense of belonging", "sex", "sexual preferences", "sexuality", "social justice", "sociocultural",
#                    "socioeconomic", "status", "stereotype", "stereotypes", "systemic", "systemically", "they/them",
#                    "trans", "transgender", "transsexual", "trauma", "traumatic", "tribal", "unconscious bias",
#                    "underappreciated", "underprivileged", "underrepresentation", "underrepresented", "underserved",
#                    "undervalued", "victim", "victims", "vulnerable populations", "women", "women and underrepresented"]