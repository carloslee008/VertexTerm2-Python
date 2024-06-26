import unreal

AssetTools = unreal.AssetToolsHelpers.get_asset_tools()
MaterialEditLibrary = unreal.MaterialEditingLibrary
EditorAssetLibrary = unreal.EditorAssetLibrary


#Create New Material
MeshPaintMaterial = AssetTools.create_asset("M_MeshPaint", "/Game/MasterMaterials", unreal.Material, unreal.MaterialFactoryNew())

#Add Texture Params for each surface
base_colors = []
normals = []
orm = []

#Create Vertex Color Nodes

NodePositionX = -500
NodePositionY = -250

VertexColorNode_Color = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionVertexColor.static_class(), NodePositionX * 6, NodePositionY)
VertexColorNode_Color.set_editor_property('Desc', 'Base_Color')

VertexColorNode_Normal = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionVertexColor.static_class(), NodePositionX * 6, NodePositionY * 0)
VertexColorNode_Normal.set_editor_property('Desc', 'Normal')

VertexColorNode_R = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionVertexColor.static_class(), NodePositionX * 6, NodePositionY * -1)
VertexColorNode_R.set_editor_property('Desc', 'R_Occlusion')

VertexColorNode_G = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionVertexColor.static_class(), NodePositionX * 6, NodePositionY * -2)
VertexColorNode_G.set_editor_property('Desc', 'Roughness')

VertexColorNode_B = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionVertexColor.static_class(), NodePositionX * 6, NodePositionY * -3)
VertexColorNode_B.set_editor_property('Desc', 'Metallic')

#Create One Minus Nodes

OneMinusNodeColor = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionOneMinus.static_class(), NodePositionX * 5, NodePositionY)
OneMinusNodeNormal = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionOneMinus.static_class(), NodePositionX * 5, NodePositionY * 0)
OneMinusNode_R = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionOneMinus.static_class(), NodePositionX * 5, NodePositionY * -1)
OneMinusNode_G = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionOneMinus.static_class(), NodePositionX * 5, NodePositionY * -2)
OneMinusNode_B = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionOneMinus.static_class(), NodePositionX * 5, NodePositionY * -3)

#Create Base Color, Normal and Orm Texture Parameters

for i in range(5):
    #Create Texture Params
    BaseColorParam = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionTextureSampleParameter2D.static_class(), NodePositionX * 6, NodePositionY * -i + 1000)
    NormalParam = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionTextureSampleParameter2D.static_class(), NodePositionX * 5, NodePositionY * -i + 1000)
    ORMParam = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionTextureSampleParameter2D.static_class(), NodePositionX * 4, NodePositionY * -i + 1000)

    #Set names and sample types
    BaseColorParam.set_editor_property("ParameterName", unreal.Name("BaseColor_{}".format(i)))
    BaseColorParam.set_editor_property("sampler_source", unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)

    NormalParam.set_editor_property("ParameterName", unreal.Name("Normal_{}".format(i)))
    NormalParam.set_editor_property("sampler_source", unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
    NormalParam.set_editor_property("sampler_type", unreal.MaterialSamplerType.SAMPLERTYPE_NORMAL)

    ORMParam.set_editor_property("ParameterName", unreal.Name("ORM_{}".format(i)))
    ORMParam.set_editor_property("sampler_source", unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
    ORMParam.set_editor_property("sampler_type", unreal.MaterialSamplerType.SAMPLERTYPE_LINEAR_COLOR)

    #Append parameters to their arrays
    base_colors.append(BaseColorParam)
    normals.append(NormalParam)
    orm.append(ORMParam)

#Define lerp arrays
base_color_lerps = []
normal_lerps = []
orm_r_lerps = []
orm_g_lerps = []
orm_b_lerps = []

for i in range(5):
    base_color_lerp = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionLinearInterpolate.static_class(), NodePositionX * -i/2 - 1600, NodePositionY)
    normal_lerp = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionLinearInterpolate.static_class(), NodePositionX * -i/2 - 1600, NodePositionY + 250)
    orm_r_lerp = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionLinearInterpolate.static_class(), NodePositionX * -i/2 -1600, NodePositionY + 500)
    orm_g_lerp = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionLinearInterpolate.static_class(), NodePositionX * -i/2 -1600, NodePositionY + 750)
    orm_b_lerp = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionLinearInterpolate.static_class(), NodePositionX * -i/2 -1600, NodePositionY + 1000)

    base_color_lerps.append(base_color_lerp)
    normal_lerps.append(normal_lerp)
    orm_r_lerps.append(orm_r_lerp)
    orm_g_lerps.append(orm_g_lerp)
    orm_b_lerps.append(orm_b_lerp)


#Connect Base Color Connections

#Connect Base Color Params to Lerps

