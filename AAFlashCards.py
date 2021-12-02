import cPickle, base64
try:
	from SimpleSession.versions.v65 import beginRestore,\
	    registerAfterModelsCB, reportRestoreError, checkVersion
except ImportError:
	from chimera import UserError
	raise UserError('Cannot open session that was saved in a'
	    ' newer version of Chimera; update your version')
checkVersion([1, 15, 42209])
import chimera
from chimera import replyobj
replyobj.status('Restoring session...', \
    blankAfter=0)
replyobj.status('Beginning session restore...', \
    blankAfter=0, secondary=True)
beginRestore()

def restoreCoreModels():
	from SimpleSession.versions.v65 import init, restoreViewer, \
	     restoreMolecules, restoreColors, restoreSurfaces, \
	     restoreVRML, restorePseudoBondGroups, restoreModelAssociations
	molInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVRFyaWJib25JbnNpZGVDb2xvcnECSwFOfYdVCWJhbGxTY2FsZXEDSwFHP9AAAAAAAAB9h1UJcG9pbnRTaXplcQRLAUc/8AAAAAAAAH2HVQVjb2xvcnEFSwFLAH2HVQpyaWJib25UeXBlcQZLAUsAfYdVCnN0aWNrU2NhbGVxB0sBRz/wAAAAAAAAfYdVDG1tQ0lGSGVhZGVyc3EIXXEJTmFVDGFyb21hdGljTW9kZXEKSwFLAX2HVQp2ZHdEZW5zaXR5cQtLAUdAFAAAAAAAAH2HVQZoaWRkZW5xDEsBiX2HVQ1hcm9tYXRpY0NvbG9ycQ1LAU59h1UPcmliYm9uU21vb3RoaW5ncQ5LAUsAfYdVCWF1dG9jaGFpbnEPSwGIfYdVCnBkYlZlcnNpb25xEEsBSwB9h1UIb3B0aW9uYWxxEX1VD2xvd2VyQ2FzZUNoYWluc3ESSwGJfYdVCWxpbmVXaWR0aHETSwFHP/AAAAAAAAB9h1UPcmVzaWR1ZUxhYmVsUG9zcRRLAUsAfYdVBG5hbWVxFUsBWAcAAABzY3JhdGNofYdVD2Fyb21hdGljRGlzcGxheXEWSwGJfYdVD3JpYmJvblN0aWZmbmVzc3EXSwFHP+mZmZmZmZp9h1UKcGRiSGVhZGVyc3EYXXEZfXEaYVUDaWRzcRtLAUsASwCGfYdVDnN1cmZhY2VPcGFjaXR5cRxLAUe/8AAAAAAAAH2HVRBhcm9tYXRpY0xpbmVUeXBlcR1LAUsCfYdVFHJpYmJvbkhpZGVzTWFpbmNoYWlucR5LAYh9h1UHZGlzcGxheXEfSwGIfYd1Lg=='))
	resInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQZpbnNlcnRxAksWVQEgfYdVC2ZpbGxEaXNwbGF5cQNLFol9h1UEbmFtZXEESxZYAwAAAEFMQX1xBShYAwAAAENZU11xBksCYVgDAAAAQVNQXXEHSwNhWAMAAABTRVJdcQhLEGFYAwAAAEFTTl1xCUsMYVgDAAAAR0xOXXEKSw5hWAMAAABMWVNdcQtLCWFYAwAAAElMRV1xDEsIYVgDAAAAUFJPXXENSw1hWAMAAABUSFJdcQ5LEWFYAwAAAFBIRV1xD0sFYVgDAAAAR0xZXXEQSwZhWAMAAABISVNdcRFLB2FYAwAAAExFVV1xEksKYVgDAAAAQVJHXXETSw9hWAMAAABUUlBdcRRLE2FYAwAAAFZBTF1xFUsSYVgDAAAAR0xVXXEWSwRhWAMAAABUWVJdcRdLFGFYAwAAAE1FVF1xGEsLYXWHVQVjaGFpbnEZSxZYAQAAAEF9h1UOcmliYm9uRHJhd01vZGVxGksWSwJ9h1UCc3NxG0sWiYmGfYdVCG1vbGVjdWxlcRxLFksAfYdVC3JpYmJvbkNvbG9ycR1LFksBfYdVBWxhYmVscR5LFlgAAAAAfYdVCmxhYmVsQ29sb3JxH0sWSwF9h1UIZmlsbE1vZGVxIEsWSwF9h1UFaXNIZXRxIUsWiX2HVQtsYWJlbE9mZnNldHEiSxZOfYdVCHBvc2l0aW9ucSNdcSRLAUsWhnElYVUNcmliYm9uRGlzcGxheXEmSxaJfYdVCG9wdGlvbmFscSd9VQRzc0lkcShLFkr/////fYd1Lg=='))
	atomInfo = cPickle.loads(base64.b64decode('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'))
	bondInfo = cPickle.loads(base64.b64decode('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'))
	crdInfo = cPickle.loads(base64.b64decode('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'))
	surfInfo = {'category': (0, None, {}), 'probeRadius': (0, None, {}), 'pointSize': (0, None, {}), 'name': [], 'density': (0, None, {}), 'colorMode': (0, None, {}), 'useLighting': (0, None, {}), 'transparencyBlendMode': (0, None, {}), 'molecule': [], 'smoothLines': (0, None, {}), 'lineWidth': (0, None, {}), 'allComponents': (0, None, {}), 'twoSidedLighting': (0, None, {}), 'customVisibility': [], 'drawMode': (0, None, {}), 'display': (0, None, {}), 'customColors': []}
	vrmlInfo = {'subid': (0, None, {}), 'display': (0, None, {}), 'id': (0, None, {}), 'vrmlString': [], 'name': (0, None, {})}
	colors = {u'Ru': ((0.141176, 0.560784, 0.560784), 1, u'default'), u'Re': ((0.14902, 0.490196, 0.670588), 1, u'default'), u'Rf': ((0.8, 0, 0.34902), 1, u'default'), u'Ra': ((0, 0.490196, 0), 1, u'default'), u'Rb': ((0.439216, 0.180392, 0.690196), 1, u'default'), u'Rn': ((0.258824, 0.509804, 0.588235), 1, u'default'), u'Rh': ((0.0392157, 0.490196, 0.54902), 1, u'default'), u'Be': ((0.760784, 1, 0), 1, u'default'), u'Ba': ((0, 0.788235, 0), 1, u'default'), u'Bh': ((0.878431, 0, 0.219608), 1, u'default'), u'Bi': ((0.619608, 0.309804, 0.709804), 1, u'default'), u'Bk': ((0.541176, 0.309804, 0.890196), 1, u'default'), u'Br': ((0.65098, 0.160784, 0.160784), 1, u'default'), u'H': ((1, 1, 1), 1, u'default'), u'P': ((1, 0.501961, 0), 1, u'default'), u'Os': ((0.14902, 0.4, 0.588235), 1, u'default'), u'Es': ((0.701961, 0.121569, 0.831373), 1, u'default'), u'Hg': ((0.721569, 0.721569, 0.815686), 1, u'default'), u'Ge': ((0.4, 0.560784, 0.560784), 1, u'default'), u'Gd': ((0.270588, 1, 0.780392), 1, u'default'), u'Ga': ((0.760784, 0.560784, 0.560784), 1, u'default'), u'Pr': ((0.85098, 1, 0.780392), 1, u'default'),
u'slate gray': ((0.439216, 0.501961, 0.564706), 1, u'default'), u'Pt': ((0.815686, 0.815686, 0.878431), 1, u'default'), u'Pu': ((0, 0.419608, 1), 1, u'default'), u'C': ((0.564706, 0.564706, 0.564706), 1, u'default'), u'Pb': ((0.341176, 0.34902, 0.380392), 1, u'default'), u'Pa': ((0, 0.631373, 1), 1, u'default'), u'Pd': ((0, 0.411765, 0.521569), 1, u'default'), u'Cd': ((1, 0.85098, 0.560784), 1, u'default'), u'Po': ((0.670588, 0.360784, 0), 1, u'default'), u'Pm': ((0.639216, 1, 0.780392), 1, u'default'), u'Hs': ((0.901961, 0, 0.180392), 1, u'default'), u'Ho': ((0, 1, 0.611765), 1, u'default'), u'Hf': ((0.301961, 0.760784, 1), 1, u'default'), u'K': ((0.560784, 0.25098, 0.831373), 1, u'default'), u'He': ((0.85098, 1, 1), 1, u'default'), u'Md': ((0.701961, 0.0509804, 0.65098), 1, u'default'), u'Mg': ((0.541176, 1, 0), 1, u'default'), u'Mo': ((0.329412, 0.709804, 0.709804), 1, u'default'), u'Mn': ((0.611765, 0.478431, 0.780392), 1, u'default'), u'O': ((1, 0.0509804, 0.0509804), 1, u'default'), u'Mt': ((0.921569, 0, 0.14902), 1, u'default'), u'S': ((1, 1, 0.188235), 1, u'default'),
u'W': ((0.129412, 0.580392, 0.839216), 1, u'default'), u'Zn': ((0.490196, 0.501961, 0.690196), 1, u'default'), u'Eu': ((0.380392, 1, 0.780392), 1, u'default'), u'Zr': ((0.580392, 0.878431, 0.878431), 1, u'default'), u'Er': ((0, 0.901961, 0.458824), 1, u'default'), u'Ni': ((0.313725, 0.815686, 0.313725), 1, u'default'), u'No': ((0.741176, 0.0509804, 0.529412), 1, u'default'), u'Na': ((0.670588, 0.360784, 0.94902), 1, u'default'), u'Nb': ((0.45098, 0.760784, 0.788235), 1, u'default'), u'Nd': ((0.780392, 1, 0.780392), 1, u'default'), u'Ne': ((0.701961, 0.890196, 0.960784), 1, u'default'), u'Np': ((0, 0.501961, 1), 1, u'default'), u'Fr': ((0.258824, 0, 0.4), 1, u'default'), u'Fe': ((0.878431, 0.4, 0.2), 1, u'default'), u'Fm': ((0.701961, 0.121569, 0.729412), 1, u'default'), u'B': ((1, 0.709804, 0.709804), 1, u'default'), u'F': ((0.564706, 0.878431, 0.313725), 1, u'default'), u'Sr': ((0, 1, 0), 1, u'default'), u'N': ((0.188235, 0.313725, 0.972549), 1, u'default'), u'Kr': ((0.360784, 0.721569, 0.819608), 1, u'default'), u'Si': ((0.941176, 0.784314, 0.627451), 1, u'default'),
u'Sn': ((0.4, 0.501961, 0.501961), 1, u'default'), u'Sm': ((0.560784, 1, 0.780392), 1, u'default'), u'V': ((0.65098, 0.65098, 0.670588), 1, u'default'), u'Sc': ((0.901961, 0.901961, 0.901961), 1, u'default'), u'Sb': ((0.619608, 0.388235, 0.709804), 1, u'default'), u'Sg': ((0.85098, 0, 0.270588), 1, u'default'), u'Se': ((1, 0.631373, 0), 1, u'default'), u'Co': ((0.941176, 0.564706, 0.627451), 1, u'default'), u'Cm': ((0.470588, 0.360784, 0.890196), 1, u'default'), u'Cl': ((0.121569, 0.941176, 0.121569), 1, u'default'), u'Ca': ((0.239216, 1, 0), 1, u'default'), u'Cf': ((0.631373, 0.211765, 0.831373), 1, u'default'), u'Ce': ((1, 1, 0.780392), 1, u'default'), u'Xe': ((0.258824, 0.619608, 0.690196), 1, u'default'), u'Lu': ((0, 0.670588, 0.141176), 1, u'default'), u'Cs': ((0.341176, 0.0901961, 0.560784), 1, u'default'), u'Cr': ((0.541176, 0.6, 0.780392), 1, u'default'), u'Cu': ((0.784314, 0.501961, 0.2), 1, u'default'), u'La': ((0.439216, 0.831373, 1), 1, u'default'), u'Li': ((0.8, 0.501961, 1), 1, u'default'), u'Tl': ((0.65098, 0.329412, 0.301961), 1, u'default'),
u'Tm': ((0, 0.831373, 0.321569), 1, u'default'), u'Lr': ((0.780392, 0, 0.4), 1, u'default'), u'Th': ((0, 0.729412, 1), 1, u'default'), u'Ti': ((0.74902, 0.760784, 0.780392), 1, u'default'), u'tan': ((0.823529, 0.705882, 0.54902), 1, u'default'), u'Te': ((0.831373, 0.478431, 0), 1, u'default'), u'Tb': ((0.188235, 1, 0.780392), 1, u'default'), u'Tc': ((0.231373, 0.619608, 0.619608), 1, u'default'), u'Ta': ((0.301961, 0.65098, 1), 1, u'default'), u'pink': ((1, 0.752941, 0.796078), 1, u'default'), u'Yb': ((0, 0.74902, 0.219608), 1, u'default'), u'Db': ((0.819608, 0, 0.309804), 1, u'default'), u'Dy': ((0.121569, 1, 0.780392), 1, u'default'), u'I': ((0.580392, 0, 0.580392), 1, u'default'), u'U': ((0, 0.560784, 1), 1, u'default'), u'Y': ((0.580392, 1, 1), 1, u'default'), u'Ac': ((0.439216, 0.670588, 0.980392), 1, u'default'), u'Ag': ((0.752941, 0.752941, 0.752941), 1, u'default'), u'Ir': ((0.0901961, 0.329412, 0.529412), 1, u'default'), u'Am': ((0.329412, 0.360784, 0.94902), 1, u'default'), u'Al': ((0.74902, 0.65098, 0.65098), 1, u'default'), u'As': ((0.741176, 0.501961, 0.890196), 1, u'default'),
u'Ar': ((0.501961, 0.819608, 0.890196), 1, u'default'), u'Au': ((1, 0.819608, 0.137255), 1, u'default'), u'At': ((0.458824, 0.309804, 0.270588), 1, u'default'), u'In': ((0.65098, 0.458824, 0.45098), 1, u'default'), u'light gray': ((0.827451, 0.827451, 0.827451), 1, u'default')}
	materials = {u'default': ((0.85, 0.85, 0.85), 30)}
	pbInfo = {'category': [u'distance monitor'], 'bondInfo': [{'color': (0, None, {}), 'atoms': [], 'label': (0, None, {}), 'halfbond': (0, None, {}), 'labelColor': (0, None, {}), 'labelOffset': (0, None, {}), 'drawMode': (0, None, {}), 'display': (0, None, {})}], 'lineType': (1, 2, {}), 'color': (1, 6, {}), 'optional': {'fixedLabels': (True, False, (1, False, {}))}, 'display': (1, True, {}), 'showStubBonds': (1, False, {}), 'lineWidth': (1, 1, {}), 'stickScale': (1, 1, {}), 'id': [-2]}
	modelAssociations = {}
	colorInfo = (8, (u'S', (1, 1, 0.188235, 1)), {(u'N', (0.188235, 0.313725, 0.972549, 1)): [2], (u'green', (0, 1, 0, 1)): [7], (u'O', (1, 0.0509804, 0.0509804, 1)): [4], (u'tan', (0.823529, 0.705882, 0.54902, 1)): [0], (u'yellow', (1, 1, 0, 1)): [6], (u'white', (1, 1, 1, 1)): [1], (u'C', (0.564706, 0.564706, 0.564706, 1)): [3]})
	viewerInfo = {'cameraAttrs': {'center': (-4.3442264565425, 0.188098551992, 2.4396759512186), 'fieldOfView': 25.358179014236, 'nearFar': (30.086683488828, -35.936624735012), 'ortho': False, 'eyeSeparation': 50.8, 'focal': 4.2145117022151}, 'viewerAttrs': {'silhouetteColor': None, 'clipping': False, 'showSilhouette': True, 'showShadows': False, 'viewSize': 42.985421940163, 'labelsOnTop': True, 'depthCueRange': (0.5, 1), 'silhouetteWidth': 2, 'singleLayerTransparency': True, 'shadowTextureSize': 2048, 'backgroundImage': [None, 1, 2, 1, 0, 0], 'backgroundGradient': [('Chimera default', [(1, 1, 1, 1), (0, 0, 1, 1)], 1), 1, 0, 0], 'depthCue': False, 'highlight': 0, 'scaleFactor': 6.9008658219719, 'angleDependentTransparency': True, 'backgroundMethod': 0}, 'viewerHL': 7, 'cameraMode': 'mono', 'detail': 5, 'viewerFog': None, 'viewerBG': 1}

	replyobj.status("Initializing session restore...", blankAfter=0,
		secondary=True)
	from SimpleSession.versions.v65 import expandSummary
	init(dict(enumerate(expandSummary(colorInfo))))
	replyobj.status("Restoring colors...", blankAfter=0,
		secondary=True)
	restoreColors(colors, materials)
	replyobj.status("Restoring molecules...", blankAfter=0,
		secondary=True)
	restoreMolecules(molInfo, resInfo, atomInfo, bondInfo, crdInfo)
	replyobj.status("Restoring surfaces...", blankAfter=0,
		secondary=True)
	restoreSurfaces(surfInfo)
	replyobj.status("Restoring VRML models...", blankAfter=0,
		secondary=True)
	restoreVRML(vrmlInfo)
	replyobj.status("Restoring pseudobond groups...", blankAfter=0,
		secondary=True)
	restorePseudoBondGroups(pbInfo)
	replyobj.status("Restoring model associations...", blankAfter=0,
		secondary=True)
	restoreModelAssociations(modelAssociations)
	replyobj.status("Restoring camera...", blankAfter=0,
		secondary=True)
	restoreViewer(viewerInfo)

