from time import time


def tperror(prompt):
    global inwords

    words = prompt.split()

    error = 0
    for i in range(len(inwords)):
        if i in (0, len(inwords)-1):
            if inwords[i] == words[i]:
                continue
            else:
                error = error + 1

        else:
            if inwords[i] == words[i]:
                if (inwords[i+1]==words[i+1]) & (inwords[i-1]== words[i-1]):
                    continue

                else:
                    error += 1

            else:
                error +=1

    return  error


def speed(inprompt, stime, etime):
    global time
    global inwords

    inwords = inprompt.split()
    twords = len(inwords)
    speed = twords / time
    return speed


def elapsedtime(stime, etime):
    time = etime - stime
    return time


if __name__ == "__main__":
    prompt = "India, officially the Republic of India ,[23] is a country in South Asia. It is the second-most populous country, the seventh-largest country by land area, and the most populous democracy in the world. Bounded by the Indian Ocean on the south, the Arabian Sea on the southwest, and the Bay of Bengal on the southeast, it shares land borders with Pakistan to the west China, Nepal, and Bhutan to the north and Bangladesh and Myanmar to the east. In the Indian Ocean, India is in the vicinity of Sri Lanka and the Maldives its Andaman and Nicobar Islands share a maritime border with Thailand, Myanmar and Indonesia."
    print("type this :- ", prompt, "")
    input("press enter when u r ready")
    stime = time()
    inprompt = input()
    etime = time()

    time = round(elapsedtime(stime, etime), 2)
    speed = speed(inprompt, stime, etime)
    error = tperror(prompt)

    print("Total time elapsed:", time, "seconnd")
    print("your average typing speed was", speed, "words per minute(w/m)")
    print("with the total of", error, "errors")







