---
title: Revision sheet
---

# Revision sheet — Geographic Information Systems

No GIS module split is documented in the repository, so this sheet is grouped by topic rather than by numbered modules. It is a topic outline built from the README summary and standard GIS concepts. The material folder contains no GIS notes, paper or question bank; see the question-bank note at the end before relying on it for assessment practice.

## Exam pattern

The README gives CIE 50 + SEE 50. No GIS paper, scheme or question bank is present, so the section split and question types cannot be confirmed from this repository.

## Topic 1 — Spatial data and GIS fundamentals

### Must know

- A GIS captures, stores, checks, integrates, analyses and displays spatially referenced data.
- Its components are hardware, software, data, people and methods.
- Spatial data has location, attributes, topology and often time.
- Vector data uses points, lines and polygons, each linked to an attribute table.
- Raster data is a grid of cells, each holding one value; cell size sets the resolution.
- Vector suits precise boundaries and networks; raster suits continuous surfaces and area calculations.
- Topology records adjacency, connectivity and containment, enabling network and overlay operations.
- Attribute types are nominal, ordinal, interval and ratio; only the last two support arithmetic.
- Scale, generalisation and metadata determine how faithfully a dataset represents the ground.
- A DEM stores elevation; a TIN models terrain as irregular triangles.

### Definitions to reproduce

> A geographic information system is a computer system for capturing, storing, querying, analysing and displaying spatially referenced data.

> Vector data represents geographic features as points, lines and polygons with associated attributes.

> Raster data represents space as a regular grid of cells, each cell carrying a value for the mapped variable.

## Topic 2 — Coordinate systems, datums and projections

### Must know

- Geographic coordinates give latitude and longitude on an ellipsoid; a datum fixes that ellipsoid and its origin.
- A projected coordinate system places the curved surface on a plane and measures in metres.
- Every projection distorts shape, area, distance or direction; none preserves all four.
- Conformal projections preserve local shape; equal-area projections preserve area.
- Equidistant projections preserve distance from a chosen point or line; azimuthal projections preserve direction from the centre.
- UTM divides the world into 60 zones, each six degrees wide, using a transverse Mercator projection.
- An EPSG code identifies a coordinate reference system unambiguously.
- Georeferencing assigns coordinates to a raster or image using ground control points.
- Reprojection converts data between systems; a datum transformation may also be required.
- Positional accuracy is not the same as precision, and both differ from scale.

### Definitions to reproduce

> A map projection is a mathematical transformation from positions on the curved Earth to positions on a plane.

> A datum is a reference surface and origin used to define geographic coordinates.

## Topic 3 — Spatial analysis

### Must know

- Selection can be by attribute, by location or by a combination of both.
- Overlay combines layers: clip cuts, intersect keeps the overlap, union keeps everything, erase removes.
- A buffer creates a zone at a set distance from a feature.
- Dissolve merges adjacent features that share an attribute value.
- A spatial join transfers attributes from one layer to another using location.
- Network analysis solves shortest path, closest facility and service-area problems.
- Raster map algebra combines layers cell by cell with arithmetic or logical operators.
- Reclassification groups cell values into new classes; slope and aspect derive from a DEM.
- Interpolation estimates values at unmeasured points by IDW, spline or kriging.
- The modifiable areal unit problem and the ecological fallacy warn against reading individual conclusions from aggregate zones.

### Definitions to reproduce

> Overlay analysis combines two or more spatial layers to produce a new layer with combined geometry and attributes.

> Spatial interpolation estimates the value of a variable at an unmeasured location from nearby measured values.

## Topic 4 — Data capture, quality and QGIS

### Must know

- Sources include digitising, GPS, remote sensing, field survey and existing datasets.
- Digitising needs snapping and topology rules; common errors are undershoot, overshoot, gaps and slivers.
- Accuracy is closeness to truth; precision is repeatability. Both are separate from resolution.
- Data quality covers positional, attribute, temporal and logical consistency, and completeness.
- Metadata records source, date, projection, scale, accuracy and processing steps.
- In QGIS, add vector and raster layers, set the project CRS, and inspect the attribute table.
- The field calculator creates or updates attributes; symbology controls how features are drawn.
- The processing toolbox provides buffer, clip, intersect, dissolve, join and raster tools.
- The print layout adds a title, legend, scale bar, north arrow and locator map.
- Editing requires toggling edit mode, creating features, snapping, saving and validating geometry.

### Definitions to reproduce

> Georeferencing is the process of assigning real-world coordinates to a raster image or map so it aligns with a known coordinate system.

> Metadata is data about data: it describes the content, source, quality, projection and ownership of a dataset.

## Last 24 hours

1. Write the vector-versus-raster comparison as a table.
2. State the four kinds of projection distortion and match each to a projection family.
3. Convert one latitude–longitude pair to a UTM zone description.
4. List the overlay operations and say what each keeps.
5. Rehearse the QGIS sequence for adding a layer, setting the CRS and producing a layout.
6. List five data-quality dimensions and one check for each.

## Question bank

No GIS question can be reproduced from this repository. The four PDFs under `material/GIS/` are Green IT and Sustainability (BCS456A) MCQ sets — `MCQ Module 1_GIT.pdf`, `Mcqs on 2nd Module_GIT6.pdf`, `MCQ Module 3_GIT.pdf` and `4th and 5th Module MCQs.docx.pdf` — not GIS papers. Their text extracts cleanly, so they are misfiled rather than scanned. No GIS marks or question types are available here.

*Source: `gis/README.md` only. The question-bank note records what the four `material/GIS/` PDFs actually contain.*
