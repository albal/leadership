from flask import Flask, render_template
import random

app = Flask(__name__)

app_title = "Leadership Principles"

principles = {'Customer Obsession': 'Leaders start with the customer and work backwards.  They work vigorously to earn '
                                    'and keep customer trust.  Although leaders pay attention to competitors, they '
                                    'obsess over customers.',
              'Ownership': "Leaders are owners.  They think long term and don't sacrifice long-term value for "
                           "short-term results.  They act on behalf of the entire company, beyond just their own "
                           "team.  They never say \"That's not my job.\"",
              'Invent and simplify': 'Leaders expect and require innovation from their teams and always find ways to '
                                     'simplify.  They are extremely aware, look for new ideas from everywhere, and are '
                                     'not limited by "not invented here."  Because we do new things, we accept that we '
                                     'may be misunderstood for long periods of time.',
              'Are right, a lot': 'Leaders are right a lot.  They have strong judgement and good instincts.  They seek '
                                  'diverse perspectives and work to dis-confirm their beliefs',
              'Learn and be curious': 'Leaders are never done learning and always seek to improve themselves.  They '
                                      'are curious about new possibilities and act to explore them.',
              'Hire and develop the best': 'Leaders raise the performance bar with every hire and promotion.  They '
                                           'recognise people with exceptional talent and willingly move them '
                                           'throughout the organisation.  Leaders develop leaders and are serious '
                                           'about their role in coaching other.  We work on behalf of our people to '
                                           'invent mechanisms for development like Career Choice.',
              'Insist on the highest standards': 'Leaders have relentlessly high standards - many people may think '
                                                 'these standards are unreasonably high.  Leaders are continually '
                                                 'raising the bar and driving their teams to deliver high quality '
                                                 'products, services, and processes.  Leaders ensure that defect do '
                                                 'not get sent down the line and problems are fixed to they stay '
                                                 'fixed.',
              'Think big': 'Thinking small is a self-fulfilling prophecy.  Leader create and communicate a bold '
                           'direction that inspires results.  They think differently and lok around corners for ways '
                           'to service customers.',
              'Bias for action': 'Speed matters in business.  Many decisions and actions are reversible and do not '
                                 'need extensive study.  We value calculated risk taking.',
              'Frugality': 'Accomplish more with less.  Constraints breed resourcefulness, self-sufficiency and '
                           'invention.  There are no extra points for growing headcount, budget size or fixed expense.',
              'Earn trust': 'Leader listen attentively, speak candidly, and treat other respectfully.  '
                            'They are vocally self-critical, even when doing so is awkward or embarrassing.',
              'Dive deep': 'Leaders operate at all levels, stay connected to the details, audit frequently, and are '
                           'sceptical when metrics and anecdote differ.  No task is beneath them.',
              'Have backbone; disagree and commit': 'Leaders are obligated to respectfully challenge decisions when '
                                                    'they disagree. even when doing so is uncomfortable or '
                                                    'exhausting.  Leaders have conviction and are tenacious.  They do '
                                                    'not compromise for the sake of social cohesion.  Once a decision '
                                                    'is determined, they commit wholly.',
              'Deliver results': 'Leaders focus on the key inputs for their business and deliver them with the right '
                                 'quality amd in a timely fashion.  Despite setbacks, they rise to the occasion '
                                 'and never compromise.'
              }


@app.route('/')
def welcome():
    return render_template("Home.html", title=app_title)


@app.route('/<int:param>')
def principle(param):
    if param >= 0:
        if param < len(principles):
            return render_template("Principle.html", title=app_title, principle=list(principles.keys())[param],
                                   description=list(principles.values())[param], num=param, total=len(principles))
    return out_of_range_message()


@app.route('/random')
def random_principle():
    items = len(principles)
    param = random.randint(0, items - 1)
    return principle(param)


@app.route('/principles')
def all_principles():
    return render_template("Principles.html", title=app_title, principles=principles.keys())


def out_of_range_message():
    return "Out of range: must be between 0 and " + str(len(principles) - 1)
