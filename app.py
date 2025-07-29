from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/oner', methods=['POST'])
def aktivite_oner():
    data = request.get_json()

    ruh_hali = data.get("ruhHali", "normal")
    yorgunluk = data.get("yorgunluk", "orta")
    hava = data.get("havaDurumu", "bulutlu")
    saat = data.get("saat", "öğlen")
    disarda_sure = data.get("sure", 60)
    yaninda_var_mi = data.get("yanindaBirileriVarMi", False)

    # Basit kural tabanlı öneri (şimdilik)
    if ruh_hali == "yorgun" and hava == "yağmurlu":
        tavsiye = "Evde kitap oku veya hafif bir film izle"
    elif yorgunluk == "düşük" and hava == "güneşli":
        tavsiye = "Yakındaki bir parkta yürüyüş yap"
    else:
        tavsiye = "Kısa bir kahve molası iyi gelebilir"

    return jsonify({"tavsiye": tavsiye})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

