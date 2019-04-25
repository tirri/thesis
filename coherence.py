from gensim import models, corpora

model_version = '5' # 5, 25, 50, 100 or 200

corpus = corpora.MmCorpus('/Users/tirri/LDA/%stopics.mm' % (model_version))
model = models.LdaModel.load('/Users/tirri/LDA/%stopics.model' % (model_version))

cm = models.CoherenceModel(model = model, corpus = corpus, coherence = 'u_mass')

print(cm.get_coherence())