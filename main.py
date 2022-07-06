# top to bottom design of backend
# should gerenate the following code from a jb
from model import * # EMO_AI/model.py

def main():
    while waiting_for_input():
        input = get_user_input()
        parsed_input = parse_user_input(input)
        output = call_model(parsed_input)
        # output should be a matrix
        #  if one wants to print output, parse it back first
        # print(output)
        # todo: plot the emotional coordinate thing as well
        # aka, 畫那個四個象限情緒的東西
        plot_emotion(output)


def call_model(input_string, PATH = "pretrained_weight.pt"):
    # this is done, but not tested
    model = get_pretrained_model(PATH)

    # working on it
    parsed_input = parse_input(input_string)

    # get inferenced output
    output = model.forward(parsed_input)

    return output

# parse the user input to tokens
# so that it can be fed into the model for inference
def parse_input(input_string):
    # related to TokenizersCollateFn() class
    pass


# plot the user data on the emotional coordinate
def plot_emotion(output):
    # get a bunch of existing data (test data ?)

    # plot the user output along with existing data
    #  on the emotional coordinate

    # construct emotional coordinate: ... (see the paper?)
    #  it's probably an 2d array

    # plot everything on the same plot, matplotlib would do the job
    pass



