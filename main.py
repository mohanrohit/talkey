import os
import random
import requests
import bs4

end = 0

def random_words():
  with open("words.txt") as word_file:
    words = word_file.readlines()
  end

  word_index = random.randint(0, len(words) + 1)
  word = words[word_index]
  print word

  response = requests.get(
    "https://www.dictionaryapi.com/api/v1/references/collegiate/xml/%s?key=67e327bd-2354-4c12-ba32-6a0ae735e900" % word,
    ssl_verify=False
  )

  soup = bs4.BeautifulSoup(response.text, "lxml-xml")

  audio_file_name = soup.entry.sound.wav.string
  audio_file_url = "https://media.merriam-webster.com/soundc11/%s/%s" % (audio_file_name[0], audio_file_name)

  if not os.path.exists(audio_file_name):
    download_response = requests.get(audio_file_url,ssl_verify=False)

    with open(audio_file_name, "wb") as audio_file:
      for file_chunk in download_response.iter_content(chunk_size = 1024 * 1024):
        if file_chunk:
          audio_file.write(file_chunk)
          audio_file.flush()
        end
      end
    end
  end

  os.system("aplay %s" % audio_file_name)
end

def all_words():
  with open("words.txt") as word_file:
    words = word_file.readlines()
  end

  for word in sorted(words):
    word = word.strip()

    if len(word) == 0:
      continue
    end

    print "Your word is '" + word + "'"

    response = requests.get(
      "https://www.dictionaryapi.com/api/v1/references/collegiate/xml/%s?key=67e327bd-2354-4c12-ba32-6a0ae735e900" % word
    )

    soup = bs4.BeautifulSoup(response.text, "lxml-xml")

    try:
      audio_file_name = soup.entry.sound.wav.string
      audio_file_url = "https://media.merriam-webster.com/soundc11/%s/%s" % (audio_file_name[0], audio_file_name)

      if not os.path.exists(audio_file_name):
        download_response = requests.get(audio_file_url)

        with open(audio_file_name, "wb") as audio_file:
          for file_chunk in download_response.iter_content(chunk_size = 1024 * 1024):
            if file_chunk:
              audio_file.write(file_chunk)
              audio_file.flush()
            end
          end
        end
      end

      os.system("aplay %s" % audio_file_name)
    except:
      print "'%s' does not have an audio file" % word
    end

    raw_input("\nPress <enter> for the next word (Ctrl+C to end).\n")
  end
end

all_words()
