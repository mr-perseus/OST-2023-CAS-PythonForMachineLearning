import random


class HtmlCreator:
    def __init__(self, model):
        self.model = model

    def export_as_html(self):
        result = """     <html>
                             <head>
                                  <style>
                                     td {
                                         font-size: 18pt;
                                     }
                                 </style>
                             </head>
                         <body>
                         """

        result += self.create_table()
        result += self.create_word_list()

        result += """        </body>
                         </html>
                         """

        return result

    def create_word_list(self):
        result = "<ul>"

        for word in self.model.get_words_to_search():
            result += "<li>" + word + "</li>"

        result += "</ul>"

        return result

    def create_table(self):
        result = "<table border = '3' style='text-align:center'"

        for y in range(self.model.get_board_height()):
            result += "<tr>"
            for x in range(self.model.get_board_width()):
                result += "<td>" + self.model.get_at(x, y) + "</td>"
            result += "</tr>"

        result += "</table>"

        return result


    def exportAsHtmlOld(self):
        result = """
                                       <html>
                                           <head>
                                               <style>
                                               td {
                                                font-size: 18pt;
                                               }
                                               </style>
                                         </head>
                                         <body>
                                         """

        result += "<table border = '3' style='text-align:center'"
        for y in range(10):
            result += "<tr>"

            for x in range(20):
                # https://pynative.com/python-random-randrange/
                value = random.choice(["A", "B", "C", "D", "E", "F"])
                result += "<td>" + value + "</td>"

            result += "</tr>"

        result += "</table>"

        # result += "<ul>"
        # for (String word: getWordsToSearch())
        # result += "<li>" + word + "</li>";
        #
        # result += "</ul>"
        result += """
                                    </body>
                                </html>
                                """
        return result
