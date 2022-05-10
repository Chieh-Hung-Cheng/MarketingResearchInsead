#------------------
# Clustering
#------------------
# Prerequisite
# install.packages("factoextra")
library("factoextra")


 1.
  # Load the data
  df = read.csv("C:\\Users\\ChiehHung\\PycharmProjects\\insead\\former_wtavg.csv")
  head(df)
  summary(df)
  # Standardize
  df_nmlz <- scale(df[, 4:8])# scale(df[,3:28])
  head(df_nmlz)
  summary(df_nmlz)
  
  # Search # of clusters
  fviz_nbclust(df_nmlz, 
               FUNcluster = hcut,
               method = "wss",
               k.max = 10 )
  
  
  # Compute the distance matrix using normalized data
  res.dist <- dist(df_nmlz, method = "euclidean")
  as.matrix(res.dist)[1:70, 1:70]# [1:389, 1:389]
  
  # Clustering
  res.hc <- hclust(d = res.dist, method = "ward.D2")
  fviz_dend(res.hc, cex = 0.5)
  res.coph <- cophenetic(res.hc)
  cor(res.dist, res.coph)
  # Cut and visualize
  grp <- cutree(res.hc, k = 2)
  fviz_dend(res.hc, k = 2, rect = TRUE, cex = 0.3)
  table(grp)
  g1 = df[grp==1,]
  summary(g1)
  g2 = df[grp==2,]
  summary(g2)
  g3 = df[grp==3,]
  summary(g3)
  
  # Step 3.
  res.hc <- hclust(d = res.dist, method = "ward.D2"complete method = ??ward.D, ??wa.D, ??cole??, ??av, ?, ??meit or ??...omplete, average linkage and Ward??s methare generally preferred
  library("factoextra")
    # instpackages("factoextra")
  fviz_dend(res.hc, cex = 0.5)
    # height is known as the cophenetic distance between the two objects
  # Assess algorithms
  res.coph <- cophenetic(res.hc)
  cor(res.dist, res.coph)
  res.hc2 <- hclust(res.dist, method = "average")
  cor(res.dist, cophenetic(res.hc2))
  
  # Step 4.
  # Cut tree into 4 groups
  grp <- cutree(res.hc, k = 4)
  head(grp, 10)
  # Number of members in each cluster
  table(grp)
  # Get the names for the members of cluster 1
  grp == 1
  rownames(df)[grp == 1]
  rownames(df)[grp == 4]
  # Visualization
  fviz_dend(res.hc, k = 4, rect = TRUE)
  fviz_dend(res.hc, k = 4, rect = TRUE, cex = 0.5)
  
# ?À³Î¦?Æ¥????w?À¸
d(df)
  
  # Step 2.
  # Compute k-means with k = 4
  set.seed(123)
  km.res <- kmeans(df, centers = 4)
  # Print the results
  print(km.res)
  km.res$cluster
  km.res$size
  km.res$centers
  
  # Step 3.
  # ?À¸s?Ì¨Î¼Æ¥Ø¡A?Ø¼_nbclust(df, 
               FUNcluster = kmeans,  # kmeans
               method = "wss",     # total within sum of square
               k.max = 10          # max number of clusters to consider
               )
  fviz_nbclust(df, 
               FUNcluster = hcut,  # ???h???À¸s
           s",     # total within sum of square
               k.max = 10          # max number of clusters to consider
  )
  # Visualization
  fviz_cluster(km.res, data = df, labelsize = 8)
  fviz_cluster(km.res, data = df, labelsize = 8, ggtheme = theme_bw())
  