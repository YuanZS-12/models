#01_create_part.dc_result.md
# Journal Execution Result
**Journal:** `C:\Users\z004n36r\.agents\nx_mcp_runs\integration_002\01_create_part.py`
**Exit code:** `TIMEOUT`
**Duration:** 90.03 s
**Working directory:** `C:\Users\z004n36r\.agents\nx_mcp_runs\integration_002`

*No new output files detected.*

> **WARNING:** Journal exceeded the 90 s timeout and was terminated.

## Diagnostics
- License-related failure signals were detected.
- SPLM_LICENSE_SERVER: `cloud`
- UGII_LICENSE_FILE: `27000@shappdctclnx1,27000@shlv6002`
- UGS_LICENSE_BUNDLE: `<not set>`
- UGII_BASE_DIR: `D:\Workdir\iproot\nx2606.1700\test44\wntx64\kits`
- Resolved run_journal.exe: `D:\Workdir\iproot\nx2606.1700\test44\wntx64\kits\nxbin\run_journal.exe`
- Candidate run_journal.exe paths:
  - `D:\Workdir\iproot\nx2606.1700\test44\wntx64\kits\nxbin\run_journal.exe`


#01-api-review.md
# Probe 01 — API Review
## dc_lookup_pattern: query="create new part", limit=3

# Designcenter journal Patterns matching: `create new part`

## 1. Creating a new NX part file in a headless journal *(score: 14)*
**Solution:** Use theSession.Parts.NewDisplay(path, NXOpen.Part.Units.Millimeters). PartCollection has NO NewPart method  --  it does not exist.

```python
workPart = theSession.Parts.NewDisplay('C:/Temp/my.prt', NXOpen.Part.Units.Millimeters)
```

## 2. theSession.Parts.NewDisplay() throws NXException 'File already exists' if the output .prt path already exists on disk *(score: 12)*
**Solution:** CONFIRMED: Parts.NewDisplay(path, ...) raises NXException with message 'File already exists' when the target .prt file is present  --  it does NOT silently overwrite. Delete the file first with os.remove(). Wrap in an existence check to avoid FileNotFoundError on first run.

```python
import os
OUTPUT_PART = 'C:/Temp/my_model.prt'
# CRITICAL: NewDisplay fails if file already exists
if os.path.exists(OUTPUT_PART):
    os.remove(OUTPUT_PART)
workPart = theSession.Parts.NewDisplay(
    OUTPUT_PART,
    NXOpen.Part.Units.Millimeters  # second arg = units, NOT DisplayPartOption
)
```

## 3. Creating a new part using the FileNew builder with a template (more powerful than Parts.NewDisplay) *(score: 12)*
**Solution:** Use theSession.Parts.FileNew() to get a builder, configure TemplateFileName, ApplicationName, Units, NewFileName, then Commit(). CRITICAL: FileNew inherits from Builder, NOT FeatureBuilder  --  use Commit() not CommitFeature(). CommitFeature() raises AttributeError. Commit() returns the Part object directly. ApplicationName must be a valid registered name (e.g., 'ModelTemplate', 'AssemblyTemplate', 'DrawingTemplate')  --  use GetApplicationNames() to list them. TemplateFileName must match an available template (e.g., 'model-plain-1-mm-template.prt')  --  use GetAvailableTemplates() to list them. Same file-exists behavior as NewDisplay  --  fails if output path already exists. UseBlankTemplate=True with TemplateType=Item throws 'The selected template does not exist'  --  templates are required for FileNew.

```python
import NXOpen
import os

def main():
    theSession = NXOpen.Session.GetSession()
    
    output_path = 'C:/Temp/my_template_part.prt'
    if os.path.exists(output_path):
        os.remove(output_path)
    
    fileNew = theSession.Parts.FileNew()
    
    # Configure template-based creation
    fileNew.TemplateFileName = 'model-plain-1-mm-template.prt'
    fileNew.UseBlankTemplate = False
    fileNew.ApplicationName = 'ModelTemplate'
    fileNew.Units = NXOpen.Part.Units.Millimeters
    fileNew.NewFileName = output_path
    fileNew.MakeDisplayedPart = True
    fileNew.TemplateType = NXOpen.FileNewTemplateType.Item
    
    # CRITICAL: Use Commit(), NOT CommitFeature()  --  FileNew is a Builder, not FeatureBuilder
    # CommitFeature() raises AttributeError: 'NXOpen.FileNew' object has no attribute 'CommitFeature'
    nxObj = fileNew.Commit()  # Returns the Part object
    fileNew.Destroy()
    
    workPart = theSession.Parts.Work
    print(f'Created: {workPart.Leaf}, Units: {workPart.PartUnits}')
    
    # To discover available templates and application names:
    # fileNew2 = theSession.Parts.FileNew()
    # templates = fileNew2.GetAvailableTemplates()  # List[str] of template filenames
    # appNames = fileNew2.GetApplicationNames()      # List[str] of valid app names
    # fileNew2.Destroy()

if __name__ == '__main__':
    main()
```