try:
	restoreCoreModels()
except:
	reportRestoreError("Error restoring core models")

	replyobj.status("Restoring extension info...", blankAfter=0,
		secondary=True)


try:
	import StructMeasure
	from StructMeasure.DistMonitor import restoreDistances
	registerAfterModelsCB(restoreDistances, 1)
except:
	reportRestoreError("Error restoring distances in session")


def restoreMidasBase():
	formattedPositions = {}
	import Midas
	Midas.restoreMidasBase(formattedPositions)
try:
	restoreMidasBase()
except:
	reportRestoreError('Error restoring Midas base state')


def restoreMidasText():
	from Midas import midas_text
	midas_text.aliases = {}
	midas_text.userSurfCategories = {}

try:
	restoreMidasText()
except:
	reportRestoreError('Error restoring Midas text state')


def restore_cap_attributes():
 cap_attributes = \
  {
   'cap_attributes': [ ],
   'cap_color': None,
   'cap_offset': 0.01,
   'class': 'Caps_State',
   'default_cap_offset': 0.01,
   'mesh_style': False,
   'shown': True,
   'subdivision_factor': 1.0,
   'version': 1,
  }
 import SurfaceCap.session
 SurfaceCap.session.restore_cap_attributes(cap_attributes)
registerAfterModelsCB(restore_cap_attributes)


