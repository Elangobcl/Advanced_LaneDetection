    
src = np.float32([[img.shape[1]*(0.52-mid_width/2), img.shape[0]*height_pct],[img.shape[1]*(0.535+mid_width/2),img.shape[0]*height_pct],
                      [img.shape[1]*(0.47+bot_width/2), img.shape[0]*bottom_trim],[img.shape[1]*(0.375-bot_width/2), img.shape[0]*bottom_trim]])
offset = img_size[0]*0.25
dst = np.float32([[offset,0],[img_size[0]-offset,0],[img_size[0]-offset,img_size[1]],[offset,img_size[1]]])

    bot_width = .76 # percentage of bottom trapezoidal height
    mid_width = .08 # percentage of mid trapezoidal height
    height_pct = .50 # percentage of trapezoidal height
    bottom_trim= .935 # percentage from top to bottom avoiding the hood of the car

    src = np.float32([[img.shape[1]*(0.54-mid_width/2), img.shape[0]*height_pct],[img.shape[1]*(0.535+mid_width/2),img.shape[0]*height_pct],
                      [img.shape[1]*(0.475+bot_width/2), img.shape[0]*bottom_trim],[img.shape[1]*(0.38-bot_width/2), img.shape[0]*bottom_trim]])


## o/p - 6

    bot_width = .76 # percentage of bottom trapezoidal height
    mid_width = .08 # percentage of mid trapezoidal height
    height_pct = .52 # percentage of trapezoidal height
    bottom_trim= .935 # percentage from top to bottom avoiding the hood of the car

    src = np.float32([[img.shape[1]*(0.530-mid_width/2), img.shape[0]*height_pct],[img.shape[1]*(0.515+mid_width/2),img.shape[0]*height_pct],
                      [img.shape[1]*(0.475+bot_width/2), img.shape[0]*bottom_trim],[img.shape[1]*(0.38-bot_width/2), img.shape[0]*bottom_trim]])
    offset = img_size[0]*0.14

