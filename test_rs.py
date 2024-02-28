from sybil import Serie, Sybil

# Load a trained model
model = Sybil("sybil_base")

# Get risk scores
serie = Serie(['D:/#Software Repository/Sybil/dicom/dicom/A2.orb.6c87.it.orbassano.S1.2421804.1_00001.DCM'])
scores = model.predict([serie])

# You can also evaluate by providing labels
serie = Serie(['D:/#Software Repository/Sybil/dicom/dicom/A2.orb.6c87.it.orbassano.S1.2421804.1_00001.DCM'], label=1)
results = model.evaluate([serie])


