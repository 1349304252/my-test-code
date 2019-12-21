from flask import Flask, request, render_template

app = Flask(__name__)

data = {
	"user1": {
		"username": "张三",
		"password": "123456",
		"login_name": "user1"
	},
	"user2": {
		"username": "王四",
		"password": "123456",
		"login_name": "user2"
	}
}


@app.route('/to-login', methods=["GET"])
def to_login():
	return render_template("login.html")


@app.route('/login', methods=["POST"])
def login():
	login_name = request.form.get("loginName")
	password = request.form.get("password")
	try:
		user_info = data[login_name]
		if user_info["password"] == password:
			return render_template("index.html", user_info=user_info)
		else:
			msg = "密码错误"
	except KeyError:
		msg = "用户不存在"

	return render_template("login.html", error=msg)


if __name__ == '__main__':
	app.run(host='127.0.0.1', debug=False, port=58311)

