# Factor Analysis, VIF
#------------------

install.packages("lavaan")
install.packages("semPlot")
install.packages("psych")
library(lavaan)
library(semPlot)
library(psych)

# data
?HolzingerSwineford1939
df <- HolzingerSwineford1939
head(df)
summary(df)
hs <- df[,c(7:15)]
head(hs)

# EFA
  # Determining # of Factors
  # Parallel Analysis (PCA and FA)  
  fa.parallel(cor(hs), n.obs = 301, fa = "both", n.iter = 100, main = "PC analysis")
  #EFA with rotation
  fa.pc <- principal(r = hs, nfactors = 3, rotate = "varimax") 
  fa.pc
  # Varimax` and `Oblimin` are the most popular
  # visualization 
  factor.plot(efa.pc)
  fa.diagram(efa.pc, digits = 3) 
  
#CFA 
  # Check assumption
    hist(df$x1)
    hist(df$x2)
    hist(df$x3)
    hist(df$x6)
  # Specifying a CFA model
    # To build a CFA model in lavaan, you??ll save a string with the model details. 
    # Each line is one latent factor, with its indicators following the =~ (read this symbol as ??is measured by??).
    HS.model <- ' visual  =~ x1 + x2 + x3
                  textual =~ x4 + x5 + x6
                  speed   =~ x7 + x8 + x9 '
    
    fit <- cfa(HS.model, data = df, 
               std.lv = TRUE)
    summary(fit, fit.measures = TRUE, standardized = TRUE)
    fitMeasures(fit, c("cfi","srmr","gfi","rmsea"))
    # model fit indices:
    # CFI (Comparative Fit Index), GFI (goodness of fit index) >0.9~0.8
    # RMSEA (Root Mean Square Error of Approximation) <0.08~0.1
    # SRMR (Standardized Root Mean Square Residual) 0.06~0.08


# VIF
    library(car)
    head(iris)
    model.iris <- lm(Sepal.Length ~ Sepal.Width + Petal.Width + Petal.Length,  # y = ?Ḱ???? 
                     data = iris)
    summary(model.iris)
    vif(model.iris) 
    #VIF <10
    model.iris.new <- lm(Sepal.Length ~ Sepal.Width + Petal.Width, data = iris)
    summary(model.iris.new)
    vif(model.iris.new)
    
    