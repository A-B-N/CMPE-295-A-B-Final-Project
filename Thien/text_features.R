# chooseCRANmirror(graphics=FALSE, ind=1)
# knitr::opts_chunk$set(echo = TRUE)
# install.packages("scales", repos = "http://cran.us.r-project.org")
# install.packages("lmtest", repos = "http://cran.us.r-project.org")
# install.packages("tidyverse", repos = "http://cran.us.r-project.org")
# install.packages("rlang", repos = "http://cran.us.r-project.org")
# install.packages("tidyverse", dependencies=TRUE, repos = "http://cran.us.r-project.org")
# install.packages("mnormt", repos = "http://cran.us.r-project.org")
# install.packages("foreign", repos = "http://cran.us.r-project.org")
# install.packages("reshape2", repos = "http://cran.us.r-project.org")
# install.packages("hunspell", repos = "http://cran.us.r-project.org")
# install.packages("tokenizers", repos = "http://cran.us.r-project.org")
# install.packages("janeaustenr", repos = "http://cran.us.r-project.org")
# install.packages("dplyr", repos = "http://cran.us.r-project.org")
# install.packages("ggplot2", repos = "http://cran.us.r-project.org")
# install.packages("tidytext", repos = "http://cran.us.r-project.org")
install.packages("data.table", repos = "http://cran.us.r-project.org")

library(tidyverse)
library(tidytext)

df <- data.table::fread("reviews.csv", data.table = FALSE) %>%
  rename(ID = V1) %>%
  select(-Title) %>%
  mutate(Age = as.integer(Age))

glimpse(df)


