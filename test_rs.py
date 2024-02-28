from sybil import Serie, Sybil

# Load a trained model
model = Sybil("sybil_base")

# Get risk scores
serie = Serie(['E:\LDCT_sybil\A2.orb.66e3.it.orbassano.S1.3968019.1_00001.DCM'])
scores = model.predict([serie])

# You can also evaluate by providing labels
# serie = Serie(['E:\LDCT_sybil\A2.orb.66e3.it.orbassano.S1.3968019.1_00001.DCM'], label=1)
# results = model.evaluate([serie])


