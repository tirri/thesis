'''
This script finds the messages that contain specified amount of specified topic's words.
It then randomly selects one of those messages and returns its id.

20, 39, 40, 62, 141, 142, 165, 180
3, 99, 129, 130, 143, 152, 185, 176
35, 54, 80, 126, 171, 151
74, 122

check the error with random when for loop!!


'''

from gensim import corpora
import random
import re



topic_3 = '0.029*"pärjätä" + 0.025*"hankkia" + 0.024*"tehdä" + 0.024*"raha" + 0.017*"tarvita" + 0.016*"elää" + 0.013*"riittää" + 0.013*"käydä" + 0.012*"vaate" + 0.012*"kulku" + 0.012*"koto" + 0.011*"pari" + 0.011*"pitää" + 0.011*"kunto" + 0.011*"kämppä"'

topic_20 =  '0.110*"köyhä" + 0.058*"kokoomus" + 0.053*"rikas" + 0.030*"raha" + 0.028*"eläkeläinen" + 0.023*"suomi" + 0.019*"työtön" + 0.016*"kansa" + 0.016*"pitää" + 0.014*"elää" + 0.012*"ihminen" + 0.012*"tavallinen" + 0.011*"köyhyys" + 0.009*"opiskelija" + 0.009*"lapsiperhe"'

topic_35 = '0.142*"työpaikka" + 0.087*"työ" + 0.056*"tehdä" + 0.052*"pitää" + 0.035*"sossu" + 0.027*"ihminen" + 0.025*"systeemi" + 0.024*"perse" + 0.020*"välinpitämättömyys" + 0.019*"työllistää" + 0.015*"pois" + 0.015*"raha" + 0.014*"riittää" + 0.013*"päästä" + 0.013*"ottaa"'

topic_39 = '0.066*"ihminen" + 0.028*"yhteiskunta" + 0.020*"seuraus" + 0.019*"armo" + 0.017*"todellisuus" + 0.014*"ongelma" + 0.014*"pitää" + 0.013*"tulevaisuus" + 0.013*"tarjolla" + 0.013*"tehdä" + 0.011*"elää" + 0.011*"maailma" + 0.011*"alkaa" + 0.010*"ratkaista" + 0.010*"johtaa"'

topic_54 = '0.033*"kasvaa" + 0.032*"neuvottelu" + 0.027*"irtisanoa" + 0.024*"työntekijä" + 0.023*"yt" + 0.021*"tuotanto" + 0.019*"lama" + 0.016*"henkilöstö" + 0.013*"vähentää" + 0.013*"suomi" + 0.012*"oyj" + 0.012*"kysyntä" + 0.011*"kansantalous" + 0.011*"työpaikka" + 0.011*"veronalennus"'

topic_62 = '0.300*"maksaa" + 0.067*"korvaus" + 0.046*"veronmaksaja" + 0.034*"maksa" + 0.022*"raha" + 0.020*"maksaminen" + 0.020*"korvata" + 0.020*"valtio" + 0.018*"tapaturma" + 0.016*"kustannus" + 0.013*"palkka" + 0.013*"verovarat" + 0.012*"kallis" + 0.012*"suuruinen" + 0.011*"eläkemaksu"'

topic_74 = '0.252*"nuori" + 0.100*"vanha" + 0.053*"porukka" + 0.027*"eläkeläinen" + 0.025*"pitää" + 0.019*"päästä" + 0.018*"tehdä" + 0.016*"ryppy" + 0.015*"jäädä" + 0.015*"juosta" + 0.014*"työ" + 0.014*"pelastua" + 0.013*"parasta" + 0.012*"alkaa" + 0.011*"taitaa"'

topic_80 = '0.326*"työ" + 0.155*"työtön" + 0.107*"tehdä" + 0.060*"palkka" + 0.022*"palkata" + 0.017*"homma" + 0.016*"työntekijä" + 0.015*"työpaikka" + 0.014*"tarvita" + 0.014*"elää" + 0.011*"työttömyyskorvaus" + 0.009*"päivä" + 0.009*"raha" + 0.007*"palkkatyö" + 0.007*"päästä"'

topic_99 = '0.080*"hakea" + 0.062*"myöntää" + 0.057*"työkyvyttömyyseläke" + 0.032*"kela" + 0.030*"päätös" + 0.024*"hakija" + 0.024*"hakemus" + 0.024*"työkyvyttömyys" + 0.019*"kuntoutus" + 0.019*"kuntoutus#tuki" + 0.018*"määräaikainen" + 0.016*"tieteellinen" + 0.015*"perustaminen" + 0.012*"työkyky" + 0.012*"sii"'