MaterialEditLibrary.connect_material_expressions(base_colors[0], '', base_color_lerps[0], 'B')
MaterialEditLibrary.connect_material_expressions(base_colors[1], '', base_color_lerps[1], 'B')
MaterialEditLibrary.connect_material_expressions(base_colors[2], '', base_color_lerps[2], 'B')
MaterialEditLibrary.connect_material_expressions(base_colors[3], '', base_color_lerps[3], 'B')
MaterialEditLibrary.connect_material_expressions(base_colors[4], '', base_color_lerps[4], 'B')
MaterialEditLibrary.connect_material_expressions(base_colors[4], '', base_color_lerps[0], 'A')
MaterialEditLibrary.connect_material_expressions(OneMinusNodeColor, '', base_color_lerps[0], 'Alpha')

#Connect Vertex Color Node to Base Color Lerps
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Color, 'A', OneMinusNodeColor, '')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Color, 'R', base_color_lerps[1], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Color, 'G', base_color_lerps[2], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Color, 'B', base_color_lerps[3], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Color, 'A', base_color_lerps[4], 'Alpha')

#Make Lerp Connections
MaterialEditLibrary.connect_material_expressions(base_color_lerps[0], '', base_color_lerps[1], 'A')
MaterialEditLibrary.connect_material_expressions(base_color_lerps[1], '', base_color_lerps[2], 'A')
MaterialEditLibrary.connect_material_expressions(base_color_lerps[2], '', base_color_lerps[3], 'A')
MaterialEditLibrary.connect_material_expressions(base_color_lerps[3], '', base_color_lerps[4], 'A')

#Connect Last Lerp to the Base Color Channel
MaterialEditLibrary.connect_material_property(base_color_lerps[4], '', unreal.MaterialProperty.MP_BASE_COLOR)

#Make Normal Map Connections

#Connect Normal Color Params to Lerps

MaterialEditLibrary.connect_material_expressions(normals[0], '', normal_lerps[0], 'B')
MaterialEditLibrary.connect_material_expressions(normals[1], '', normal_lerps[1], 'B')
MaterialEditLibrary.connect_material_expressions(normals[2], '', normal_lerps[2], 'B')
MaterialEditLibrary.connect_material_expressions(normals[3], '', normal_lerps[3], 'B')
MaterialEditLibrary.connect_material_expressions(normals[4], '', normal_lerps[4], 'B')
MaterialEditLibrary.connect_material_expressions(normals[4], '', normal_lerps[0], 'A')
MaterialEditLibrary.connect_material_expressions(OneMinusNodeNormal, '', normal_lerps[0], 'Alpha')

#Connect Vertex Color Node to Normal Lerps
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Normal, 'A', OneMinusNodeNormal, '')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Normal, 'R', normal_lerps[1], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Normal, 'G', normal_lerps[2], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Normal, 'B', normal_lerps[3], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Normal, 'A', normal_lerps[4], 'Alpha')

#Make Lerp Connections
MaterialEditLibrary.connect_material_expressions(normal_lerps[0], '', normal_lerps[1], 'A')
MaterialEditLibrary.connect_material_expressions(normal_lerps[1], '', normal_lerps[2], 'A')
MaterialEditLibrary.connect_material_expressions(normal_lerps[2], '', normal_lerps[3], 'A')
MaterialEditLibrary.connect_material_expressions(normal_lerps[3], '', normal_lerps[4], 'A')

#Connect Last Lerp to the Base Color Channel
MaterialEditLibrary.connect_material_property(normal_lerps[4], '', unreal.MaterialProperty.MP_NORMAL)

#Make Ambient Occlusion Connections

#Connect ORM Red Channel Params to Lerps

MaterialEditLibrary.connect_material_expressions(orm[0], 'R', orm_r_lerps[0], 'B')
MaterialEditLibrary.connect_material_expressions(orm[1], 'R', orm_r_lerps[1], 'B')
MaterialEditLibrary.connect_material_expressions(orm[2], 'R', orm_r_lerps[2], 'B')
MaterialEditLibrary.connect_material_expressions(orm[3], 'R', orm_r_lerps[3], 'B')
MaterialEditLibrary.connect_material_expressions(orm[4], 'R', orm_r_lerps[4], 'B')
MaterialEditLibrary.connect_material_expressions(orm[4], 'R', orm_r_lerps[0], 'A')
MaterialEditLibrary.connect_material_expressions(OneMinusNode_R, '', orm_r_lerps[0], 'Alpha')

#Connect Vertex Color Node to ORM_R Lerps
MaterialEditLibrary.connect_material_expressions(VertexColorNode_R, 'A', OneMinusNode_R, '')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_R, 'R', orm_r_lerps[1], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_R, 'G', orm_r_lerps[2], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_R, 'B', orm_r_lerps[3], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_R, 'A', orm_r_lerps[4], 'Alpha')

#Make Lerp Connections
MaterialEditLibrary.connect_material_expressions(orm_r_lerps[0], '', orm_r_lerps[1], 'A')
MaterialEditLibrary.connect_material_expressions(orm_r_lerps[1], '', orm_r_lerps[2], 'A')
MaterialEditLibrary.connect_material_expressions(orm_r_lerps[2], '', orm_r_lerps[3], 'A')
MaterialEditLibrary.connect_material_expressions(orm_r_lerps[3], '', orm_r_lerps[4], 'A')

