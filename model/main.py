#importing required modules
import codecs
import unidecode
import re
import spacy
from contraction_mapping import contraction_mapping
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import precision_score, recall_score, f1_score


nlp = spacy.load('en')

class main:
    def spacy_cleaner(text):
        """
        This function uses Spacy module to pre-process the input text.
        input: Text
        output: Cleaned Text
        """
        try:
            decoded = unidecode.unidecode(codecs.decode(text, 'unicode_escape'))

        except:
            decoded = unidecode.unidecode(text)

        apostrophe_handled = re.sub("’", "'", decoded)
        expanded = ' '.join([contraction_mapping[t] if t in contraction_mapping else t for t in apostrophe_handled.split(" ")])
        parsed = nlp(expanded)
        final_tokens = []

        for t in parsed:
            if t.is_punct or t.is_space or t.like_num or t.like_url or str(t).startswith('@'):
                pass

            else:
                if t.lemma_ == '-PRON-':
                    final_tokens.append(str(t))

                else:
                    sc_removed = re.sub("[^a-zA-Z]", '', str(t.lemma_))
                    if len(sc_removed) > 1:
                        final_tokens.append(sc_removed)

        joined = ' '.join(final_tokens)
        spell_corrected = re.sub(r'(.)\1+', r'\1\1', joined)
        return spell_corrected
    

    def lr_cv(splits, X, Y, pipeline, average_method):
        """
        This function created a pipeline for the model and prints the precision,
         recall and F1 score from model output
         parms:
            splits: Number of folds needed for k-fold
            X: Feature
            Y: Label
            pipline: pipline object
            average_method: Method Type to handle im balanced data
        """
        # applying kfold
        kfold = StratifiedKFold(n_splits=splits, shuffle=True, random_state=777)
        accuracy = []
        precision = []
        recall = []
        f1 = []
        for train, test in kfold.split(X, Y):
            # fitting the splitted x and y
            lr_fit = pipeline.fit(X[train], Y[train])

            # predicting
            prediction = lr_fit.predict(X[test])

            # scoring
            scores = lr_fit.score(X[test],Y[test])

            # calculating the accuracy.
            accuracy.append(scores * 100)

            # calculating the precision
            precision.append(precision_score(Y[test], prediction, average=average_method)*100)

            # printing the precision, recall and F1 score from model output
            print('              negative    neutral     positive')
            print('precision:',precision_score(Y[test], prediction, average=None))
            recall.append(recall_score(Y[test], prediction, average=average_method)*100)
            print('recall:   ',recall_score(Y[test], prediction, average=None))
            f1.append(f1_score(Y[test], prediction, average=average_method)*100)
            print('f1 score: ',f1_score(Y[test], prediction, average=None))
            print('-'*50)
        return lr_fit

        print("accuracy: %.2f%% (+/- %.2f%%)" % (np.mean(accuracy), np.std(accuracy)))
        print("precision: %.2f%% (+/- %.2f%%)" % (np.mean(precision), np.std(precision)))
        print("recall: %.2f%% (+/- %.2f%%)" % (np.mean(recall), np.std(recall)))
        print("f1 score: %.2f%% (+/- %.2f%%)" % (np.mean(f1), np.std(f1)))


