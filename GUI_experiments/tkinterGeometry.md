# Three Types Of Tkinter Geometry Managers
## 1. Pack
algorithm pack child widgets against inner edge of parent or other widget objects already packed against an inner edge, then calculates a bounding box, stretching it to encompass them
#### Pros
  -  simple to use
  - use when widget expanded to fill entire frame
  - use to stack multiple widgets vertical or horizontal
  - responsive

#### Cons
  -  unsuitable for complex layouts

## 2. Grid
for organizing widgets in vertical and horizontal relationships
   #### Pros
   -  like using HTML tables you can specify rowspan and colspumnspan
   -  can leave gaps in the form of empty rows or columnspan
   -  order that widgets are defined in code makes no difference to the placement in the GUI
   - responsive

#### Cons
  -  more involved and requires pre planning your layout
  -  sticky command syntax is a little clunky to control the cell fills, i.e. stick a label to all compass directions to fill the cell or a single direction to align it

## 3. Place
when widget placement needs to be fixed in reference to the parent (which should not be resizable)
####  Pros
-  very exact control of widget location and size including overlap
-  describe location in absolute or relative terms

####  Cons
  -  difficult to manage a large number of widgets
  - does not suit responsive controls