topic_122 = '0.108*"vuotias" + 0.097*"eläkeikä" + 0.038*"täyttää" + 0.036*"nostaa" + 0.033*"päästä" + 0.032*"ikä" + 0.029*"jäädä" + 0.027*"työ" + 0.025*"ansiosidonnainen" + 0.023*"päiväraha" + 0.020*"iätä" + 0.016*"työelämä" + 0.015*"eläke#putki" + 0.015*"pitää" + 0.014*"syntyä"'

topic_126 = '0.076*"liitto" + 0.019*"toimisto" + 0.018*"työkkäri" + 0.017*"työnhakija" + 0.015*"pitää" + 0.015*"kuulua" + 0.014*"palautua" + 0.014*"saaminen" + 0.013*"syy" + 0.012*"ilmoittautua" + 0.012*"psykiatri" + 0.011*"soveltua" + 0.011*"ehto" + 0.010*"työttömyys#turva#laki" + 0.010*"työttömyysturva"'

topic_129 = '0.120*"maksu" + 0.083*"maksa" + 0.041*"leipä" + 0.036*"sormi" + 0.034*"pappa" + 0.034*"eläkemaksu" + 0.028*"perä" + 0.026*"vanhainkoti" + 0.025*"maksaa" + 0.025*"puhdas" + 0.015*"vapaaehtoinen" + 0.014*"loppua" + 0.013*"pieru" + 0.012*"teho" + 0.012*"eläke#vakuutus#maksu"'

topic_130 = '0.116*"työntekijä" + 0.103*"pankki" + 0.094*"työnantaja" + 0.044*"maksaa" + 0.040*"korko" + 0.027*"palkka" + 0.023*"ottaa" + 0.017*"periä" + 0.017*"laina" + 0.016*"maksu" + 0.014*"maksaja" + 0.014*"irtisanominen" + 0.013*"pitää" + 0.010*"jäsenmaa" + 0.009*"strategia"'

topic_141 = '0.072*"eläke#ikä" + 0.027*"nosto" + 0.026*"kanava" + 0.025*"nostaminen" + 0.020*"eläkerahasto" + 0.018*"nykyinen" + 0.016*"nostaa" + 0.016*"eläke#järjestelmä" + 0.015*"vuode" + 0.014*"pitkä" + 0.011*"pitää" + 0.010*"ikääntyminen" + 0.009*"väestö" + 0.009*"vara" + 0.008*"tehdä"'

topic_142 = '0.064*"vanhus" + 0.050*"hoitaa" + 0.035*"hoito" + 0.027*"hoitaja" + 0.023*"pitää" + 0.019*"tarvita" + 0.013*"yhteiskunta" + 0.013*"tehdä" + 0.013*"ihminen" + 0.011*"raha" + 0.011*"sairaala" + 0.010*"omainen" + 0.010*"elää" + 0.010*"koto" + 0.010*"riittää"'

topic_143 = '0.217*"kk" + 0.088*"tulo" + 0.054*"asumistuki" + 0.044*"toimeentulotuki" + 0.026*"tuki" + 0.020*"käsi" + 0.020*"elää" + 0.018*"luukku" + 0.017*"rooma" + 0.016*"jerusalemi" + 0.013*"köyhyysraja" + 0.012*"asua" + 0.012*"yhde" + 0.011*"näyte" + 0.011*"vuokra"'

topic_151 = '0.056*"jaksaa" + 0.053*"työ" + 0.030*"tehdä" + 0.026*"raskas" + 0.020*"kurssi" + 0.017*"päästä" + 0.013*"pitää" + 0.013*"pitkä" + 0.011*"työelämä" + 0.011*"toivo" + 0.011*"sokeus" + 0.011*"loppu" + 0.010*"ikä" + 0.010*"mieli" + 0.010*"tilanne"'

topic_152 = '0.040*"korottaa" + 0.032*"ostovoima" + 0.031*"pienituloinen" + 0.031*"korotus" + 0.029*"sosiaaliturva" + 0.029*"toimeentulo" + 0.023*"elintaso" + 0.022*"työ#markkina#tuki" + 0.019*"köyhyys" + 0.018*"veroton" + 0.017*"perusturva" + 0.017*"nostaa" + 0.016*"perusosa" + 0.015*"tulo" + 0.015*"peruspäiväraha"'

