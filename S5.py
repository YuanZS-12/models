#review-evidence-01.json
{
  "server": "dc_mcp_server",
  "tools": [
    "dc_lookup_pattern",
    "dc_get_api_info",
    "dc_run_snippet"
  ],
  "facts": [
    "NXOpen.PartCollection.NewDisplay creates a new displayable part in NX 2606; returns tuple (part, status)",
    "NXOpen.Part.Units.Millimeters is the unit specifier for mm-based parts",
    "NXOpen.Session.GetSession() retrieves the active NX session",
    "work_part.Save(BasePart.SaveComponents.TrueValue, BasePart.CloseAfterSave.FalseValue) saves the part with its components",
    "NewDisplay accepts path+name without .prt extension; NX appends it automatically",
    "the newly created display part becomes the active work part after NewDisplay; the session work part accessor returns it",
    "no known incompatibilities for NXOpen.PartCollection.NewDisplay in NX 2606"
  ]
}
#review-evidence-06.json
{
  "server": "dc_mcp_server",
  "tools": [
    "dc_lookup_pattern",
    "dc_get_api_info",
    "dc_run_snippet"
  ],
  "facts": [
    "NXOpen.Features.FreeformSurfaceCollection.CreateSweptBuilder1 creates a SweptBuilder1 for freeform surface/solid operations",
    "SweptBuilder1.BodyPreference.BodyType accepts NXOpen.GeometricUtilities.FeatureOptions.BodyStyle.Solid for solid output",
    "SweptBuilder1.SectionList.Append accepts an ordered list of Section objects for multiple sections",
    "SweptBuilder1.GuideList.Append accepts one or more guide Section objects",
    "SweptBuilder1.OrientationMethod.OrientationOption accepts Fixed for fixed orientation along guide",
    "closed_rectangle_section creates a rectangular Section at a given Z with width/height",
    "line_section creates a linear Section between two Point3d coordinates",
    "Section-to-guide correspondence is established by matching the order of points in sections and guides",
    "CommitFeature on SweptBuilder1 returns the committed feature; Destroy must be called in finally block",
    "known verified recipe nx2606.sweep.two-sections with status=verified in api-recipes registry"
  ]
}