def restore_volume_data():
 volume_data_state = \
  {
   'class': 'Volume_Manager_State',
   'data_and_regions_state': [ ],
   'version': 2,
  }
 from VolumeViewer import session
 session.restore_volume_data_state(volume_data_state)

try:
  restore_volume_data()
except:
  reportRestoreError('Error restoring volume data')

geomData = {'AxisManager': {}, 'CentroidManager': {}, 'PlaneManager': {}}

try:
	from StructMeasure.Geometry import geomManager
	geomManager._restoreSession(geomData)
except:
	reportRestoreError("Error restoring geometry objects in session")


def restoreSession_RibbonStyleEditor():
	import SimpleSession
	import RibbonStyleEditor
	userScalings = [('licorice', [[0.35, 0.35], [0.35, 0.35], [0.35, 0.35], [0.35, 0.35, 0.35, 0.35], [0.35, 0.35]])]
	userXSections = []
	userResidueClasses = []
	residueData = [(1, 'Chimera default', 'rounded', u'amino acid'), (2, 'Chimera default', 'rounded', u'amino acid'), (3, 'Chimera default', 'rounded', u'amino acid'), (4, 'Chimera default', 'rounded', u'amino acid'), (5, 'Chimera default', 'rounded', u'amino acid'), (6, 'Chimera default', 'rounded', u'amino acid'), (7, 'Chimera default', 'rounded', u'amino acid'), (8, 'Chimera default', 'rounded', u'amino acid'), (9, 'Chimera default', 'rounded', u'amino acid'), (10, 'Chimera default', 'rounded', u'amino acid'), (11, 'Chimera default', 'rounded', u'amino acid'), (12, 'Chimera default', 'rounded', u'amino acid'), (13, 'Chimera default', 'rounded', u'amino acid'), (14, 'Chimera default', 'rounded', u'amino acid'), (15, 'Chimera default', 'rounded', u'amino acid'), (16, 'Chimera default', 'rounded', u'amino acid'), (17, 'Chimera default', 'rounded', u'amino acid'), (18, 'Chimera default', 'rounded', u'amino acid'), (19, 'Chimera default', 'rounded', u'amino acid'), (20, 'Chimera default', 'rounded', u'amino acid'), (21, 'Chimera default', 'rounded', u'amino acid'), (22, 'Chimera default', 'rounded', u'amino acid')]
	flags = RibbonStyleEditor.NucleicDefault1
	SimpleSession.registerAfterModelsCB(RibbonStyleEditor.restoreState,
				(userScalings, userXSections,
				userResidueClasses, residueData, flags))
