#------------------
# Clustering
#------------------

 1.
  # Load the data
  data("USArrests")
  head(USArrests)
  summary(USArrests)
  # Standardize the data
  df <- scale(USArrests)
  summary(df)
  
  # Step 2.
  # Compute the distance matrix
  # df = the standardized data
  res.dist <- dist(df, method = "euclidean")
  as.matrix(res.dist)[1:6, 1:6]
  
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
  