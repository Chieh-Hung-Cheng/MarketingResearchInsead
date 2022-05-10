# Conjoint
library(readxl)# read_excel
levels = read.csv("C:\\Users\\ChiehHung\\Documents\\R_codes\\lego_level.csv"); levels
profiles = read.csv("C:\\Users\\ChiehHung\\Documents\\R_codes\\lego_profile.csv"); profiles
ratings = read.csv("C:\\Users\\ChiehHung\\Documents\\R_codes\\lego_ratings.csv"); ratings

library(conjoint)
part_uts = caPartUtilities(ratings, profiles, levels); part_uts
avg_uts = Conjoint(ratings, profiles, levels); avg_uts

# Orthogonal array
library(DoE.base)
oa.design(nlevels=c(3,3,3))

# Market Share
caUTs = function(x){rowSums(part_uts[, c(1, x+c(1,1+3, 1+3+3))])}
newprofiles = list(c(1,3,1), c(3,2,3), c(1,1,2)); newprofiles
UTs = sapply(newprofiles, caUTs); UTs
argmaxUTs = apply(UTs, 1, which.max); argmaxUTs
tb = table(argmaxUTs)
names(tb) <- c("Product1", "Product2", "Product3"); tb

# T test
# compared with average mu
data = read.csv("C:\\Users\\ChiehHung\\Documents\\R_codes\\{}.csv"); data
t.test({}, mu={}, alternative="two_sided")

# two population
t.test({}, {}, alternative="two.sided")

# paired t-test
promotion = read.csv("C:\\Users\\ChiehHung\\Documents\\R_codes\\promotion.csv")
before = promotion[,1]; before
after = promotion[,2]; after
t.test(after, before, paired=TRUE, alternative='two.sided')

# Chi-square
#one-dimensional
obs = c({})
expt = c({})
q = sum((obs-expt)^2/expt);q
pvalue = 1-pchisq(q, df={n}-1);pvalue

#two-dimensional
obs = matrix(c(58,13,39,41,42,37,31,65,34), nrow=3, ncol=3, byrow=TRUE); obs
expt = matrix(c(130*110/360, 120*110/360, 110*110/360, 130*120/360,120*120/360,110*120/360,130*130/360,120*130/360,110*130/360), nrow=3, ncol=3, byrow=TRUE); expt
q = sum((obs-expt)^2/expt); q
pvalue = 1-pchisq(q, df=(3-1)*(3-1)); pvalue

#ANOVA
AOV = aov({}~factor({})*factor({}), data={})
summary(AOV)

#Alpha test
library(ltm)
resp = read.csv("C:\\Users\\ChiehHung\\PycharmProjects\\insead\\havard_insead.csv"); resp
cronbach.alpha(resp)
cronbach.alpha(resp[,c(7,11,18)])