topic_165 = '0.040*"tutkimus" + 0.025*"unioni" + 0.021*"kehittää" + 0.021*"kansalainen" + 0.020*"kehitys" + 0.017*"esittää" + 0.017*"yhteiskunnallinen" + 0.017*"kansainvälinen" + 0.017*"kulttuuri" + 0.015*"taso" + 0.015*"lähde" + 0.014*"osoittaa" + 0.014*"sosiaalinen" + 0.014*"synnyttää" + 0.014*"pyrkiä"'

topic_171 = '0.036*"työttömyys" + 0.030*"määrä" + 0.025*"suomi" + 0.024*"nykyinen" + 0.017*"tarvita" + 0.017*"kasvu" + 0.017*"lisääntyä" + 0.016*"kasvaa" + 0.014*"ongelma" + 0.014*"maahanmuuttaja" + 0.013*"suomalainen" + 0.012*"luku" + 0.011*"tulevaisuus" + 0.011*"maa" + 0.011*"työvoima"'

topic_176 = '0.066*"määritellä" + 0.045*"kello" + 0.044*"etuus" + 0.042*"lakkauttaa" + 0.029*"välttää" + 0.028*"automaattisesti" + 0.028*"lakisääteinen" + 0.026*"selkeästi" + 0.023*"saanti" + 0.023*"yksilöllinen" + 0.021*"suorittaa" + 0.020*"vihdoinkin" + 0.016*"omaava" + 0.016*"tehtävä" + 0.015*"eläke#tulo"'

topic_180 = '0.053*"porvari" + 0.046*"työläinen" + 0.043*"kommunisti" + 0.037*"sosialismi" + 0.031*"kapitalisti" + 0.030*"työväki" + 0.027*"kapitalismi" + 0.022*"hajaannus" + 0.020*"mtv" + 0.019*"sosialisti" + 0.018*"yhdistää" + 0.017*"propaganda" + 0.017*"hitler" + 0.015*"eriseuraisuus" + 0.014*"vallankumous"'

topic_185 = '0.224*"tuki" + 0.069*"lopettaa" + 0.057*"maatalous" + 0.040*"maanviljelijä" + 0.037*"kustantaa" + 0.028*"metsätalousministeriö" + 0.025*"kansallinen" + 0.024*"rikastua" + 0.023*"vara" + 0.021*"viljelijä" + 0.018*"jako" + 0.013*"maataloustuki" + 0.013*"raha" + 0.011*"veikata" + 0.011*"veronmaksaja"'

def main():
    model_version = 200
    data = corpora.MmCorpus('/Users/tirri/LDA/%stopics.mm' % (model_version))
    list_of_relevant_messages_in_all_topics = []
    topics = [topic_3, topic_20, topic_35, topic_39, topic_54, topic_62, topic_74, topic_80, topic_99,
               topic_122, topic_126, topic_129, topic_130, topic_141, topic_142, topic_143, topic_151, topic_152,
               topic_165, topic_171, topic_176, topic_180, topic_185]
    i= 1
    for topic in topics:
        print('got to the beginning of for loop, handling the following topic:')
        print(topic)
        words_in_topic = do_the_regex(topic)
        print(words_in_topic)
        all_relevant_messages = get_relevant_messages(data, words_in_topic)
        print(all_relevant_messages)
        randomly_selected_relevant_message = random_sample_of_message_ids(all_relevant_messages)
        list_of_relevant_messages_in_all_topics.append(i)
        i +=1
        list_of_relevant_messages_in_all_topics.append(randomly_selected_relevant_message)
        print('got to the end of for loop')
    print(list_of_relevant_messages_in_all_topics)

def message_to_list_of_words(n_of_message):
    with open('/Users/tirri/LDA/bows/file%s.txt.lemma' % (n_of_message)) as file:
        text = file.readline()
        message = [word for word in text.split()]
    return message

def words_match_message(words_to_match, message):
    if len(message) < 51:
        if len(set(words_to_match) & set(message)) > 2:
            return True
    else:
        return False

def get_relevant_messages(data, words_to_match):
    relevant_messages = []
    for message_id in range(1, len(data)):
        message = message_to_list_of_words(message_id)
        if words_match_message(words_to_match, message):
            relevant_messages.append(message_id)
    return relevant_messages

def random_sample_of_message_ids(ids):
    random_item = random.choice(ids)
    print('selected message number: %s' % random_item)
    return random_item

def do_the_regex(topic_words):
    regex = r'\"\w{1,}\"'
    words_in_hips = re.findall(regex, topic_words)
    only_words = [word.replace('"', '') for word in words_in_hips]
    return only_words

main()

