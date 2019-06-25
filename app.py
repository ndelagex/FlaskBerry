from flask import Flask, render_template
import sqlite3, os, psycopg2
app = Flask(__name__)
app.debug = True

@app.route("/")
def main():
    if os.path.isfile('lab_app.db'):
      conn = sqlite3.connect('lab_app.db')
    else:
      url = os.environ.get('DATABASE_URL') #postgres url in heroku
      conn = psycopg2.connect(url, sslmode='require')

    curs = conn.cursor()
    curs.execute("SELECT * FROM temperatures order by rDatetime desc limit 1")
    temperatures = curs.fetchall()
    curs.execute("SELECT * FROM humidities order by rDatetime desc limit 1")
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
