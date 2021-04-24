import genanki
import os
import random

def createAPKG(name):
  my_model = genanki.Model(
  1380120064,
  'Example',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ])
  deckId = random.randint(1000000000,9900000000)
  my_deck = genanki.Deck(
    deckId,
    name)
  DIRECTORY = "Temp"
  count=0
  filelist = sorted(os.listdir(DIRECTORY))
  filelist.remove('input.pdf')
  #print(filelist)
  while count<len(filelist):
    field1 = '<img src="%s"\>' % (filelist[count])
    field2 = '<img src="%s"\>' % (filelist[count+1])
    my_note = genanki.Note(model=my_model,fields=[field1,field2])
    my_deck.add_note(my_note)
    count=count+2
  my_package = genanki.Package(my_deck)
  for x in filelist:
    my_package.media_files.append('Temp'+os.sep+x)
  my_package.write_to_file('%s.apkg' % name)