from flask import Flask, render_template, request

app = Flask(__name__)

# Дефинирање на прашањата (20 прашања)
questions = [
    # 4-годишни (Техничари)
    {"id": 1, "text": "Дали те интересира како работат компјутерските процесори и меморијата?", "cat": "komp"},
    {"id": 2, "text": "Дали уживаш во пишување код (C++, JavaScript, HTML)?", "cat": "komp"},
    {"id": 3, "text": "Дали сакаш да монтираш видео материјали и да додаваш ефекти?", "cat": "multi"},
    {"id": 4, "text": "Дали те привлекува графички дизајн и дигитална илустрација?", "cat": "multi"},
    {"id": 5, "text": "Дали би сакал да работиш на одржување на големи енергетски мрежи?", "cat": "energo"},
    {"id": 6, "text": "Дали те интересира како се произведува струја во електраните?", "cat": "energo"},
    {"id": 7, "text": "Дали те фасцинира како работат паметните телефони и антените?", "cat": "elektronika"},
    {"id": 8, "text": "Дали би сакал да лемиш мали електронски компоненти на плочки?", "cat": "elektronika"},
    {"id": 9, "text": "Дали сакаш да решаваш логички проблеми и математички загатки?", "cat": "komp"},
    {"id": 10, "text": "Дали би сакал да креираш анимации за веб страни?", "cat": "multi"},

    # 3-годишни (Занаетчии)
    {"id": 11, "text": "Дали сакаш да поправаш расипани кујнски апарати (миксери, машини)?", "cat": "mehanic"},
    {"id": 12, "text": "Дали би сакал да монтираш штекери и светлосни инсталации во куќи?", "cat": "monter"},
    {"id": 13, "text": "Дали повеќе сакаш практична работа со раце отколку седење пред компјутер?", "cat": "mehanic"},
    {"id": 14, "text": "Дали те интересира како се поставуваат кабли за струја во згради?", "cat": "monter"},
    {"id": 15, "text": "Дали сакаш да расклопуваш мотори и електрични машини?", "cat": "mehanic"},

    # Општи/Микс
    {"id": 16, "text": "Дали те интересира роботика и автоматизирани машини?", "cat": "komp"},
    {"id": 17, "text": "Дали сакаш да работиш со професионални камери и осветлување?", "cat": "multi"},
    {"id": 18, "text": "Дали би сакал да работиш во компанија како ЕВН или МЕПСО?", "cat": "energo"},
    {"id": 19, "text": "Дали сакаш да инсталираш безбедносни камери и аларми?", "cat": "monter"},
    {"id": 20, "text": "Дали те интересира пренос на податоци преку оптички кабли?", "cat": "elektronika"}
]


@app.route('/')
def quiz():
    return render_template('quiz.html', questions=questions)


@app.route('/result', methods=['POST'])
def result():
    edu_type = request.form.get('edu_type')
    scores = {"komp": 0, "multi": 0, "energo": 0, "elektronika": 0, "mehanic": 0, "monter": 0}

    for q in questions:
        answer = request.form.get(f"q{q['id']}")
        if answer == "yes":
            scores[q['cat']] += 1

    # Филтер според годините што ги бираме
    if edu_type == "4":
        final_pool = {k: v for k, v in scores.items() if k in ["komp", "multi", "energo", "elektronika"]}
    else:
        final_pool = {k: v for k, v in scores.items() if k in ["mehanic", "monter"]}

    winner_key = max(final_pool, key=final_pool.get)

    profiles = {
        "komp": "Компјутерска техника и автоматика",
        "multi": "Мултимедиски технологии",
        "energo": "Електротехничар - Енергетичар",
        "elektronika": "Електроника и телекомуникации",
        "mehanic": "Електромеханичар",
        "monter": "Електроинсталатер и монтер"
    }

    return render_template('result.html', profile=profiles[winner_key])


if __name__ == '__main__':
    app.run(debug=True)