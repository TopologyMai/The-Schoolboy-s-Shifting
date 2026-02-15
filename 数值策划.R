# ==========================================
# 糕糕的校园漂流 - 数值模拟器 (A/B 路线对比版)
# ==========================================
library(ggplot2)
library(dplyr)
library(tidyr)

set.seed(42)

simulate_playthrough <- function(route_choice) {
  # --- 初始属性 ---
  res <- 5
  con <- 5
  
  # --- 第一幕 ---
  # 分支 0
  s0 <- sample(1:2, 1)
  if(s0 == 1) { res <- res - 0.5; con <- con + 1 } else { res <- res + 0.5; con <- con - 0.5 }
  
  # 分支 1
  s1 <- sample(1:3, 1)
  if(s1 == 1) { res <- res - 1; con <- con + 2 } 
  else if(s1 == 2) { res <- res + 0.5; con <- con + 1 } 
  else { res <- res + 2; con <- con - 1 }
  
  # 分支 2
  s2 <- sample(1:2, 1)
  if(s2 == 1) { res <- res + 1.5; con <- con - 1 } else { res <- res - 2; con <- con + 0.5 }
  
  # --- 第二幕 ---
  # 分支 3
  s3 <- sample(1:3, 1)
  if(s3 == 1) { res <- res - 1; con <- con + 1.5 } 
  else if(s3 == 2) { res <- res + 2; con <- con + 1 } 
  else { res <- res + 0.5; con <- con - 1 }
  
  # 分支 4 (根据输入修正了逻辑)
  s4 <- sample(1:3, 1)
  
  if (s4 == 1) {
    res <- res + 2
    con <- con - 1.5
    
  } else if (s4 == 3) {
    res <- res + 1.5
    con <- con - 1
    
  } else {
    # 选项 2：进入二级选择
    s4_2 <- sample(1:2, 1)
    
    if (s4_2 == 1) {
      # 隐藏选项（如果暂时不影响数值）
      res <- res + 0
      con <- con + 0
    } else {
      # 选项 2-2
      res <- res - 0.5
      con <- con + 1
    }
  }
  
  
  # 分支 5
  s5 <- sample(1:2, 1)
  if(s5 == 1) { res <- res + 2; con <- con - 1.5 } else { res <- res - 2; con <- con + 2.5 }
  
  # --- 第三 & 四幕：分支路线选择 ---
  if(route_choice == "Route_A") {
    # 路线 A (原 Music 线逻辑更新)
    s6 <- sample(1:3, 1); if(s6==1){res<-res-1.5;con<-con+1.5} else if(s6==2){res<-res+1.5;con<-con-1} else {res<-res-2;con<-con+2}
    s7 <- sample(1:3, 1); if(s7==1){res<-res-2;con<-con+3} else if(s7==2){res<-res+3;con<-con-2} else {res<-res+1;con<-con-1.5}
    s10 <- sample(1:3, 1); if(s10==1){res<-res-0.5;con<-con+2} else if(s10==2){res<-res-2;con<-con+3} else {res<-res+3;con<-con+2}
    s11 <- sample(1:3, 1); if(s11==1){res<-res+1.5;con<-con-2} else if(s11==2){res<-res+2;con<-con-3} else {res<-res-2;con<-con+2}
  } else {
    # 路线 B (原 Basketball 线逻辑更新)
    s8 <- sample(1:3, 1); if(s8==1){res<-res+2;con<-con-1.5} else if(s8==2){res<-res+0.5;con<-con+1.5} else {res<-res-2;con<-con+2}
    s9 <- sample(1:3, 1); if(s9==1){res<-res-1.5;con<-con+2} else if(s9==2){res<-res+2;con<-con-1.5} else {res<-res-2;con<-con+3}
    s12 <- sample(1:3, 1); if(s12==1){res<-res+2;con<-con+0.5} else if(s12==2){res<-res+3;con<-con-1.5} else {res<-res-2;con<-con+2}
    s13 <- sample(1:3, 1); if(s13==1){res<-res-2;con<-con+3} else if(s13==2){res<-res+1.5;con<-con-2.5} else {res<-res+3;con<-con-2}
  }
  
  # --- 第五幕 ---
  # 分支 14 (数值无变动 0/0)
  # 分支 15
  s15 <- sample(1:2, 1)
  if(s15 == 1) { res <- res - 1; con <- con + 1 } else { res <- res + 1; con <- con - 1 }
  
  return(data.frame(Resonance = res, Control = con, Route = route_choice))
}

# 2. 运行模拟 (各路线运行 5,000 次，总计 10,000 次)
n_each <- 5000
sim_a <- replicate(n_each, simulate_playthrough("Route_A"), simplify = FALSE) %>% bind_rows()
sim_b <- replicate(n_each, simulate_playthrough("Route_B"), simplify = FALSE) %>% bind_rows()
sim_data <- bind_rows(sim_a, sim_b)

sim_data <- sim_data %>%
  mutate(
    Total = Resonance + Control,
    Diff = Resonance - Control
  )

# 3. 结局逻辑判定 (优化版)
sim_data <- sim_data %>%
  mutate(Ending = case_when(
    Total < 14 ~ "Ending D",
    
    Route == "Route_B" & (Total >= 17 & abs(Diff) <= 3.5) ~ "True Ending",
    Route == "Route_A" & (Total >= 16 & abs(Diff) <= 3.5) ~ "True Ending",
    
    (Diff > 7) ~ "Ending B",
    (Diff < -7) ~ "Ending C",
    
    TRUE ~ "Ending A"  # 其他所有情况归为 A
  ))

# 4. 输出分路线统计结果
stats_compare <- sim_data %>% 
  group_by(Route, Ending) %>% 
  summarise(Count = n(), .groups = 'drop') %>%
  group_by(Route) %>%
  mutate(Percentage = paste0(round(Count / sum(Count) * 100, 2), "%"))

print("--- 路线对比统计 ---")
print(stats_compare)

# 5. 可视化对比分析
ggplot(sim_data, aes(x = Resonance, y = Control, color = Ending)) +
  geom_jitter(alpha = 0.3, size = 0.8) +
  facet_wrap(~Route) +  # 分左右两图对比
  theme_minimal() +
  labs(title = "Monte Carlo Simulation: Route A vs Route B",
       subtitle = "Comparison of Resonance and Control distribution",
       x = "Resonance", y = "Control") +
  scale_color_brewer(palette = "Set1") +
  theme(legend.position = "bottom")