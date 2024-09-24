Practical 8 

activities=data.frame(
 From=c(1,2,2,3,4,5,6),
 To=c(2,3,4,5,6,7,7),
 Time=c(2,4,3,2,1,2,3)
 )
 g=graph_from_data_frame(activities,directed=TRUE)
 E(g)$weight=activities$Time
 plot(g,edge.label=E(g)$weight,vertex.size=30,edge.arrow.size=0.5,main="Project Network
Diagram")
 E(g)$neg_weight=-E(g)$weight

shortest_paths_result=shortest_paths(g,from=1,to=8,weights=E(g)$neg_weight,mode="out",outp
ut="both")
 critical_path_edges=shortest_paths_result$epath[[1]]
 critical_path_duration= -sum(E(g)$neg_weight[critical_path_edges])
 project_completion_time=critical_path_duration
 print(paste("Critical Path Duration:",critical_path_duration))
 print(paste("Project Completion Time:",project_completion_time))
 critical_path_edges_ids<-as_ids(critical_path_edges)
 critical_path_activities<-unique(c(
 activities$From[activities$From%in%V(g)[.from(critical_path_edges)]],
 activities$To[activities$To%in%V(g)[.to(critical_path_edges)]]
 ))
 print(paste("Critical Path Activities:",paste(critical_path_activities,collapse="")))


Practical 9 

activities=data.frame(
    from=c(1,1,2,2,3,4,5,4),
      to=c (2,3,3,5,4,5,6,6),
        a=c(1,1,0,1,1,0,1,1), 
        m=c(4,2,0,4.5,3,0,1,2),
         b=c (7,3,0,11,5,0,1,3)
)
activities$Expected_Time = (activities$a + 4 * activities$m + activities$b) / 6
activities$Variance = ((activities$b - activities$a) / 6)^2
g = graph_from_data_frame (d = activities [, c("from", "to", "Expected_Time")], directed = TRUE)
 E(g)$weight = activities$Expected_Time
plot (g, edge.label = E (g) $weight, main = "PERT Network", vertex.label = V(g) $name)
# Non-positive edge weight found, ignoring all weights during graph layout.