#Connect Last Lerp to the Base Color Channel
MaterialEditLibrary.connect_material_property(orm_r_lerps[4], '', unreal.MaterialProperty.MP_AMBIENT_OCCLUSION)

#Make Roughness Connections

#Connect ORM Green Channel Params to Lerps
MaterialEditLibrary.connect_material_expressions(orm[0], 'G', orm_g_lerps[0], 'B')
MaterialEditLibrary.connect_material_expressions(orm[1], 'G', orm_g_lerps[1], 'B')
MaterialEditLibrary.connect_material_expressions(orm[2], 'G', orm_g_lerps[2], 'B')
MaterialEditLibrary.connect_material_expressions(orm[3], 'G', orm_g_lerps[3], 'B')
MaterialEditLibrary.connect_material_expressions(orm[4], 'G', orm_g_lerps[4], 'B')
MaterialEditLibrary.connect_material_expressions(orm[4], 'G', orm_g_lerps[0], 'A')
MaterialEditLibrary.connect_material_expressions(OneMinusNode_G, '', orm_g_lerps[0], 'Alpha')

#Connect Vertex Color Node to ORM_G Lerps
MaterialEditLibrary.connect_material_expressions(VertexColorNode_G, 'A', OneMinusNode_G, '')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_G, 'R', orm_g_lerps[1], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_G, 'G', orm_g_lerps[2], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_G, 'B', orm_g_lerps[3], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_G, 'A', orm_g_lerps[4], 'Alpha')

#Make Lerp Connections
MaterialEditLibrary.connect_material_expressions(orm_g_lerps[0], '', orm_g_lerps[1], 'A')
MaterialEditLibrary.connect_material_expressions(orm_g_lerps[1], '', orm_g_lerps[2], 'A')
MaterialEditLibrary.connect_material_expressions(orm_g_lerps[2], '', orm_g_lerps[3], 'A')
MaterialEditLibrary.connect_material_expressions(orm_g_lerps[3], '', orm_g_lerps[4], 'A')

#Connect Last Lerp to the Base Color Channel
MaterialEditLibrary.connect_material_property(orm_g_lerps[4], '', unreal.MaterialProperty.MP_ROUGHNESS)

#Make Matllic Connections

#Connect ORM Blue Channel Params to Lerps
MaterialEditLibrary.connect_material_expressions(orm[0], 'B', orm_b_lerps[0], 'B')
MaterialEditLibrary.connect_material_expressions(orm[1], 'B', orm_b_lerps[1], 'B')
MaterialEditLibrary.connect_material_expressions(orm[2], 'B', orm_b_lerps[2], 'B')
MaterialEditLibrary.connect_material_expressions(orm[3], 'B', orm_b_lerps[3], 'B')
MaterialEditLibrary.connect_material_expressions(orm[4], 'B', orm_b_lerps[4], 'B')
MaterialEditLibrary.connect_material_expressions(orm[4], 'B', orm_b_lerps[0], 'A')
MaterialEditLibrary.connect_material_expressions(OneMinusNode_B, '', orm_b_lerps[0], 'Alpha')

#Connect Vertex Color Node to ORM_B Lerps
MaterialEditLibrary.connect_material_expressions(VertexColorNode_B, 'A', OneMinusNode_B, '')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_B, 'R', orm_b_lerps[1], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_B, 'G', orm_b_lerps[2], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_B, 'B', orm_b_lerps[3], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_B, 'A', orm_b_lerps[4], 'Alpha')

#Make Lerp Connections
MaterialEditLibrary.connect_material_expressions(orm_b_lerps[0], '', orm_b_lerps[1], 'A')
MaterialEditLibrary.connect_material_expressions(orm_b_lerps[1], '', orm_b_lerps[2], 'A')
MaterialEditLibrary.connect_material_expressions(orm_b_lerps[2], '', orm_b_lerps[3], 'A')
MaterialEditLibrary.connect_material_expressions(orm_b_lerps[3], '', orm_b_lerps[4], 'A')

#Connect Last Lerp to the Base Color Channel
MaterialEditLibrary.connect_material_property(orm_b_lerps[4], '', unreal.MaterialProperty.MP_METALLIC)

#Create Material Instance
MeshPaintInstance = AssetTools.create_asset("MeshPaintInstance", "/Game/masterMaterials", unreal.MaterialInstanceConstant, unreal.MaterialInstanceConstantFactoryNew())
#MaterialEditLibrary.set_material_instance_parent(MeshPaintInstance, MeshPaintMaterial)
MeshPaintInstance.set_editor_property("Parent", MeshPaintMaterial)
MaterialEditLibrary.update_material_instance(MeshPaintInstance)

#Save Material and Instance
EditorAssetLibrary.save_asset("/Game/masterMaterials/M_MeshPaint", True)
EditorAssetLibrary.save_asset("/Game/masterMaterials/MeshPaintInstance", True)
