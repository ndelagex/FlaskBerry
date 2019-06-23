from flask import Flask, render_template
import sqlite3
app = Flask(__name__)
app.debug = True

@app.route("/")
def main():
    conn = sqlite3.connect('lab_app.db')
    curs = conn.cursor()
    curs.execute("SELECT * FROM temperatures limit 1")
    temperatures = curs.fetchall()
    curs.execute("SELECT * FROM humidities limit 1")
    humidities = curs.fetchall()

    temperature = temperatures[0][2]
    humidity = humidities[0][2]

    #humidity, temperature = (0,0)
    if humidity is not None and temperature is not None:
      return render_template("lab_temp.html",temp=temperature,hum=humidity)
    else:
      return render_template("no_sensor.html")

@app.route("/example")
def example_route():
  return "This is another route"

if __name__ == "__main__":
    app.run()
