memory_store = []


def remember_analysis(text, final_prediction):

    entry = {

        "text": text,

        "prediction": final_prediction
    }

    memory_store.append(entry)

    return {

        "agent": "Memory Agent",

        "memory_size": len(memory_store),

        "last_prediction": final_prediction
    }


def get_memory():

    return memory_store