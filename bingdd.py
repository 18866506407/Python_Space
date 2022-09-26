import turtle

turtle.title( 'PythonBingDwenDwen' )

turtle.speed( 100 )  # 速度

# 左手
turtle.penup()
turtle.goto( 177 , 112 )
turtle.pencolor( "lightgray" )
turtle.pensize( 3 )
turtle.fillcolor( "white" )
turtle.begin_fill()
turtle.pendown()
turtle.setheading( 80 )
turtle.circle( -45 , 200 )
turtle.circle( -300 , 23 )
turtle.end_fill()

# 左手内
turtle.penup()
turtle.goto( 182 , 95 )
turtle.pencolor( "black" )
turtle.pensize( 1 )
turtle.fillcolor( "black" )
turtle.begin_fill()
turtle.setheading( 95 )
turtle.pendown()
turtle.circle( -37 , 160 )
turtle.circle( -20 , 50 )
turtle.circle( -200 , 30 )
turtle.end_fill()
# 轮廓
# 头顶
turtle.penup()
turtle.goto( -73 , 230 )
turtle.pencolor( "lightgray" )
turtle.pensize( 3 )
turtle.fillcolor( "white" )
turtle.begin_fill()
turtle.pendown()
turtle.setheading( 20 )
turtle.circle( -250 , 35 )
# 左耳
turtle.setheading( 50 )
turtle.circle( -42 , 180 )
# 左侧
turtle.setheading( -50 )
turtle.circle( -190 , 30 )
turtle.circle( -320 , 45 )
# 左腿
turtle.circle( 120 , 30 )
turtle.circle( 200 , 12 )
turtle.circle( -18 , 85 )
turtle.circle( -180 , 23 )
turtle.circle( -20 , 110 )
turtle.circle( 15 , 115 )
turtle.circle( 100 , 12 )
# 右腿
turtle.circle( 15 , 120 )
turtle.circle( -15 , 110 )
turtle.circle( -150 , 30 )
turtle.circle( -15 , 70 )
turtle.circle( -150 , 10 )
turtle.circle( 200 , 35 )
turtle.circle( -150 , 20 )
# 右手
turtle.setheading( -120 )
turtle.circle( 50 , 30 )
turtle.circle( -35 , 200 )
turtle.circle( -300 , 23 )
# 右侧
turtle.setheading( 86 )
turtle.circle( -300 , 26 )
# 右耳
turtle.setheading( 122 )
turtle.circle( -53 , 160 )
turtle.end_fill()

# 右耳内
turtle.penup()
turtle.goto( -130 , 180 )
turtle.pencolor( "black" )
turtle.pensize( 1 )
turtle.fillcolor( "black" )
turtle.begin_fill()
turtle.pendown()
turtle.setheading( 120 )
turtle.circle( -28 , 160 )
turtle.setheading( 210 )
turtle.circle( 150 , 20 )
turtle.end_fill()

# 左耳内
turtle.penup()
turtle.goto( 90 , 230 )
turtle.setheading( 40 )
turtle.begin_fill()
turtle.pendown()
turtle.circle( -30 , 170 )
turtle.setheading( 125 )
turtle.circle


# 不关闭窗口

turtle.exitonclick()