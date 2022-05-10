# Factor Analysis, VIF
#------------------
library(lavaan)
library(semPlot)
library(psych)
library(readxl)
df = read.csv("C:\\Users\\ChiehHung\\PycharmProjects\\insead\\insead_dataset_nodul.csv"); df
head(df)
summary(df)
hs <- df[,c(33:54)]; hs
head(hs)

# EFA
  # Determining # of Factors
  # Parallel Analysis (PCA and FA)  
  fa.parallel(cor(hs), n.obs = 459, fa = "both", n.iter = 100, main = "PC analysis")
  #EFA with rotation
  fa.pc <- principal(r = hs, nfactors = 3, rotate = "varimax"); fa.pc
  # Varimax` and `Oblimin` are the most popular
  # visualization 
  # factor.plot(efa.pc)
  # fa.diagram(efa.pc, digits = 3) 
 
#CFA 
  # Check assumption
    hist(df$Q17_1)
  # Specifying a CFA model
    # To build a CFA model in lavaan, you??ll save a string with the model details. 
    # Each line is one latent factor, with its indicators following the =~ (read this symbol as ??is measured by??).
    #HS.model <- ' f1 =~ Q17_2  + Q17_3 + Q17_4 + Q17_5 + Q17_9 + Q17_10+ Q17_11 + Q17_15 + Q17_16 + Q17_18 + Q17_19 + Q17_20 + Q17_21 + Q17_23 + Q17_25 + Q17_26
    #              f2 =~ Q17_7 + Q17_14 + Q17_27 + Q17_29
    #              f3 =~ Q17_1 + Q17_8'
    #HS.model <- ' cirr =~ Q17_2  + Q17_5 + Q17_6 + Q17_12 + Q17_13 + Q17_14 + Q17_17 + Q17_18 + Q17_22 + Q17_30
    #              ena =~ Q17_9 + Q17_11 + Q17_15 + Q17_21 + Q17_24 + Q17_28 + Q17_29'
    HS.model <- ' f1 =~ Q17_2 + Q17_12 + Q17_13 + Q17_14 + Q17_17 + Q17_18 + Q17_22
                  f2 =~ Q17_4 + Q17_8 + Q17_15 + Q17_28 + Q17_29
                  f3 =~ Q17_9 + Q17_16 + Q17_19 + Q17_21 + Q17_24
                  f4 =~ Q17_1 + Q17_3 + Q17_6 + Q17_23 + Q17_26'
    
    #HS.model <- ' f1 =~ Q17_2 + Q17_8 + Q17_12 + Q17_13 + Q17_17 + Q17_19 + Q17_23
    #              f2 =~ Q17_3 + Q17_5 + Q17_9 + Q17_15 + Q17_20 + Q17_29
    #              f3 =~ Q17_1 + Q17_4 + Q17_10 + Q17_11 + Q17_14 + Q17_18 + Q17_22 + Q17_25 + Q17_28 + Q17_30
    #              f4 =~ Q17_6 + Q17_7 + Q17_16 + Q17_24 + Q17_27'
    
    #HS.model <- ' f1 =~ Q17_1 + Q17_2 + Q17_3 + Q17_6 + Q17_12 + Q17_13 + Q17_14 + Q17_23 + Q17_26 + Q17_30
    #              f2 =~ Q17_4 + Q17_8 + Q17_15 + Q17_28 + Q17_29
    #              f3 =~ Q17_9 + Q17_16 + Q17_19 + Q17_21 + Q17_24'
    
    fit <- cfa(HS.model, data = df, std.lv = TRUE)
    summary(fit, fit.measures = TRUE, standardized = TRUE)
    fitMeasures(fit, c("cfi","srmr","gfi","rmsea"))
    semPaths(fit,"std", curvePivot = TRUE,optimizeLatRes=TRUE,sizeMan=3)
    # model fit indices:
    # CFI (Comparative Fit Index), GFI (goodness of fit index) >0.9~0.8
    # RMSEA (Root Mean Square Error of Approximation) <0.08~0.1
    # SRMR (Standardized Root Mean Square Residual) 0.06~0.08


# VIF
    library(car)
    head(iris)
    model.iris <- lm(Sepal.Length ~ Sepal.Width + Petal.Width + Petal.Length,  # y = ?á¸????? 
                     data = iris)
    summary(model.iris)
    vif(model.iris) 
    #VIF <10
    model.iris.new <- lm(Sepal.Length ~ Sepal.Width + Petal.Width, data = iris)
    summary(model.iris.new)
    vif(model.iris.new)
    
    