# Function to read in files

read_data = function(filepath) {
  data = read.csv(filepath, header = F)
  
  return(data)
}


drop_instance_weight = function(data) {
  newdata = data %>% 
    select(-instance_weight)
  
  return(newdata)
}


to_character = function(data, cols_to_convert) {
  newdata = data %>% 
    mutate_at(vars(cols_to_convert), as.character)
  
  return(newdata)
}


drop_children = function(data) {
  newdata = data %>% 
    filter(age >= 15)
  
  return(newdata)
}