try:
	restoreSession_RibbonStyleEditor()
except:
	reportRestoreError("Error restoring RibbonStyleEditor state")

trPickle = 'gAJjQW5pbWF0ZS5UcmFuc2l0aW9ucwpUcmFuc2l0aW9ucwpxASmBcQJ9cQMoVQxjdXN0b21fc2NlbmVxBGNBbmltYXRlLlRyYW5zaXRpb24KVHJhbnNpdGlvbgpxBSmBcQZ9cQcoVQZmcmFtZXNxCEsBVQ1kaXNjcmV0ZUZyYW1lcQlLAVUKcHJvcGVydGllc3EKXXELVQNhbGxxDGFVBG5hbWVxDWgEVQRtb2RlcQ5VBmxpbmVhcnEPdWJVCGtleWZyYW1lcRBoBSmBcRF9cRIoaAhLFGgJSwFoCl1xE2gMYWgNaBBoDmgPdWJVBXNjZW5lcRRoBSmBcRV9cRYoaAhLAWgJSwFoCl1xF2gMYWgNaBRoDmgPdWJ1Yi4='
scPickle = 'gAJjQW5pbWF0ZS5TY2VuZXMKU2NlbmVzCnEBKYFxAn1xA1UHbWFwX2lkc3EEfXNiLg=='
kfPickle = 'gAJjQW5pbWF0ZS5LZXlmcmFtZXMKS2V5ZnJhbWVzCnEBKYFxAn1xA1UHZW50cmllc3EEXXEFc2Iu'
def restoreAnimation():
	'A method to unpickle and restore animation objects'
	# Scenes must be unpickled after restoring transitions, because each
	# scene links to a 'scene' transition. Likewise, keyframes must be 
	# unpickled after restoring scenes, because each keyframe links to a scene.
	# The unpickle process is left to the restore* functions, it's 
	# important that it doesn't happen prior to calling those functions.
	import SimpleSession
	from Animate.Session import restoreTransitions
	from Animate.Session import restoreScenes
	from Animate.Session import restoreKeyframes
	SimpleSession.registerAfterModelsCB(restoreTransitions, trPickle)
	SimpleSession.registerAfterModelsCB(restoreScenes, scPickle)
	SimpleSession.registerAfterModelsCB(restoreKeyframes, kfPickle)
