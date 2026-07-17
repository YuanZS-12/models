#bearing-review.json
{
  "schema_version": 2,
  "server": "dc_mcp_server",
  "runtime_mode": "mcp_review",
  "tools": [
    "dc_lookup_pattern",
    "dc_search",
    "dc_semantic_search",
    "dc_get_api_info",
    "dc_list_namespace"
  ],
  "facts": [
    "NXOpen.Session.GetSession() returns singleton Session; Session.DexManager returns DexManager for STEP import/export",
    "NXOpen.PartCollection.Work returns current work Part; PartCollection.NewDisplay(name, units) creates new .prt part; Part.Units inherits from BasePart.Units enum with members: Inches, Millimeters, Mix, Meters, Micrometers",
    "NXOpen.Part is subclass of BasePart; BasePart.SaveAs(new_file_name) -> PartSaveStatus creates copy of target part; BasePart.Save() saves part",
    "NXOpen.Features.FeatureCollection.CreateBlockFeatureBuilder(None) -> BlockFeatureBuilder; SetOriginAndLengths(origin_point, length, width, height) creates block; uses CommitFeature() and Destroy()",
    "NXOpen.Features.FeatureCollection.CreateCylinderBuilder(None) -> CylinderBuilder; properties: Type (Types enum: AxisDiameterAndHeight, ArcAndHeight), Origin, Direction, Diameter (Expression), Height (Expression); uses CommitFeature() and Destroy()",
    "NXOpen.Features.FeatureCollection.CreateBooleanBuilder(None) -> BooleanBuilder; Operation property uses Feature.BooleanType enum (Unite, Subtract); Target property accepts Body; Tool property accepts DisplayableObject; uses CommitFeature() and Destroy()",
    "NXOpen.Features.FeatureCollection.CreateChamferBuilder(None) -> ChamferBuilder; ChamferOption enum: SymmetricOffsets, TwoOffsets, OffsetAndAngle; FirstOffset is str (settable); uses CommitFeature() and Destroy()",
    "NXOpen.Features.FeatureCollection.CreateEdgeBlendBuilder(None) -> EdgeBlendBuilder; AddChainset(collector, radius) adds edge blend chainset; AddConstantRadiusEdge is not a property but AddChainset is the primary method; uses CommitFeature() and Destroy()",
    "NXOpen.DexManager.CreateStepCreator() -> StepCreator; StepCreator properties: ExportAs (ExportAsOption enum: Ap203, Ap214, Ap242, Ap242ED2), ExportFrom (ExportFromOption enum: DisplayPart, ExistingPart), FileSaveFlag (bool), InputFile (str), OutputFile is inherited; ObjectTypes has Solids filter; uses Commit() and Destroy()",
    "NXOpen.StepCreator.ExportAsOption enum members: Ap203, Ap214, Ap242, Ap242ED2",
    "NXOpen.StepCreator.ExportFromOption enum members: DisplayPart, ExistingPart",
    "NXOpen.BaseCreator.ExportDestinationOption (referenced in builder.py _set_export_destination_to_file) used for ExportDestination property",
    "ChamferBuilder uses ScCollector via SmartCollector or Collector property for edge selection; CreateRuleEdgeDumb for edge rule creation"
  ],
  "target_nx_version": "NX 2606",
  "probe": "nx_benchmark_bearing_housing"
}
