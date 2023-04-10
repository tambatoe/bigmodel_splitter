
intersection()
{
    import(file_to_split, convexity=3, center=true);
 
    color("red")
    translate([cube_posX, cube_posY, cube_posZ])
    cube([cubeszX, cubeszY, cubeszZ], center=true);
};