try:
	restoreAnimation()
except:
	reportRestoreError('Error in Animate.Session')

def restoreLightController():
	import Lighting
	Lighting._setFromParams({'ratio': 1.25, 'brightness': 1.16, 'material': [30.0, (0.85, 0.85, 0.85), 1.0], 'back': [(0.35740674433659325, 0.6604015517481454, -0.6604015517481455), (1.0, 1.0, 1.0), 0.0], 'mode': 'two-point', 'key': [(-0.35740674433659325, 0.6604015517481454, 0.6604015517481455), (1.0, 1.0, 1.0), 1.0], 'contrast': 0.83, 'fill': [(0.25056280708573153, 0.25056280708573153, 0.9351131265310293), (1.0, 1.0, 1.0), 0.0]})
try:
	restoreLightController()
except:
	reportRestoreError("Error restoring lighting parameters")

info = [(317, 56, 100.642, 1)]
try:
	from BondRotMgr import bondRotMgr
	bondRotMgr._sessionRestore(info, version=2)
except:
	reportRestoreError("Error restoring bond rotations")


try:
	from BuildStructure.gui import _sessionRestore
	_sessionRestore({'adjust torsions': {'decimal places': 3, 'labels': 'None', 'show degree symbol': 1}, 'mapped': 0})
except:
	reportRestoreError("Failure restoring Build Structure")