---

## dc_get_api_info: info_type="method", class_name="NXOpen.PartCollection", method_name="NewDisplay"

# NewDisplay Method
**Class:** `NXOpen.PartCollection`
**Signature:** `NewDisplay(name: str, units: Part.Units) -> Part`
**Category:** Collections
**Description:** Creates a new .prt part and sets this part as the active display part. Note: This method should only be used to create new .prt parts. Use NXOpen.PartCollection.NewBaseDisplay to create other types of parts other than .prt parts.
**Parameters:** 2
  - `name: str`
  - `units: Part.Units`
**Return Type:** `Part`
**Usage Patterns:**
  - `obj.NewDisplay()`

## dc_get_api_info: info_type="class", class_name="NXOpen.Part", property_filter="Units"

# Part
**Full name:** `NXOpen.Part`
**Module:** `NXOpen`
**Category:** General
**Description:** Represents an NX part of type .prt.
**Inherits from:** `NXOpen.BasePart`, `NXOpen.NXObject`, `NXOpen.TaggedObject`, `object`

## Methods (44 — omitted while property_filter is active)

## Properties (0 of 86 match 'Units' — try a different prefix)

## Nested Types (6)
### `NXOpen.Part.PartFamilyAttrType` *(enum)*
  Members Include: |TextType| text attribute |NumericType| numeric attribute |IntegerType| integer attribute |DoubleType| double attribute |StringType| string attribute |PartType| part attribute |NameType| name attribute |InstanceType| instance attribute |ExpressionType| expression attribute |MirrorType| mirror attribute |DensityType| density attribute |FeatureType| feature attribute
  **Members:** `TextType`, `NumericType`, `IntegerType`, `DoubleType`, `StringType`, `PartType`, `NameType`, `InstanceType`, `ExpressionType`, `MirrorType`, `DensityType`, `FeatureType`
### `NXOpen.Part.Relations` *(enum)*
  Members Include: |Standalone| no master model support |ReferenceExisting| Master model support |Mix| support any one of relation
  **Members:** `Standalone`, `ReferenceExisting`, `Mix`
### `NXOpen.Part.Units` *(enum)*
  Members Include: |Inches| |Millimeters| |Mix| |Meters| |Micrometers|
  **Members:** `Inches`, `Millimeters`, `Mix`, `Meters`, `Micrometers`
### `NXOpen.Part.UpdateFromJtFileOptions` *(enum)*
  Members Include: |Default| update geometry in JT Derived part from input JT file.
  **Members:** `Default`
### `NXOpen.Part.FeatureUpdateStatus` *(class)*
  Contains feature update status report PartFeatureUpdateStatus_Struct NX is an alias for Part.FeatureUpdateStatus NX.
  **Members:** *(no members)*
### `NXOpen.Part.PartFamilyAttributeData` *(class)*
  Contains part family attributes information PartPartFamilyAttributeData_Struct NX is an alias for Part.PartFamilyAttributeData NX.
  **Members:** *(no members)*

## dc_get_api_info: info_type="method", class_name="NXOpen.BasePart", method_name="Save"

# Save Method
**Class:** `NXOpen.BasePart`
**Signature:** `Save(self, save_component_parts: BasePart.SaveComponents, close: BasePart.CloseAfterSave) -> PartSaveStatus`
**Category:** General
**Description:** Saves the part whether it is modified or not.
**Parameters:** 3
  - `self`
  - `save_component_parts: BasePart.SaveComponents`
  - `close: BasePart.CloseAfterSave`
**Return Type:** `PartSaveStatus`
**Usage Patterns:**
  - `obj.Save()`
#01-review-evidence-01.json
