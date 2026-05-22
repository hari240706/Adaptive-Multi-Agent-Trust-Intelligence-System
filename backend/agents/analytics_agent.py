from agents.database_agent import (

    get_recent_analyses,

    get_database_stats
)

from agents.vector_memory_agent import (
    
    get_vector_database_stats
)


# =========================
# System Analytics
# =========================

def get_system_analytics():

    database_stats = get_database_stats()

    vector_stats = get_vector_database_stats()

    return {

        "agent":
        "Analytics Agent",

        "database_stats":
        database_stats,

        "vector_memory_stats":
        vector_stats
    }


# =========================
# Historical Analyses
# =========================

def get_analysis_history():

    history = get_recent_analyses()

    return {

        "agent":
        "Analytics Agent",

        "recent_analyses":
        history
    }