def restore_surface_color_mapping():
 try:
  surface_color_state = \
   {
    'class': 'Surface_Colorings_State',
    'coloring_table': {},
    'geometry': None,
    'is_visible': False,
    'version': 2,
   }
  import SurfaceColor.session
  SurfaceColor.session.restore_surface_color_state(surface_color_state)
 except:
  reportRestoreError('Error restoring surface color mapping')

registerAfterModelsCB(restore_surface_color_mapping)


def restoreRemainder():
	from SimpleSession.versions.v65 import restoreWindowSize, \
	     restoreOpenStates, restoreSelections, restoreFontInfo, \
	     restoreOpenModelsAttrs, restoreModelClip, restoreSilhouettes

	curSelIds =  []
	savedSels = []
	openModelsAttrs = { 'cofrMethod': 4 }
	windowSize = (958, 954)
	xformMap = {0: (((0.16911923866493, 0.18213840039151, -0.96861978413422), 35.889612557768), (-33.665170122731, -0.25567892867533, 0.00088618613322789), True)}
	fontInfo = {'face': (u'Sans Serif', 'Bold', 36)}
	clipPlaneInfo = {}
	silhouettes = {0: True, 384: True}

	replyobj.status("Restoring window...", blankAfter=0,
		secondary=True)
	restoreWindowSize(windowSize)
	replyobj.status("Restoring open states...", blankAfter=0,
		secondary=True)
	restoreOpenStates(xformMap)
	replyobj.status("Restoring font info...", blankAfter=0,
		secondary=True)
	restoreFontInfo(fontInfo)
	replyobj.status("Restoring selections...", blankAfter=0,
		secondary=True)
	restoreSelections(curSelIds, savedSels)
	replyobj.status("Restoring openModel attributes...", blankAfter=0,
		secondary=True)
	restoreOpenModelsAttrs(openModelsAttrs)
	replyobj.status("Restoring model clipping...", blankAfter=0,
		secondary=True)
	restoreModelClip(clipPlaneInfo)
	replyobj.status("Restoring per-model silhouettes...", blankAfter=0,
		secondary=True)
	restoreSilhouettes(silhouettes)

	replyobj.status("Restoring remaining extension info...", blankAfter=0,
		secondary=True)
try:
	restoreRemainder()
except:
	reportRestoreError("Error restoring post-model state")
from SimpleSession.versions.v65 import makeAfterModelsCBs
makeAfterModelsCBs()

from SimpleSession.versions.v65 import endRestore
replyobj.status('Finishing restore...', blankAfter=0, secondary=True)
endRestore({})
replyobj.status('', secondary=True)
replyobj.status('Restore finished.')

