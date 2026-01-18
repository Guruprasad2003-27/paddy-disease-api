def recommend_treatment(disease):
    recommendations = {

        "bacterial_leaf_blight": {
            "medicine": "Streptomycin sulphate + Copper oxychloride",
            "fertilizer": "Balanced NPK, avoid excess nitrogen",
            "advice": "Ensure proper drainage and avoid water stagnation"
        },

        "bacterial_leaf_streak": {
            "medicine": "Copper-based bactericide",
            "fertilizer": "Potassium-rich fertilizer",
            "advice": "Use disease-free seeds"
        },

        "blast": {
            "medicine": "Tricyclazole or Isoprothiolane",
            "fertilizer": "Reduce nitrogen, add potassium",
            "advice": "Maintain proper plant spacing"
        },

        "brown_spot": {
            "medicine": "Mancozeb or Carbendazim",
            "fertilizer": "Apply Zinc and Potash",
            "advice": "Improve soil nutrition"
        },

        "tungro": {
            "medicine": "No direct cure – control leafhoppers",
            "fertilizer": "Apply recommended NPK",
            "advice": "Remove infected plants immediately"
        },

        "normal": {
            "medicine": "No treatment required",
            "fertilizer": "Regular NPK fertilizer",
            "advice": "Crop is healthy"
        }
    }

    return recommendations.get(
        disease,
        {
            "medicine": "Consult agriculture officer",
            "fertilizer": "Soil test recommended",
            "advice": "Disease not recognized"
        }
    )
