from plumbum import cli, colors
import os
from plumbum import local

import classification
import fronts
path = "/home/riccardo/.notes/"
file = "notes.txt"
if not os.path.exists(path):
    os.makedirs(path)


class Notes(cli.Application):
    """Application for notes
    """
    PROGNAME = "notes"
    VERSION = "0.1"

    def main(self):
        if not self.nested_command:           # will be ``None`` if no sub-command follows
            print("No command given")
            return 1   # error exit code

@Notes.subcommand("add")
class Add(cli.Application):
    "add notes to the main file"
    priority = cli.Flag(["p", "priority"], help = "If given, I will be very prioritive")
    def main(self, value : str):
      if not os.path.exists (path+file):
        f=open(path+file, "w+")
      else:
        f=open(path+file, "a")
        if(self.priority):
          danger = colors.red|"\u26A0"
          f.write("[ ] "+danger+"   "+value+"\n" )
        else:
          f.write("[ ] "+ value+"\n" )

@Notes.subcommand("show")
class Show(cli.Application):
    "show the notes on the file"
    def main(self):
      if not os.path.exists (path+file):
        print("no file notes.txt found")
      else:
        f=open(path+file, "r")
        a = f.read()
        print(a)

@Notes.subcommand("find")
class Find(cli.Application):
  "find words in the file notes"
  def main(self, word : str):
    word = word.lower()
    found = 0
    if not os.path.exists (path+file):
      print("no file notes.txt found")
    else:
      for line in open(path+file, "r"):
        if word in line.lower():
          print(line)
          found = found +1


    if found == False:
          print("word not found")


@Notes.subcommand("done")
class Done(cli.Application):
  "Puts a tick on the thing that i have done"
  def main(self, word : str):
    copy=open(path+"copy"+file, "w")
    word = word.lower()
    found = 0
    if not os.path.exists (path+file):
      print("no file notes.txt found")
    else:
      copy=open(path+"copy"+file, "a")
      for line in open(path+file, "r"):
        if word in line.lower():
          stanghetta = colors.green|"\u2713"
          line = line.replace('[ ]',"["+stanghetta+"]")
          copy.write(line)
          found = found + 1
        else:
          copy.write(line)

    if found == True :
      mv = local["mv"]
      mv(path+"copy"+file,path+file)

    else:
          print("word not found")

@Notes.subcommand("remove")
class Remove(cli.Application):
  "Remove the thing with the keyword you give"
  def main(self, word : str):
    stanghetta = colors.green|"\u2713"
    copy=open(path+"copy"+file, "w")
    word = word.lower()
    found = 0
    if not os.path.exists (path+file):
      print("no file notes.txt found")
    else:
      copy=open(path+"copy"+file, "a")
      for line in open(path+file, "r"):
        if word in line.lower():
            # if stanghetta in line.lower():
            #     pass
            # else:
            #     print("you don'have done this thing yet, are you sure to remove it? [y/n]")
            #     @Notes.subcommand("y")
            #     class Sure(cli.Application):
            #         "Are you sure?"
            #         def main(self, answer : str):
            #             if answer in ["y","yes","Yes","YES"]:
            #                 pass
            #             else:
            #                 copy.write(line)
            found = found + 1
        else:
            copy.write(line)

    if found == True :
      mv = local["mv"]
      mv(path+"copy"+file,path+file)

    else:
          print("word not found")


if __name__ == "__main__":
    Notes.run()
